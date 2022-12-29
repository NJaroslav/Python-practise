ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    The function checks if the command contains a word from the ignore list.

    command is a string. Command to check
    ignore is a list. Word list

    Returns
    * True if the command contains a word from the ignore list
    * False - if not
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    config_dict = {}
    with open(config_filename,'r') as f:
        for line in f:
            line = line.rstrip()
            if line and not line.startswith('!') or ignore_command(line,ignore):
                if line[0].isalnum():
                    block = line
                    config_dict[block] = []
                else:
                    config_dict[block].append(line.rstrip())
    return config_dict
