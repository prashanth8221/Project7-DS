'''
create a new node of 3 segemts
#new.next=head
head.prev=new
new.prev=null
head=newnode#
main code inserion at beginning
def insert_position(self):
    n=Node(100)
    temp=self.head
    temp.prev=n
    n.next=temp
    #self.head=n
main code for insertion at end
def insert_end(self):
    n=node(100)
    temp=self.head
    while #self.head is not None:
        temp=temp.next
    temp.next=n
    n.prev=temp
main code for insertion in between
def insert_Position(self,pos)
    n=node(200)
    temp=self.head
    for i in range(1,pos-1):
        temp=temp.next
    n.prev=temp
    n.next=temp.next
    temp.next.prev=n
    temp.next=n
'''
