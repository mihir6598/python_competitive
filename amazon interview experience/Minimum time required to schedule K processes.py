# https://www.geeksforgeeks.org/minimum-time-required-to-schedule-k-processes/


def solve(arr,k):
    m = max(arr)
    temp = [0 for i in range(m+1)]
    
    for i in arr:
        temp[i] += 1
    ans = 0
    i = m
    while i>0:
        if i*temp[i]<k:
            k -= i*temp[i]
            temp[int(i/2)] += temp[i]
            ans += temp[i]
            i -= 1
            
        else:
            j = 0
            while j*i<k:
                j+=1
            ans = ans + j
            break
        print (temp,k,ans)
    return ans

if __name__ == "__main__":
    arr = [1, 5, 8, 6]
    print (solve(arr,10))