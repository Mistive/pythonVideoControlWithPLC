from pyModbus import pyModbus
import serial
import time



def main():
    ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.1)  # timeout 단위: s
    modbus = pyModbus(ser)
    cnt = 0
    print("Start")

    while (True):
        L1 = modbus.readCoilStatus(1, 1, 4)
        L1Q = modbus.readInputRegisters(1, 1, 5)
        modbus.writeSingleRegister(1,1,cnt)
        modbus.writeSingleRegister(1, 2, cnt+cnt)
        modbus.writeSingleRegister(1, 3, cnt+cnt+cnt)
        modbus.writeSingleRegister(1, 4, cnt+cnt+cnt+cnt)
        modbus.writeSingleRegister(1, 5, cnt+cnt+cnt+cnt+cnt)

        print('L1: ', L1)
        print('L1Q:', L1Q)
        cnt = cnt+1
        time.sleep(1)

if __name__ == '__main__':
    main()