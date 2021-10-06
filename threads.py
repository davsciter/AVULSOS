import threading
import time

def Tarefa1():
    x = 0
    while(x<5):
        print("Tarefa 1")
        time.sleep(1)
        x+=1

def Tarefa2():
    y = 0
    while(y<5):
        print("Tarefa 2")
        time.sleep(1)
        y+=1

threading.Thread(target=Tarefa1).start()
Tarefa2()