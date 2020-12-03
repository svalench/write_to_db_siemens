import struct

import cprint

from funcs.log import decor_raise, decor_log
from siemens.module_siemens import PlcRemoteUse


@decor_raise
def connect_to_plc(address, rack, slot, port=102) -> PlcRemoteUse:
    """connect to remote plc"""
    plc = PlcRemoteUse(address=address, rack=rack, slot=slot, port=port)
    print(plc)
    return plc


def get_data() ->list:
    """read data from anyware"""
    return [0.0,2.3,3.2,6.3,51.2,3.2,53.2,312.321,5.23,23234.234]


@decor_raise
def data_to_bytearray(data:list) -> bytearray:
    """data to bytearray"""
    data.reverse()
    res = bytearray()
    for i in data:
        if type(i).__name__ == "int":
            if(i<-32767 or i>32767):
                raise ValueError("int must be format requires -32767 <= number <= 32767")
            res+=(struct.pack("h", i))
        elif(type(i).__name__=='float'):
            res+=(struct.pack("f",i))
        else:
            raise ValueError("Value in list must be an int or float")
    cprint.cprint.info(f"length of bytearray {len(res)}")
    res.reverse()
    return res


@decor_raise
def write_data_to_plc(plc:PlcRemoteUse, db:int, offset:int, data:bytearray):
    """function for write data to plc"""
    res = False
    if plc.write_to_db_bytearray(db=db, offset=offset, data=data):
        res = True
    return res


@decor_raise
def step_cycle(plc) -> bool:
    """main cycle for read data, transform to byte and write to plc"""
    data = get_data()
    bytes = data_to_bytearray(data)
    return write_data_to_plc(plc=plc, db=3, offset=0, data=bytes)