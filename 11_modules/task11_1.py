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
            r_host, l_int, l_int_num, *other, r_int, r_int_num = dev_inf
            res[(main_id, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return res


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
