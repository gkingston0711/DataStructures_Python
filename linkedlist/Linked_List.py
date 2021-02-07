from Node import *

class Linked_List:

    def __init__(self):
        self.head=None


    def insert(self,Name,Id):

        newNode=Node(Name,Id)

        if (self.head != None):
            current = self.head
            while (current.next!=None):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


    def ordered_insert(self,Name,Id):

        new_node=Node(Name,Id)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        elif self.head.name >= new_node.name:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head
            while current.next is not None and current.next.name < new_node.name:
                current = current.next

            new_node.next = current.next
            current.next = new_node


    def output_list(self):

        if self.head == None:
            print("empty list")

        current_node = self.head

        while current_node is not None:
            print("Name is -> "+current_node.name + " " +"Id # is -> "+ str(current_node.id))
            current_node = current_node.next
        return


    def output_justNames(self):
        if self.head==None:
            print("empty list")

        current_node=self.head

        while current_node is not None:
            print("Name is: "+current_node.name + " -> ")
            current_node = current_node.next


    def putInOrder(self):
        if self.head==None:
            print("this list is empty")

        newList = Linked_List()
        current=self.head

        while current != None:
            newList.ordered_insert(current.name,current.id)
            current=current.next

        return newList
