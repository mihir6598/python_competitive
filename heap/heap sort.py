def heapify(arr,i,n):
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

def heapsort(arr):
    for i in range(len(arr)//2-1,-1,-1):
       heapify(arr,i,len(arr))

    for i in range(len(arr)-1,-1,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,0,i)
    

if __name__ == "__main__":
    arr = [5,10,19,1,4,8,7,5 ]
    heapsort(arr)
    print (arr)