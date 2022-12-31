from tabulate import tabulate

def print_ip_table(reachable, unreachable):
    table = {'Reachable' : reachable, 'Unreachable' : unreachable}
    print(tabulate(table, headers = 'keys'))
