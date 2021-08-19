import serial
import configparser
import pathlib

cfg = configparser.ConfigParser()
cfg.read(str(pathlib.Path(__file__).parent.resolve()) + "/serial.cfg")
port = cfg["config"]["port"]
baud_rate = cfg["config"]["baud_rate"]

try:
    ser = serial.Serial(port=port)
except serial.SerialException as ex:
    print(ex)


def door(open_door: bool):
    pass
    # print(open_door)
    # if open_door:
    #     ser.write(b"1")
    # else:
    #     ser.write(b"2")


def door_closed() -> bool:
    return False


def home(): ser.write(b"2b")


def bin1(): ser.write(b"1a")


def bin2(): ser.write(b"1c")


def bin3(): ser.write(b"3a")


def bin4(): ser.write(b"3b")


def bin5(): ser.write(b"4a")


def bin6(): ser.write(b"4c")


def bin7(): ser.write(b"5a")


def bin8(): ser.write(b"5c")
