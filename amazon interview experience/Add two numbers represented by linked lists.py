# https://www.geeksforgeeks.org/sum-of-two-linked-lists/
# https://www.geeksforgeeks.org/amazon-interview-experience-offcampus-for-sde-1/?ref=rp

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

def printList(head):
    while (head):
        print (head.val)
        head = head.next
def findLength(head):
    ans = 0
    while head:
        head = head.next
        ans = ans+1
    return  ans


def solve(head1,head2):
    
    def final(head1,head2,length1,length2):
        
        if length1>length2:
            sum = head1.val + final(head1.next,head2,length1-1,length2)
            add = sum//10
            sum = sum%10
            head1.val = sum
            return add
        if length1 ==0:
            return 0  
        if length1 == length2:
            sum = head1.val + head2.val + final(head1.next,head2.next,length1-1,length2-1)
            add = sum//10
            sum = sum%10
            head1.val = sum
            # print (sum)
            return add 
        return 0

    length1 = findLength(head1)
    length2 = findLength(head2)
    
    temp = final(head1,head2,length1,length2)
    if temp != 0:
        head = ListNode(temp)
        head.next = head1
        printList(head)
    else:
        printList(head1)


if __name__ == "__main__":
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    head2 = ListNode(9)
    head2.next = ListNode(9)
    head2.next.next = ListNode(9)
    # printList(head)
    # printList(head2)
    solve(head,head2)
    