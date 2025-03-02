class Node():

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev
    
    def setPrev(self, prev):
        self.prev = prev

class DoublyLinkedList():

    def __init__(self):
        self.head = None

    # Insert element at head of list
    def insertNodeAtHead(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            currNode = self.head
            currNode.prev = new_node
            new_node.next = currNode
            self.head = new_node

    # Insert element at end of list
    def insertNodeAtEnd(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            
            currNode.next = new_node
            new_node.prev = currNode

    # Insert element at middle of list
    def insertNodeAtMiddle(self, target_node, new_node):
        if target_node.next is None:
            self.insertNodeAtEnd(new_node)
        else:
            new_node.next = target_node.next
            target_node.next.prev = new_node
            target_node.next = new_node
            new_node.prev = target_node

    # Return given element
    def searchNode(self, data):
        if not data:
            return print('No data available')
        else:
            currNode = self.head
            while currNode:
                if currNode.data == data:
                    return currNode
                currNode = currNode.next
            return print('Node not found')

    # Delete the head element
    def deleteHead(self):
        if not self.head:
            return print('No head in Linked List')
        else:
            currNode = self.head
            self.head = currNode.next
            self.head.prev = None
            currNode = None

    def deleteElement(self, target_node):
        
        if self.head is None:
            return print('No linked List')
        
        currNode = self.head
        
        if currNode.data == target_node.data:
            self.deleteHead()
            return
        
        previousNode = None
        while currNode and currNode.data != target_node.data:
            previousNode = currNode
            currNode = currNode.next
        
        if currNode is None:
            return print('Node not found')

        previousNode.next = currNode.next
        currNode.next.prev = previousNode
        currNode = None
            

    def print(self):
        currNode = self.head
        print('NULL <-> ', end='')
        while currNode:
            print(currNode.data, end=' <-> ')
            currNode = currNode.next
        print('NULL')

dll = DoublyLinkedList()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)


dll.insertNodeAtHead(one)
dll.insertNodeAtHead(two)
dll.insertNodeAtEnd(five)
dll.insertNodeAtEnd(four)
dll.insertNodeAtMiddle(five, three)


dll.print()
dll.deleteHead()
dll.print()