import time
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pandas import DataFrame

from ..call_parameters import CallParameters
from .gds_arrow_client import GdsArrowClient
from .query_runner import QueryRunner
from graphdatascience.query_runner.graph_constructor import GraphConstructor
from graphdatascience.server_version.server_version import ServerVersion


class AuraDbQueryRunner(QueryRunner):
    GDS_REMOTE_PROJECTION_PROC_NAME = "gds.arrow.project"

    def __init__(
        self,
        gds_query_runner: QueryRunner,
        db_query_runner: QueryRunner,
        arrow_client: GdsArrowClient,
        encrypted: bool,
    ):
        self._gds_query_runner = gds_query_runner
        self._db_query_runner = db_query_runner
        self._gds_arrow_client = arrow_client
        self._encrypted = encrypted

    def run_cypher(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
        database: Optional[str] = None,
        custom_error: bool = True,
    ) -> DataFrame:
        return self._db_query_runner.run_cypher(query, params, database, custom_error)

    def call_function(self, endpoint: str, params: Optional[CallParameters] = None) -> Any:
        return self._gds_query_runner.call_function(endpoint, params)

    def call_procedure(
        self,
        endpoint: str,
        params: Optional[CallParameters] = None,
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        logging: bool = False,
        custom_error: bool = True,
    ) -> DataFrame:
        if params is None:
            params = CallParameters()

        if AuraDbQueryRunner.GDS_REMOTE_PROJECTION_PROC_NAME == endpoint:
            return self._remote_projection(endpoint, params, yields, database, logging)

        elif ".write" in endpoint and self.is_remote_projected_graph(params["graph_name"]):
            return self._remote_write_back(endpoint, params, yields, database, logging, custom_error)

        return self._gds_query_runner.call_procedure(endpoint, params, yields, database, logging, custom_error)

    def is_remote_projected_graph(self, graph_name: str) -> bool:
        database_location: str = self._gds_query_runner.call_procedure(
            endpoint="gds.graph.list",
            yields=["databaseLocation"],
            params=CallParameters(graph_name=graph_name),
        ).squeeze()
        return database_location == "remote"

    def server_version(self) -> ServerVersion:
        return self._db_query_runner.server_version()

    def driver_config(self) -> Dict[str, Any]:
        return self._db_query_runner.driver_config()

    def encrypted(self) -> bool:
        return self._db_query_runner.encrypted()

    def set_database(self, database: str) -> None:
        self._db_query_runner.set_database(database)

    def set_bookmarks(self, bookmarks: Optional[Any]) -> None:
        self._db_query_runner.set_bookmarks(bookmarks)

    def bookmarks(self) -> Optional[Any]:
        return self._db_query_runner.bookmarks()

    def last_bookmarks(self) -> Optional[Any]:
        return self._db_query_runner.last_bookmarks()

    def database(self) -> Optional[str]:
        return self._db_query_runner.database()

    def create_graph_constructor(
        self, graph_name: str, concurrency: int, undirected_relationship_types: Optional[List[str]]
    ) -> GraphConstructor:
        return self._gds_query_runner.create_graph_constructor(graph_name, concurrency, undirected_relationship_types)

    def close(self) -> None:
        self._gds_arrow_client.close()
        self._gds_query_runner.close()
        self._db_query_runner.close()

    def _remote_projection(
        self,
        endpoint: str,
        params: CallParameters,
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        logging: bool = False,
    ) -> DataFrame:
        self._inject_arrow_config(params["arrow_configuration"])
        return self._db_query_runner.call_procedure(endpoint, params, yields, database, logging, False)

    def _remote_write_back(
        self,
        endpoint: str,
        params: CallParameters,
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        logging: bool = False,
        custom_error: bool = True,
    ) -> DataFrame:
        if params["config"] is None:
            params["config"] = {}

        # we pop these out so that they are not retained for the GDS proc call
        db_arrow_config = params["config"].pop("arrowConfiguration", {})  # type: ignore
        self._inject_arrow_config(db_arrow_config)

        job_id = params["config"]["jobId"] if "jobId" in params["config"] else str(uuid4())  # type: ignore
        params["config"]["jobId"] = job_id  # type: ignore

        params["config"]["writeToResultStore"] = True  # type: ignore

        gds_write_result = self._gds_query_runner.call_procedure(
            endpoint, params, yields, database, logging, custom_error
        )

        db_write_proc_params = {
            "graphName": params["graph_name"],
            "databaseName": self._gds_query_runner.database(),
            "jobId": job_id,
            "arrowConfiguration": db_arrow_config,
        }

        write_back_start = time.time()
        database_write_result = self._db_query_runner.call_procedure(
            "gds.arrow.write", CallParameters(db_write_proc_params), yields, None, False, False
        )
        write_millis = (time.time() - write_back_start) * 1000
        gds_write_result["writeMillis"] = write_millis

        if "nodePropertiesWritten" in gds_write_result:
            gds_write_result["nodePropertiesWritten"] = database_write_result["writtenNodeProperties"]
        if "propertiesWritten" in gds_write_result:
            gds_write_result["propertiesWritten"] = database_write_result["writtenNodeProperties"]
        if "nodeLabelsWritten" in gds_write_result:
            gds_write_result["nodeLabelsWritten"] = database_write_result["writtenNodeLabels"]
        if "relationshipsWritten" in gds_write_result:
            gds_write_result["relationshipsWritten"] = database_write_result["writtenRelationships"]

        return gds_write_result

    def _inject_arrow_config(self, params: Dict[str, Any]) -> None:
        host, port = self._gds_arrow_client.connection_info()
        token = self._gds_arrow_client.request_token()
        if token is None:
            token = "IGNORED"

        params["host"] = host
        params["port"] = port
        params["token"] = token
        params["encrypted"] = self._encrypted
