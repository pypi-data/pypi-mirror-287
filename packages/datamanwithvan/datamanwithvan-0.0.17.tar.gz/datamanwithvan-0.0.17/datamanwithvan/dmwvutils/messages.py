class DatamanwithvanMessages:

    msg_info_version_number = None
    msg_info_welcome = r"""
    ___      _                          __    __ _ _   _                   __
   /   \__ _| |_ __ _  /\/\   __ _ _ __/ / /\ \ (_| |_| |____   ____ _  /\ \ \
  / /\ / _` | __/ _` |/    \ / _` | '_ \ \/  \/ | | __| '_ \ \ / / _` |/  \/ /
 / /_/| (_| | || (_| / /\/\ | (_| | | | \  /\  /| | |_| | | \ V | (_| / /\  /
/___,' \__,_|\__\__,_\/    \/\__,_|_| |_|\/  \/ |_|\__|_| |_|\_/ \__,_\_\ \/
"""
    msg_info_welcome_footer = "Welcome to Datamanwithvan client!"
    msg_error_cant_fetch_rep_rule = "Unable to fetch replication rules"
    msg_warn_no_rep_rule = "This job has no active rules to run"
    msg_info_repl_rule_exist = "All good, rest not implemented yet"
    msg_warn_not_implemented = "Not implemented yet"
    msg_error_no_conf = "Unable to find a usable configuration. Exiting now.."
    msg_info_help_message = """
Main help message coming soon...
"""

    def __init__(self, version):
        self.msg_info_version_number = version
