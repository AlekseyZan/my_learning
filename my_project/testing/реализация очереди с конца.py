from time import sleep
class Queue:
    def __init__(self):
        self.elems = list()

    def add(self,value): #добавление элемента в очередь
        self.elems.insert(0, value)

    def get(self):  #изъятие элемента
       val = self.elems.pop()
       return val

    def size(self):  #размер очереди
        size = len(self.elems)
        return size

queue = Queue()
for i in range(9,-1,-1):
    queue.add(i)
    print(i,end=" '")
print()

for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)
