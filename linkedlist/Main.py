from Linked_List import *
from Node import *
from CSV import *



def main():


    print("linkedlist below...\n")

    myList = Linked_List()
    myList.insert("brad",11)
    myList.insert("anne",2)
    myList.insert("jay",7)
    myList.insert("zira",9)
    myList.insert("amy",11)
    myList.insert("zach",14)
    #myList.output_list()


    orderedList = Linked_List()
    orderedList.ordered_insert("brett",20)
    orderedList.ordered_insert("anna",17)
    orderedList.ordered_insert("zayne",9)
    orderedList.ordered_insert("cliff",16)
    orderedList.ordered_insert("callie",12)
    orderedList.ordered_insert("victor",27)

    #orderedList.output_list()

    #orderedList.output_justNames()

    #reorderedList=myList.putInOrder()

    #myList.output_justNames()
    #print("\n")
    #reorderedList.output_justNames()

    #print(myList)

    students=openCSV("roster.txt")






main()
