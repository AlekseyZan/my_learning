from time import sleep
class Queue:
    def __init__(self):
        self.elems = list()

    def add(self,value): #добавление элемента в очередь
        self.elems.append(value)

    def get(self):  #изъятие элемента
        return self.elems.pop(0)

    def size(self):  #размер очереди
        size = len(self.elems)
        return size

queue = Queue()
for i in range(10):
    queue.add(i)
    print(i,end=" '")
print()

for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)
