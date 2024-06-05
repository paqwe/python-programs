class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None




class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        A_node=Node(data)
        # A_node.ref=None
        if self.head is None:
            self.head = A_node
        else:
            n=self.head
            while n.ref is not None:
                n = n.ref
            n.ref = A_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can not delete nodes!")
        else:
            self.head=self.head.ref


        




LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_after(200,10)
LL1.delete_begin()

LL1.print_LL()

