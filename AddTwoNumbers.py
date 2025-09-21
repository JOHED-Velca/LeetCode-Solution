class Node:
    def __init__(self, data): # Constructor to initialize the node
        self.data = data # Value of the node
        self.next = None # Pointer to the next node
        
    def _repr_(self): # String representation of the node
        return self.data # Return the data of the node

class LinkedList: # Define a linked list class
    def __init__(self): # Constructor to initialize the linked list
        self.head = None # Initialize the head of the linked list
    
    def append(self, data): # Method to append a new node to the linked list
        new_node = Node(data) # Create a new node with the given data
        if self.head is None: # If the linked list is empty
            self.head = new_node # Set the new node as the head and 
            return 
        current = self.head # Start from the head node
        while current.next: # Traverse to the end of the linked list
            current = current.next # Move to the next node
        current.next = new_node # Append the new node at the end of the linked list
        
    def printList(self): # Method to print the linked list
        current = self.head # Start from the head node
        while current: # Traverse the linked list
            print(current.data) # Print the data of the current node
            current = current.next # Move to the next node
        # print("None") # Indicate the end of the list
    
    def __repr__(self): # String representation of the linked list
        node = self.head # Start from the head node
        nodes = [] # List to store the string representation of nodes
        while node is not None: # Traverse the linked list
            nodes.append(str(node.data)) # Append the data of the current node to the list
            node = node.next # Move to the next node
        nodes.append("None") # Append "None" to indicate the end of the list
        return " -> ".join(nodes) # Join the node data with " -> " and return as a string
            
def findLowestValue(head):
    minValue = head.data # Initialize minValue with the head node's data
    currentNode = head.next # Start from the next node
    while currentNode: # Traverse the linked list
        if currentNode.data < minValue: # If current node's data is less than minValue
            minValue = currentNode.data # Update minValue
        currentNode = currentNode.next # Move to the next node
    return minValue # Return the lowest value found

list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(3)

# Method 1: Using the printList() method
print("Using printList() method:")
list1.printList()

# Method 2: Using the __repr__ method
print("Using print(list1):")
print(list1)

