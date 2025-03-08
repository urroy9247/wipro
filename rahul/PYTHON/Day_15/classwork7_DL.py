class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            pass
        
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def search(self,value):
        temp = self.head
        found = False
        while temp is not None:
            if temp.data == value:
                found = True
                break
            temp = temp.next
        return found
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
dll = DLinkedlist()
dll.addNode(10)
if dll.isEmpty():
    print("Double Linked List is Empty")
else:
    print("Double Linked List is not Empty")