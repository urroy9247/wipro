class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Insert a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node after a given node
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("The previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete the first occurrence of a node with the given data
    def delete(self, data):
        current = self.head
        if current and current.data == data:  # If the node to be deleted is the head
            self.head = current.next
            current = None
            return
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                current = None
                return
            prev = current
            current = current.next
        print(f"Node with data {data} not found.")
    
    # Traverse and print the list
    def traverse(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

    # Search for a node by value
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Driver code
ll = LinkedList()

# Appending nodes
ll.append(10)
ll.append(20)
ll.append(30)

# Prepending nodes
ll.prepend(5)

# Inserting after a given node
ll.insert_after(ll.head.next, 15)

# Traversing the list
print("Traverse the list:")
ll.traverse()

# Searching for a value
print(f"Search for 20: {'Found' if ll.search(20) else 'Not Found'}")
print(f"Search for 100: {'Found' if ll.search(100) else 'Not Found'}")

# Deleting nodes
ll.delete(20)
print("List after deleting 20:")
ll.traverse()

ll.delete(5)  # Deleting head node
print("List after deleting 5 (head):")
ll.traverse()

ll.delete(100)  # Deleting a non-existing node