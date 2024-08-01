import urllib

from sqlalchemy import create_engine, text
from datamanwithvan.dmwvutils import messages
from datamanwithvan.datamove import datamanwithvanmover


class ReplicationJob:

    replication_job_id = None
    configuration = None
    content = None
    logger = None
    query_engine = None

    def _checkin_replication_job(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _checkout_replication_job(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    # TODO: Uncomment and implement this method
    def __getQueryEngineMySQL(configuration):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    # TODO: Implement this method
    def __getQueryEnginePostgresSQL(configuration):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def __getQueryEngineAzureSQL(self, configuration):
        server = configuration.backenddatabase.server
        database = configuration.backenddatabase.database
        uid = configuration.backenddatabase.uid
        pwd = configuration.backenddatabase.pwd

        # credential = DefaultAzureCredential()
        # token = credential.get_token(
        # "https://database.windows.net/.default").token

        # Construct connection string
        connection_string = (
            f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={server};"
            f"Database={database};"
            f"Uid={uid};"
            f"Pwd={pwd};"
            f"Encrypt=yes;"                # Ensure encryption
            f"TrustServerCertificate=no;"
        )

        # Encode the connection string for SQLAlchemy
        params = urllib.parse.quote_plus(connection_string)
        engine_url = f"mssql+pyodbc:///?odbc_connect={params}"

        # Create SQLAlchemy engine
        engine = create_engine(engine_url)

        return engine

    def _getQueryEngine(self, configuration):
        """
        Returns an SQLAlchemy's QueryEngine Object.

        Parameters:
        - configuration (datamanwithvanConfig): The object containing
        Datamanwithvan's master configuration

        Returns:
        - Engine: A class `_engine.Engine` instance.
        """
        if configuration.backenddatabase.dbtype == "azuresql":
            return self.__getQueryEngineAzureSQL(configuration)

        if configuration.backenddatabase.dbtype == "postgresql":
            return self.__getQueryEnginePostgresSQL(configuration)

        if configuration.backenddatabase.dbtype == "mysql":
            return self.__getQueryEngineMySQL(configuration)

    def __init__(self, replication_job_id,
                 configuration, content, logger):
        self.replication_job_id = replication_job_id
        self.configuration = configuration
        self.content = content
        self.logger = logger
        self.query_engine = self._getQueryEngine(configuration)

    def _getReplicationRules(self, replication_job_id, query_engine):
        result = []
        status = 0
        rules = []

        try:
            with query_engine.connect() as connection:
                sch = self.configuration.backenddatabase.schema
                tbl = self.configuration.backenddatabase.repl_rules_table
                query = f"""SELECT *
                from {sch}.{tbl}
                where id={replication_job_id} and enabled=1"""

                rules = connection.execute(text(query))

                if len(rules.fetchall()) == 0:
                    status = 1
                else:
                    status = 0

        except Exception as e:
            self.logger.error(f"Could not fetch replication rules"
                              f"for Job ({replication_job_id}) : {e}")
            status = 2

        result = [status, rules]

        return result

    def runjob(self, replication_job_id):
        self.logger.info(f"runjob: {replication_job_id}")

        # runjob step 1: Get Replication Rules
        self._checkin_replication_job()
        # end of runjob step 1

        # runjob step 2: Get Replication Rules
        replication_rules = self._getReplicationRules(
            replication_job_id, self.query_engine)
        self.logger.info(replication_rules)
        # end of runjob step 2

        # runjob step 3: Validate the Replication Rules
        if replication_rules[0] == 0:
            self.logger.info(
                messages.DatamanwithvanMessages.msg_info_repl_rule_exist)
        if replication_rules[0] == 1:
            self.logger.warning(
                messages.DatamanwithvanMessages.msg_warn_no_rep_rule)
            return replication_rules[0]
        if replication_rules[0] == 2:
            mg = messages.DatamanwithvanMessages.msg_error_cant_fetch_rep_rule
            self.logger.error(mg)
            return replication_rules[0]
        # end of runjob step 3

        # runjob step 4: What's next?
        # TODO: we create a DatamanwithvanMover
        # object that will do the heavy work
        DatamanwithvanMoverObj = datamanwithvanmover.DatamanwithvanMover(
            replication_rules, self.configuration, self.content, self.logger)
        result_assign_rules = DatamanwithvanMoverObj.assign_replication_rules()
        self.logger.info(result_assign_rules)

        result_start_tasks = DatamanwithvanMoverObj.start_replication_tasks()
        self.logger.info(result_start_tasks)
        self.logger.debug(DatamanwithvanMoverObj)
        # end of runjob step 4

        # runjob step 5: What's next?
        self._checkout_replication_job()
        # end of runjob step 5

    def dummy(self):
        pass
