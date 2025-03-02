# Linked Lists 

class Node():
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
    
'''
newNode = Node(10)
newNode.setNext(Node(20))
print(newNode.getNext().data)
'''

class LinkedList():

    def __init__(self):
        self.head = None

    # Insert element at head of list
    def insertNodeAtHead(self, new_node):
        # If LinkedList is Empty
        if self.head is None:
            self.head = new_node
        # If LinkedList is not Empty
        else:
            new_node.next = self.head
            self.head = new_node
    
    # Insert element at end of list
    def insertNodeAtEnd(self, new_node):
        currNode = self.head
        # While nextNode is not Null
        while currNode.next:
            currNode = currNode.next
        currNode.next = new_node

    # Insert element at middle of list
    def insertNodeAtMiddle(self, target_node, new_node):
        if target_node.next is None:
            return print('Insert at End')
        else:
            new_node.next = target_node.next
            target_node.next = new_node

    # Return given element
    def searchNode(self, data):
        if not data:
            return print('No data available')
        
        currentNode = self.head
        while currentNode:
            if currentNode.data == data:
                return currentNode
            currentNode = currentNode.next
        return print('Node not found')

    # Delete the head element
    def deleteHead(self):
        if not self.head:
            return print('No head in Linked List')
        
        currNode = self.head
        self.head = currNode.next
        currNode = None
    
    # Delete given element
    def deleteElement(self, target_node):
        currNode = self.head

        # If the element to be deleted is the head, call the delete head func
        if currNode.data == target_node.data:
            self.deleteHead()
        
        previousNode = None

        # If the currNode is not None and the data is not the target data
        while currNode and (currNode.data != target_node.data):
            previousNode = currNode
            currNode = currNode.next
        
        # If we reach the end of the list and the element is not found
        if currNode is None:
            return print('Element not found')
        
        # Update the previous node next
        previousNode.next = currNode.next
        currNode = None

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(f'{currentNode.data} -> ', end='')
            currentNode = currentNode.next 
        print('NULL')


ll = LinkedList()
ll.deleteHead()
ten = Node(10)
twenty = Node(20)
thirty = Node(30)
six = Node(6)
ll.insertNodeAtHead(ten)
ll.insertNodeAtHead(twenty)
ll.insertNodeAtHead(thirty)
# ll.insertNodeAtMiddle(twenty, six)

target = ll.searchNode(20)

ll.printLinkedList()

ll.deleteElement(twenty)
ll.printLinkedList()


# Insert element at head of list

# Insert element at end of list

# Insert element at middle of list

# Delete given element

# Delete the first element

# Return given element