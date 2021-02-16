class LinkedList:
    def __init__(self):
        self.head = None
    
    def PrintMiddle(self):
        current = self.head
        mid = self.head

        if not current:
            print ("empty linkedlist")
        elif not current.next:
            print ("only one element")

        while current and current.next:
            mid = mid.next
            current = current.next.next
        print (mid.data)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = first = Node(1)
    first.next = second = Node(2)
    second.next = third = Node(3)
    third.next = fourth = Node(4)
    llist.PrintMiddle()