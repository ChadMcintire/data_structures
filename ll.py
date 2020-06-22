from create_node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, name, value):
        #if new list
        newNode = Node(name, value)
        if not self.head:
            self.head = newNode
        else:
            #save head's current position
            temp = self.head
            #move head's position until you find a None value for
            #nextNode
            while(temp.next):
                temp = temp.next

            #set the none value to the new node
            temp.next = newNode
