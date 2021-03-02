def solve(arr,n):
    final = {}
    for i in arr:
        if n-i in final:
            return True
        else:
            final[i] = "1"
    return False
if __name__ == "__main__":
    arr = [5,7,1,2,8,4,3]
    print (solve(arr,100))