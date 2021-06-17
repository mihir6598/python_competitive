class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def solve(head):
    tmp = 0
    if head.next:
        tmp = solve(head.next)
        if head.val - tmp>=0:
            head.val = head.val - tmp
            return 0
        else:
            head.val = 9
            return 1
    else:
        if head.val == 0:
            head.val = 9
            return  1
        else:
            head.val = head.val - 1
            return 0

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(0)
    head.next.next = Node(1)
    
    solve(head)
    while (head):
        print (head.val)
        head = head.next