def solution(arr,x):
    n = len(arr)
    first = 0
    first = find_first(arr,0,n-1,x)
    last = find_last(arr,first,n-1,x)
    print (last - first +1)
    # print (last)

def find_first(arr,low,high,x):
    if high >= low:
        mid = (high+low)//2
   
    # print (mid)
        if (arr[mid] == x ) and (x>arr[mid-1] or mid == 0):
            return mid
        elif (x>arr[mid]):
            return find_first(arr,mid+1,high,x)
        else:
            return find_first(arr,low,mid-1,x)
    else:
        return -1
    

def find_last(arr,low,high,x):
    if high >= low:
        mid = (high+low)//2
        print (mid)
        if (arr[mid] == x) and (x<arr[mid+1] or mid == (len(arr)-1)):
            return mid
        elif (x<arr[mid]):
            return find_last(arr,low,mid-1,x)
        else:
            print ("else")
            return find_last(arr,mid+1,high,x)
    else:
        return -1


if __name__ == "__main__":
    arr = [1,2,2,2,2,4,5]
    solution(arr,2)