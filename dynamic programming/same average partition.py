def solve(arr,left,right,l_average,r_average,main_average,i):
    # print (left,l_average,r_average,right,main_average)
    global a
    # print (a)
    if i == len(arr):
        if l_average == r_average:
            print (left,right)
            return True
        a.add((len(left),l_average))
        a.add((len(right),r_average))
        return False

    if (len(left),l_average) in a:
        return
    if (len(right),r_average) in a:
        return
    # if l_average>main_average:
    #     return
    # if r_average>main_average:
    #     return
    
        
    left.append(arr[i])
    l = solve(arr,left,right,sum(left)/len(left),r_average,main_average,i+1)
    left.pop()
    if l:
        return True
    right.append(arr[i])
    r = solve(arr,left,right,l_average,sum(right)/len(right),main_average,i+1)
    right.pop()
    if r:
        return True
    return False

if __name__ == "__main__":
    # arr = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
    arr = [5,16,4,11,4]

    a = set()
    arr.sort()
    temp = arr.pop()
    print (arr)
    print (solve(arr,[],[temp],0,temp,sum(arr)/len(arr),0))
