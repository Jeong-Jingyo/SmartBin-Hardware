import serial
import configparser
import pathlib
from threading import Thread

cfg = configparser.ConfigParser()
cfg.read(str(pathlib.Path(__file__).parent.resolve()) + "/serial.cfg")
port = cfg["config"]["port"]
baud_rate = cfg["config"]["baud_rate"]


class Serial:
    working = None
    latest_bin_allocation_ratio = None
    ser = None

    def __init__(self):
        try:
            self.ser = serial.Serial(port="COM4")
            ser_thr = Thread(target=self.get_stat)
            ser_thr.start()
        except serial.SerialException as ex:
            print(ex)
            
    def get_stat(self):
        while True:
            stat = self.ser.read()
            try:
                int(stat)
                self.latest_bin_allocation_ratio = int(stat)
            except ValueError:
                if stat == "i":
                    self.working = False
                elif stat == "w":
                    self.working = True

    def open_door(self):
        return True
        self.ser.write(b"s")

    def door_closed(self) -> bool:
        return True

    def get_latest_bin_allocation_ratio(self):
        return self.latest_bin_allocation_ratio

    def home(self):
        self.ser.write(b"2b")

    def bin1(self):
        self.ser.write(b"1a")

    def bin2(self):
        self.ser.write(b"1c")

    def bin3(self):
        self.ser.write(b"3a")

    def bin4(self):
        self.ser.write(b"3b")

    def bin5(self):
        self.ser.write(b"4a")

    def bin6(self):
        self.ser.write(b"4c")

    def bin7(self):
        self.ser.write(b"5a")

    def bin8(self):
        self.ser.write(b"5c")
