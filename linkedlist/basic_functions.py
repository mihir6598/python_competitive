class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print ("empty")
        else:
            temp = self.head
            while temp!= None:
                print (temp.data)
                temp = temp.next
    
    def push(self, new_data): 
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
        # 3. Make next of new Node as head 
        new_node.next = self.head             
        # 4. Move the head to point to new Node  
        self.head = new_node 

    def insertAfter(self, prev_node, new_data):  
    # 1. check if the given prev_node exists  
        if prev_node is None:  
            print ("The given previous node must inLinkedList.")
            return
        # 2. Create new node &  
        # 3. Put in the data  
        new_node = Node(new_data)  
        # 4. Make next of new Node as next of prev_node  
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node  
        prev_node.next = new_node

    def append(self, new_data): 
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
                self.head = new_node 
                return
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
        # 6. Change the next of last node 
        last.next =  new_node 

    def deleteNode(self, key): 
         
        # Store head node 
        temp = self.head 
 
        # If head node itself holds the key to be deleted 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        # if key was not present in linked list 
        if(temp == None): 
            return
        # Unlink the node from linked list 
        prev.next = temp.next
        temp = None

    def DeleteList(self):
        current = self.head
        while current:
            pre = current.next
            del current.data
            current = pre
            print ("in")

    def getCount(self): 
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
  
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count 

    def getCountRecursive(self,node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)
    
    def CountRecursive(self):
        return self.getCountRecursive(self.head)



if __name__ == "__main__":
    llist = LinkedList()
    llist.head = first = Node(1)
    first.next = second = Node(2)
    second.next = third = Node(3)
    llist.push(4)
    llist.insertAfter(second,10)
    llist.append(15)
    llist.deleteNode(4)
    # llist.DeleteList()
    count = llist.CountRecursive()
    print ("count", count)
    llist.traversal()
    
