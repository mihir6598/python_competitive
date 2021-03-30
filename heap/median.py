def heapify_max(arr,i,n):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,largest,n)
    return arr

def heapify_min(arr,i,n):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,largest,n)
    return arr

def insert_max(arr,n):
    arr.append(n)
    s = len(arr)-1
    location = len(arr)-1
    while(s):
        s = (location-1)//2
        if arr[s]<arr[location]:
            arr[s] , arr[location] = arr[location], arr[s]
            location = s
        else:
            break
    return arr
def insert_min(arr,n):
    arr.append(n)
    s = len(arr)-1
    location = len(arr)-1
    while(s):
        s = (location-1)//2
        if arr[s]>arr[location]:
            arr[s] , arr[location] = arr[location], arr[s]
            location = s
        else:
            break
    return arr
            


def sol(arr):
   

    ans = 0
    arr_left = []
    arr_right = []
    for i in range(len(arr)):
        if arr[i]<ans:
            if len(arr_left)>len(arr_right):
                temp = arr_left[0]
                arr_left[0] = arr[i]
                arr_left = heapify_max(arr_left,0,len(arr_left))
                arr_right = insert_min(arr_right,temp)
            else:
                arr_left = insert_max(arr_left,arr[i])
        else:
            if len(arr_left)<len(arr_right):
                temp = arr_right[0]
                arr_right[0] = arr[i]
                arr_right = heapify_min(arr_right,0,len(arr_right))
                arr_left = insert_max(arr_left,temp)
            else:
                arr_right = insert_min(arr_right,arr[i])
        if i >1:
            if not i%2:
                if len(arr_left)>len(arr_right):
                    ans = arr_left[0]
                else:
                    ans = arr_right[0]
            else:
                ans = (arr_left[0]+arr_right[0])/2
        elif i == 0:
            ans = arr[0]
        else:
            ans = (arr[0]+arr[1])/2
    print (ans)
        # print (arr_left)
        # print (arr_right)

if __name__ == "__main__":
    arr = [5,10,19,1,4,8,7,5 ]
    sol(arr)
    