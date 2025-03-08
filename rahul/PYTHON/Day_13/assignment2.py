class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        a = self.head
        while a is not None:
            print(a.data)
            a = a.next 
        
    def AtBeginning(self,data):
        nb = Node(data)
        nb.next = self.head 
        self.head = nb

    def AtEnd(self,data):
        ne = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = ne

    def InBetween(self,mn,data):
        nn = Node(data)
        nn.next = mn.next
        mn.next = nn

    def update(self,old_val,new_val):
        temp = self.head 
        while temp:
            if temp.data == old_val:
                temp.data = new_val
                return
            temp = temp.next
        print(f"Value {old_val} not found in list.")

list = Slinkedlist()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

list.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

list.printlist()
print("\n")

list.InBetween(n3,35)
list.printlist()
print("\n")

list.update(40,45)
list.printlist()
print("\n")

list.AtEnd(50)
list.printlist()