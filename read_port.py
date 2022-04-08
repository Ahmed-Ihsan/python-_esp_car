import serial
import time

print('connection with port ...')
ser = serial.Serial('COM10', 115200, timeout=1)
ser_ = serial.Serial('COM11', 115200, timeout=1)
print(f'reading Data from port  ')

while 1:
    for i in range(50):
            ser_.write(bytes(b'n'))
            line = ser.readline()# read a byte
            if line:
                string = line.decode()  # convert the byte string to a unicode string
                num = int(string) # convert the unicode string to an int
                print("Data is",end=': ')
                print(num)
            
ser.close()