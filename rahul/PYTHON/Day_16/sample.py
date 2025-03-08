class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        nn = Node(data)
        if not self.head:
            self.head = nn
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = nn
    
    def Atbeginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def Inbetween(self,present_node,data):
        new_node = Node(data)
        new_node.next = present_node.next
        present_node.next = new_node

    def deleteNode(self,key):
        current = self.head
        if current and current.data == key:
            current.next = self.head
            current = None
            return 
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            print("No node is found")
            return
        prev.next = current.next
        current = None
        print("Node is deleted")

    def search(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("Node is found")
                return
            temp = temp.next
        print("Node not found")
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

LL = Linkedlist()

LL.append(10)
LL.append(20)
LL.display()