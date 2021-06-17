# https://www.geeksforgeeks.org/amazon-interview-experience-11/


from collections import defaultdict
import gc
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            new = Node(val)
            self.tail.right = new
            new.left = self.tail
            self.tail = new
    def print_list(self):
        head = self.head
        while head:
            print (head.val)
            head = head.right
    def remove(self,val):
        index = 1
        head = self.head
        while head:
            if head.val == val:
                self.deleteNode(head)
                break
            index = index + 1
            head = head.right
        return index
    def deleteNode(self,node):
        if not node:
            return
        if node == self.head:
            self.head = self.head.right
        if node.right:
            node.right.left = node.left
        if node.left:
            node.left.right = node.right
        gc.collect()
                    

def solve(s):
    ans = 0
    list = List() 
    mom = [0]*26
    for i in s:
        list.add(ord(i)-ord('a'))
        mom[ord(i)-ord('a')] += 1
    ans = 0
    for i in range(len(mom)):
        for j in range(mom[i]):
            print (i,j)
            ans = ans + list.remove(i)
    return ans

if __name__ == "__main__":
    s = "aacba"
    print (solve(s))