# config/config.py
# Keeping it here for reference purposes, since we're using
# Dynaconf to load the configuration inside the main script.
import os

from dynaconf import Dynaconf


class datamanwithvanConfig:

    DatamanwithvanConf = None
    path_to_config = None
    logger = None
    status = 0

    def _loadConfig(self, args_config, logger):
        if args_config:
            logger.info("Loading Datamanwithvan configuration"
                        f"from {args_config}")

            if os.access(args_config, os.R_OK):
                # TODO: Read the config file, load it...
                try:
                    self.DatamanwithvanConf = Dynaconf(
                        settings_files=[args_config],
                        environments=False
                    )
                    self.status = 0
                    settings_dict = self.DatamanwithvanConf.to_dict()
                    logger.debug(settings_dict)
                except Exception as configFileNotFound:
                    logger.error(f"Can't load {args_config}:"
                                 f"{configFileNotFound}")
                    self.status = 3
            else:
                logger.error(f"Can't load {args_config}: "
                             "File does not exist")
                self.status = 2
        else:
            logger.error("No Datamanwithvan config file was specified"
                         ",default values and runtime config"
                         " parameters are not supported yet..")
            self.status = 1

        return self.status

    def __init__(self, args_config, logger):
        # TODO: Do we need sanitization here for args_config?
        self.path_to_config = args_config
        self.logger = logger
        self.status = self._loadConfig(args_config, logger)
