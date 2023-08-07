import threading
import time

def name():
    for i in range(0,5):
        t1 = input("Enter Name : ")
        t2 = int(input("Enter Price : "))
        time.sleep(1) 
        print(t1)
        print(t2)
            

t1=threading.Thread(target=name,args=( ))

t1.start()
t1.join()



    
