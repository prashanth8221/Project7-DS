class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None

    def push_back(self, newElement):
        newNode = Node(newElement)
        if (self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

        # Delete first node of the list

    def pop_front(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            if (self.head != None):
                self.head.prev = None

                # display the content of the list

    def PrintList(self):
        temp = self.head
        if (temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

    # test the code
MyList = DLL()

    # Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.PrintList()

    # Delete the first node
MyList.pop_front()
MyList.PrintList()
