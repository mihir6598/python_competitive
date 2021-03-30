def heapify(arr,i,n):
    l = 2*i+1
    r = 2*i+2
    minimum = i
    if l<n and arr[l]<arr[minimum]:
        minimum = l
    if r<n and arr[r]<arr[minimum]:
        minimum = r
    
    if minimum != i:
        arr[minimum], arr[i] = arr[i], arr[minimum]
        heapify(arr,minimum,n)

if __name__ == "__main__":
    arr = [3,2,3,1,2,4,5,5,6]
    k = 4
    min_heap = arr[:k]
    for i in range(len(min_heap)//2,-1,-1):
        heapify(min_heap,i,k)
    for i in range(k,len(arr)):
        print (min_heap)
        if min_heap[0]<arr[i]:
            min_heap[0] = arr[i]
            heapify(min_heap,0,len(min_heap))
    print (min_heap)