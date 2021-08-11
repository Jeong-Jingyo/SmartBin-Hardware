import serial
import configparser
import pathlib

cfg = configparser.ConfigParser()
cfg.read(str(pathlib.Path(__file__).parent.resolve()) + "/serial.cfg")
print(cfg)
port = cfg["config"]["port"]
baud_rate = cfg["config"]["baud_rate"]

try:
    ser = serial.Serial(port=port)
except serial.SerialException as ex:
    print(ex)


def door(open_door: bool):
    print(open_door)
    if open_door:
        ser.write(b"1")
    else:
        ser.write(b"2")


def home(): ser.write(b"2b")


def pet(): ser.write(b"1a")


def pet_re(): ser.write(b"1c")


def plastic(): ser.write(b"3a")


def plastic_(): ser.write(b"3b")


def can(): ser.write(b"4a")


def glass(): ser.write(b"4c")


def vinyl(): ser.write(b"5a")


def general(): ser.write(b"5c")
