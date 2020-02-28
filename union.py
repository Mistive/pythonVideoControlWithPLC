import pyModbus
import vlctest
import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.1)  # timeout 단위: s
modbus = pyModbus.pyModbus(ser)


p=vlctest.Player()
flag = 0
while(True):
    ret = modbus.readCoilStatus(id=1, address=0, num=3)
    print(flag is 0 and ret[0] is 1)

    if ret[0] is 1 and flag is 0:
        flag = 1
        p.stop()
        p.play('./videos/01.mp4')
    elif ret[1] is 1 and flag is 0:
        flag = 1
        p.stop()
        p.play('./videos/02.mp4')
    elif ret[2] is 1 and flag is 0:
        flag = 1
        p.stop()
        p.play('./videos/03.mp4')
    elif ret == [0,0,0]:
        flag = 0

    print(ret, flag)
    time.sleep(0.2)