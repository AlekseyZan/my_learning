class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self,value):
        if self.head.value is  None:
            self.head.value = value
            return

        temp = Node()
        temp.value = value
        #1 variant
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = temp

        #2 variant
        #temp.next = self.head
        #self.head = temp
        self.size +=1

    def lenght(self): #Dlina spiska
        current_node = self.head
        if self.head.value is None:
            size = 0
        else:
            size = 1
        while current_node.next is not None:
            current_node = current_node.next
            size +=1
        return size

    def find_value(self,value): #funkzia poiska znacheniya
        if self.head.value is not None:
            if self.head.value == value:
                return True
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False

    def find_node(self,value):
        pass


    def print(self):
        if self.head.value is None:
            print("Empty Linked List")
            return
        print(self.head.value,end=" ")
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.value,end=" ")
            
        print()    

ll = LinkedList()
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(9)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(7)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(6)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(4)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(9)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
ll.add(19)
print(ll.lenght())
print(ll.find_value(0),ll.find_value(9),ll.find_value(6))
ll.print()
a = 10