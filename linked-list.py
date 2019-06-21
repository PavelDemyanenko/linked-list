# program to implement Linked List

class LinkedList:
    def __init__(self):
        self.head = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):
        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data feild of Node
    def updateData(self, data):
        self.data = data

    # method to set Link feild the Node
    def setLink(self, node):
        self.link = node

    # method returns data feild of the Node
    def getData(self):
        return self.data

    # method returns address of the next Node
    def getNextNode(self):
        return self.link


# main method

# creating LinkedList
myList = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(1)
myList.addToStart(4)
myList.addToStart(8)
myList.addToStart(12)
myList.addToEnd(16)

myList.display()

# pushing an element
myList.push(20)

myList.display()

print("Max in list", myList.Max())
print("Min in list", myList.Min())

# removing an element
myList.remove(12)
myList.remove(myList.Max())
myList.remove(myList.Min())

myList.display()
