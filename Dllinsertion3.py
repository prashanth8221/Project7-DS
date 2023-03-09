class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None

    def insert_Position(self, pos,data):
        n = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
ob=DLL()
n=Node(100)
ob.head=n
n1=Node(200)
n1.prev=n
n.next=n1
n2=Node(300)
n2.prev=n1
n1.next=n2
ob.display()
print("")
print("after insertion")
ob.insert_Position(2,150)
ob.display()