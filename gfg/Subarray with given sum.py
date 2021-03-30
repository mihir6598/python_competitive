def subArraySum(arr, n, s): 
    #Your code here
    l = 0
    r = 0
    sum = 0
    while (l<=r and r<n):
        
        sum = sum + arr[r]
        if sum<s:
            r = r + 1
        elif sum == s:
            print (l,r)
            break
        else:
            sum = sum - arr[l] - arr[r]
            l = l + 1

N = 10 
S = 15
A = [1,2,3,4,5,6,7,8,9,10]
subArraySum(A,N,S)
for acc in accumulate(A):
    print (acc)