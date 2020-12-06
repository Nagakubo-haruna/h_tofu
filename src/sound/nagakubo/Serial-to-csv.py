import serial
import numpy as np

ser = serial.Serial("COM3",9600)
ser.close()
ser.open()

listdata=[]


def main():
    while True:
        count = 0
        # data = ser.readline()
        # print(data)
        while count < 2:
            data = ser.readline()
            listdata.append(int(data))
            print (listdata)
            count += 1

try:
    main()

except KeyboardInterrupt:
    np.savetxt('data.txt',listdata)
