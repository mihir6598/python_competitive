from typing import List
# https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val
        
def solve(head,k):
    # printlist(head)
    if not head:
        return None
    pre = None
    cur = head
    main = head
    next = None
    count = 0
    while cur and count < k:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        count = count + 1
    main.next = solve(next,k)
        
    return pre

def printlist(head):
    while head:
        print (head.val)
        head = head.next
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    k = 3
    printlist(solve(head,k))