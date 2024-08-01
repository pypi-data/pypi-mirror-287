import argparse
import sys
import logging
import pkg_resources

from datamanwithvan.config import config
from datamanwithvan.dmwvutils import messages
from datamanwithvan.job import replicationjob

# Section 6 : Obtain the current version number
package_name = "datamanwithvan"
version = pkg_resources.get_distribution(package_name).version
# End of Section 6

# Section 17 : Create an instance of the DatamanwithvanMessages class
DatamanwithvanMessagesObj = messages.DatamanwithvanMessages(version)
print(DatamanwithvanMessagesObj.msg_info_welcome)
print(DatamanwithvanMessagesObj.msg_info_welcome_footer)
# End of Section 17

# Section 4 : Before anything else, set up the logger...
logger = logging.getLogger('datamanwithvan')
console_handler = logging.StreamHandler()
console_format = logging.Formatter('%(name)s : %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)
# End of Section 4


def _handle_cmd_args():
    # Initialize ArgumentParser with description
    parser = argparse.ArgumentParser(
        description="A tool for managing and executing data jobs."
    )

    # Add general arguments
    parser.add_argument(
        "-c", "--config", type=str, default=None,
        help="Full path to a config file"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable verbose mode"
    )
    parser.add_argument(
        "-i", "--info", action="store_true",
        help="Print help message and exit"
    )

    # Add subparsers for subcommands
    subparsers = parser.add_subparsers(
        dest="subcommand", help='Subcommands', required=False
    )

    # Subcommand: job
    parser_job = subparsers.add_parser(
        'job', help='Commands related to job execution'
    )
    parser_job.add_argument(
        '--run', type=int, help='Run a job with the specified job ID'
    )

    # Parse the arguments
    args = parser.parse_args()

    return args


def datamanwithvan_entry():
    # Section 5 : As soon as main starts, pick up
    # any command line arguments...
    args = _handle_cmd_args()
    # End of Section 5

    # Section 7 : Print out help message
    if args.info:
        print(DatamanwithvanMessagesObj.msg_info_help_message)
        sys.exit(0)
    else:
        # No need to do anything here
        pass
    # End of Section 7

    # Section 1 : Determine verbosity based on parameter passing
    if args.verbose:
        console_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
    # End of Section 1

    # Section 2 : Load configuration from a config file,
    # if it's been passed, or by default config options
    datamanwithvanConfigObj = config.datamanwithvanConfig(args.config, logger)
    if datamanwithvanConfigObj.status > 0:
        logger.error(DatamanwithvanMessagesObj.msg_error_no_conf)
        sys.exit(1)
    # From this point on, refer to Datamanwithvan configuration
    # set as "datamanwithvanConfigObj.DatamanwithvanConf"
    # End of Section 2

    # Section 8 : Capture a replication job ID to execute, if there's one...
    if args.subcommand:
        if args.run is not None and args.subcommand == "job":
            ReplicationJobObj = replicationjob.ReplicationJob(
                args.run,
                datamanwithvanConfigObj.DatamanwithvanConf,
                DatamanwithvanMessagesObj,
                logger)
            ReplicationJobObj.runjob(args.run)
        else:
            pass
    # End of Section 8


if __name__ == "__main__":
    datamanwithvan_entry()
