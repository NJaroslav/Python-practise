def parse_cdp_neighbors(command_output):
    """
    Here we pass the output of the command as single string because it is in this
    form that received command output from equipment. Taking the output of
    the command as an argument, instead of a filename, we make the function more
    generic: it can work both with files and with output from equipment.
    Plus, we learn to work with such a output.
    """
    res = {}
    for line in command_output.split('\n'):
        if '>' in line:
            main_id = line.split('>')[0]
        dev_inf = line.split()
        if len(dev_inf) >= 4 and dev_inf[3].isdigit():
            res[(main_id, dev_inf[1] +  dev_inf[2])] = (dev_inf[0], dev_inf[8]+ dev_inf[9])
    return res


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
