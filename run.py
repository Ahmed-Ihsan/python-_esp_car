import move_obj
import threading
import time
from CAR_ESP import scan_serial_port ,Data_port ,M5cam

# Data_port.Data_port()
# M5cam.download_frame(6)

resl = scan_serial_port.serial_ports()
print(f"port is : {resl}")
if(len(resl) == 2):
     com_R = resl[1]
     com_w = resl[0]
else:
     com_R = input("write port name for read data >> ")
     com_w = input("write port name for send data >> ")
     
Data_port.set_com(com_R,com_w)
for i in range(3):
     print(i)
     time.sleep(1)
     
new = dict()
for i in range(20):
     new[f'{i}']=threading.Thread(target=move_obj.main, args=(f'window number{i}',)) 
# else:
#      camM5 =threading.Thread(target=M5cam.download_frame, args=(1,)) 
#      camM5.start()

for i in new: 
     new[i].start()
     new[i].join()