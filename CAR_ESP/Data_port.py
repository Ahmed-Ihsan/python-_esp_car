import serial
import time

ser = None
ser_ = None

def set_com(com_R,com_w):
    global ser ,ser_
    print('connection with port ...')
    ser = serial.Serial(com_R, 115200, timeout=1)
    ser_ = serial.Serial(com_w, 115200, timeout=1)
    print(f'reading Data from port  ')
    
def set_data(data):
    global ser ,ser_
    # for i in range(50):
    ser_.write(bytes(data))
        # line = ser.readline()
        # if line:
        #     string = line.decode()
        #     num = int(string)
        #     print("Data is",end=': ')
        #     print(num)
    print("Done")
    ser.close()

# set_data(b'L','COM15','COM13')