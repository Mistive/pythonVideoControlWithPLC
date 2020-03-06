import pyModbus
import vlctest
import serial
import time






ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.1)  # timeout 단위: s
modbus = pyModbus.pyModbus(ser)
str = ['./videos/01.mp4', './videos/02.mp4', './videos/03.mp4']
player=vlctest.Player()
modbus.writeSingleCoil(id=1, address=9, on=True)
flag = 0
while(True):
    playbutton = modbus.readCoilStatus(id=1, address=10, num=1)
    ret = modbus.readCoilStatus(id=1, address=0, num=3)
    print(ret, playbutton)

    if player.changePlaying() is True:
        if playbutton is 1:
            player.resume()
        else:
            player.pause()

    for i in range(0,3):
        if ret[i] is 1:
            # player.getstate()
            # if player.playable is 1:
            #
            #     player.stop()
            player.play(str[i])
            modbus.writeSingleCoil(id=1, address=9, on=True)
            modbus.writeSingleCoil(id=1, address=100 + i, on=True)
            time.sleep(0.1)
            modbus.writeSingleCoil(id=1, address=100 + i, on=False)

    time.sleep(0.1)