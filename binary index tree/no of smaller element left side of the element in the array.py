class fenwik:
    def __init__(self,n):
        self.arr = [0 for i in range(n+2)]
    
    def query(self,i):
        ans = 0 
        i += 1
        i-=i&(-i)
        while i>0:
            print (i)
            ans += self.arr[i]
            i-=i&(-i)
        return ans
    
    def update(self,i,val,n):
        i += 1
        while i<=n:
            self.arr[i] += val
            i+=i&(-i)

if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 1]
    tree = fenwik(max(arr))
    ans = []
    arr.reverse()
    for i in range(len(arr)):
        tree.update(arr[i],1,max(arr))
        ans.append(tree.query(arr[i]))
    print (ans)