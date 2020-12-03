from cprint import cprint

from funcs.log import decor_log
from funcs.plc_func import data_to_bytearray, connect_to_plc, step_cycle


@decor_log
def main():
    """main cycle of program"""
    try:
        plc = connect_to_plc("185.6.25.165", 0, 1)
        res = True
    except:
        res = False
    while res:
        res = step_cycle(plc)
    if not res:
        cprint.warn("reconnect to plc")
        main()

if __name__ == '__main__':
    main()


