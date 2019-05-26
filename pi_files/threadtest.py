import threading
import time

i = 0

def test1():
    global i
    while True:
        time.sleep(1)
        print("worker", i)
        i += 1

threading.Thread(target=test1).start()

while True:
    print("main", i)
    time.sleep(0.3)
    i += 1
