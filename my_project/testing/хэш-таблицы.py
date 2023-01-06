class Node:
    def __init__(self):
        self.data = None
        self.next = None

class HashTable:
    def __init__(self,size):
      self.elems = []
      self.size = size
      for i in range(size):
        self.elems.append(Node())

    def hash(self,key):
        return key % self.size

    def add(self,value):
        hash = self.hash(value)
        if self.elems[hash].data is None:
            self.elems[hash].data = value
        else:
            current_node = self.elems[hash]
            while current_node.next is not None:
                current_node = current_node.next
            temp = Node()
            temp.data = value
            current_node.next = temp


    def delete(self,value):
        hash = self.hash(value)
        if self.elems[hash].data is None:
            raise Exception("Элеметов с таким хэшем нет")
        else:
            prev = None
            current_node = self.elems[hash]
            if current_node.data == value:
                self.elems[hash] = self.elems[hash].next
                return
            while current_node.next is not None:
                prev = current_node
                current_node = current_node.next
                if current_node.data == value:
                    prev.next = current_node.next
                    return
            raise Exception("Такого элемента нет в таблице")

    def find(self,value):
        pass





