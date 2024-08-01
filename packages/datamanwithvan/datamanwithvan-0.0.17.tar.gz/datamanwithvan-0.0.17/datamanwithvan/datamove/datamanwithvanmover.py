import dask
from dask import delayed
import dask.threaded
from datamanwithvan.dmwvutils import messages
import logging

logger = logging.getLogger('datamanwithvanmover')
console_handler = logging.StreamHandler()
console_format = logging.Formatter('%(name)s : %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)


class DatamanwithvanMover:
    replication_rules = None
    configuration = None
    content = None
    logger = None

    def __init__(self, replication_rules, configuration, content, logger):
        self.replication_rules = replication_rules
        self.configuration = configuration
        self.content = content
        self.logger = logger

    def _origin_to_agent(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _agent_to_agent(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _agent_to_target(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _agent_to_origin(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _agent_from_agent(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _agent_from_origin(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _checkin_replication_task(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _checkout_replication_task(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _transfer_data(self, replication_rule):
        status = messages.DatamanwithvanMessages.msg_warn_not_implemented

        self._checkin_replication_task()

        if replication_rule[8] == "push":
            self._origin_to_agent()

            self._agent_to_agent()

            self._agent_to_target()

        if replication_rule[8] == "pull":
            self._agent_from_origin()

            self._agent_from_agent()

            self._agent_to_origin()

        self._checkout_replication_task()

        return status

    def _get_data_deltas(self):
        return messages.DatamanwithvanMessages.msg_warn_not_implemented

    def _initiate_replication_tasks(self, replication_rule):
        logger.debug(replication_rule)

        self._get_data_deltas()

        self._transfer_data(replication_rule)

    def start_replication_tasks(self):
        results = dask.compute(*self.tasks, scheduler='threads')

        logger.debug(results)

        return results

    def assign_replication_rules(self):
        """
        For every replication rule in the job, make a separate thread
        to handle it
        """
        status = None
        try:
            num_tasks = len(self.replication_rules[1].fetchall())
            self.tasks = [delayed(self._initiate_replication_tasks)(
                self.replication_rules[1][i]) for i in range(0, num_tasks - 1)]
            status = 35
        except Exception as e:
            logger.error(f" failed to make replication tasks: {e}")
            status = 36

        return status
