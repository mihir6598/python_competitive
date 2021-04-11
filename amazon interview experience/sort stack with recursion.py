# https://www.geeksforgeeks.org/amazon-interview-experience-offcampus-for-sde-1/?ref=rp

def solve2(n,arr):
    if not arr:
        arr.append(n)
        return
    if n>arr[-1]:
        arr.append(n)
        return
    temp = arr.pop()
    solve2(n,arr)
    arr.append(temp)

def solve(arr):
    if not arr:
        return
    temp = arr.pop()
    solve(arr)
    solve2(temp,arr)

if __name__ == "__main__":
    stack = [4,5,2,3,1,6]
    solve(stack)
    print (stack)