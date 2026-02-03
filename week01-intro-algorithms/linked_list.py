
class ListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 

    def add_node(self, value):
        temp = ListNode(value)
        temp.next = self.head
        self.head = temp

    def remove_node(self, value):
        prev = None 
        iter = self.head
        while iter is not None:
            if iter.data == value:
                if prev is None:    # This is the first node
                    self.head = iter.next 
                else:
                    prev.next = iter.next
                break
            prev = iter
            iter = iter.next


    def search(self, value):
        iter = self.head
        while iter is not None:
            if iter.data == value:
                return iter 
            iter = iter.next 
        return None

    def is_empty(self):
        return self.head is None

    def display(self):
        iter = self.head
        while iter is not None:
            print(iter.data)
            iter = iter.next


list = LinkedList()
list.add_node(10)
list.add_node(5)
list.add_node(12)
list.add_node(4)
list.add_node(57)
list.add_node(6)
list.display()

node = list.search(67)
if node is None:
    print("Not found")


node = list.search(12)
if node is not None:
    print(node.data)

list.remove_node(12)
list.remove_node(6)
print("Deleted 12 and 6")
list.display()