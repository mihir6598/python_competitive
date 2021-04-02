import heapq
def solve(arr):

    heapq.heapify(arr)

    res = 0
    while len(arr)>1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        res = first + second
        heapq.heappush(arr,first + second)
    return res

if __name__ == "__main__":
    arr = [ 4, 3, 2, 6 ]
    print (solve(arr))