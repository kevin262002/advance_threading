import threading

def even():
    print("Even Numbers")
    for i in range(0, 10, 2):
        print(i, end = " ")

def odd():
    print("\nOdd Numbers")
    for i in range(1, 10, 2):
        print(i, end = " ")

t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)

t1.start()
t2.start()

t1.join()
t2.join()
