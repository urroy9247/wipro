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
        

list_1 = Slinkedlist()

n1 = Node("Sun")
n2 = Node("Mon")
n3 = Node("Tue")
n4 = Node("Wed")
n5 = Node("Thu")

list_1.head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

list_1.printlist()