class fenwik:
    def __init__(self,n):
        self.arr = [0 for i in range(n+1)]
    
    def query(self,i):
        ans = 0 
        i += 1
        while i>0:
            ans += self.arr[i]
            i-=i&(-i)
        return ans
    
    def update(self,i,val,n):
        i += 1
        while i<=n:
            self.arr[i] += val
            i+=i&(-i)

if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = fenwik(len(arr))
    ans = []
    for i in range(len(arr)):
        tree.update(i,arr[i],len(arr))
        ans.append(tree.query(i))
    print (ans)