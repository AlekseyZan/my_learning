class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = Node()

    def insert_to_end(self,value):  #Vstavit element v konec spiska
        if self.head.value is None:
            self.head.value = value
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        temp = Node()
        temp.value = value
        temp.prev = current_node
        current_node.next = temp




    def insert_to_start(self,value):  #Vstavit element v nachalo spiska
        if self.head.value is None:
            self.head.value = value
            return
        temp = Node()
        temp.value = value
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_after_value(self,after_value,value_to_insert):  #Vstavit posle znacheniya
        if self.head.value is None:
            raise Exception("Empty list")
        if self.head.value == after_value:
            temp = Node()
            temp.value = value_to_insert
            temp.next = self.head.next
            temp.prev = self.head
            self.head.next.prev = temp
            self.head.next = temp
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == after_value:
                break
            current_node = current_node.next
        if current_node.next is None:
            if current_node.value != after_value:
                raise Exception("No such element")

        temp = Node()
        temp.value = value_to_insert
        temp.next = current_node.next
        temp.prev = current_node
        current_node.next.prev = temp
        current_node.next = temp

    def delete_from_end(self):
        if self.head.value is None:
            raise Exception("Empty list")
        if self.head.next is None:
            val = self.head.value
            self.head = Node()
            return val
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        val = current_node.value
        current_node.prev.next = None
        return val


    def delete_from_start(self):
        if self.head.value is None:
            raise Exception("Empty list")
        if self.head.next is None:
            self.head = Node()
            val = self.head.value
            return  val
        self.head.next.prev = None
        val = self.head.value
        self.head = self.head.next
        return val

        
dll = DoubleLinkedList()
dll.insert_to_start(9)
dll.insert_to_end(7)
dll.insert_to_start(6)
dll.insert_after_value(9, 8)
a = 10
print(dll.delete_from_end())
print(dll.delete_from_start())