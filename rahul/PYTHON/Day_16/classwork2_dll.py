class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the doubly linked list with an empty list

    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        
        last.next = new_node  # Make the last node point to the new node
        new_node.prev = last  # Make the new node's prev pointer point to the last node

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node  # Update the current head's prev pointer
        new_node.next = self.head  # New node points to the current head
        self.head = new_node  # Update the head to the new node

    def insert_after_node(self, prev_node, data):
        """Insert a new node after a given node"""
        if not prev_node:
            print("Previous node is not in the list.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next  # Make new node's next point to prev_node's next
        if prev_node.next:
            prev_node.next.prev = new_node  # If there is a next node, make its prev point to new node
        prev_node.next = new_node  # Make prev_node's next pointer point to new node
        new_node.prev = prev_node  # Make the new node's prev pointer point to prev_node

    def display_forward(self):
        """Display the list from head to tail (forward traversal)"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display the list from tail to head (backward traversal)"""
        current = self.head
        if not current:
            return
        
        # Move to the last node
        while current.next:
            current = current.next
        
        # Traverse backward using the prev pointer
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def delete(self, key):
        """Delete the first occurrence of a node with the given data"""
        current = self.head

        # If the list is empty
        if not current:
            print("List is empty.")
            return
        
        # Case 1: Deleting the head node
        if current.data == key:
            self.head = current.next  # Move head to the next node
            if self.head:
                self.head.prev = None  # Set the prev pointer of the new head to None
            current = None
            return

        # Case 2: Delete a node somewhere in the middle or end
        while current:
            if current.data == key:
                if current.next:  # If it's not the last node
                    current.next.prev = current.prev  # Adjust the next node's prev pointer
                if current.prev:  # If it's not the first node
                    current.prev.next = current.next  # Adjust the previous node's next pointer
                current = None
                return
            current = current.next

        print(f"Node with data {key} not found.")

# Example Usage:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Forward Traversal:")
dll.display_forward()

print("\nBackward Traversal:")
dll.display_backward()

# Deleting a node
dll.delete(30)
print("\nAfter deleting 30 (Forward Traversal):")
dll.display_forward()

dll.delete(10)  # Deleting the head
print("\nAfter deleting 10 (Forward Traversal):")
dll.display_forward()

dll.delete(50)  # Trying to delete a non-existing node