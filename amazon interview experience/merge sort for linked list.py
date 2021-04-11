# https://www.geeksforgeeks.org/amazon-interview-experience-offcampus-for-sde-1/?ref=rp

# https://www.geeksforgeeks.org/merge-sort-for-linked-list/

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

def merge(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    ans = ListNode(0)
    current = ans
    while head1 and head2:
        if head1.val < head2.val:
            current.next = head1
            head1 = head1.next
            current = current.next
            current.next = None
        else:
            current.next = head2
            head2 = head2.next
            current = current.next
            current.next = None
    if head1:
        current.next = head1
    if head2:
        current.next = head2
    # printList(ans.next)
    return ans.next
            
def printList(head):
    while head:
        print (head.val)
        head = head.next
    
def mergesort(head):
    slow = head
    fast = head
    
    while (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    if fast == slow:
        if fast.next:
            left = head
            right = head.next
            left.next = None
        else:
            return head
    else:
        right = slow.next
        slow.next = None
        left = head
        # printList (left)
        # print ("")
        # printList(right)
    left = mergesort(left)
    right = mergesort(right)
    
    head = merge(left,right)
    printList(head)
    print("")
    return head

if __name__ == "__main__":
    head = ListNode("1")
    head.next = ListNode("1")
    head.next.next = ListNode("1")
    head.next.next.next = ListNode("3")
    head = mergesort(head)
    printList(head)