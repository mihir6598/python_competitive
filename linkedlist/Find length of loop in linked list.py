# Python3 program to detect loop
# in the linked list

# Node class


class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new
    # node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it
    # the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def LengthOfLinkedList(self):
        slow = self.head
        fast = self.head
        flag = 0
        count = 0
        while fast and fast.next and fast.next.next:
            if flag !=0 and fast == slow:
                count = 1
                slow = slow.next
                while slow != fast:
                    count = count + 1
                    slow = slow.next
                print (count)
                break 
            flag = 1
            slow = slow.next
            fast = fast.next.next
        print ("0")


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

llist.LengthOfLinkedList()
