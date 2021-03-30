import string

def solve(str1,l,r):
    global ans
    global ans2
    if l<=r:
        if r-l+1>ans:
            print (str1[l:r]," ",str1[r:l:-1])
            if str1[l:r] == str1[r:l:-1]:
                if ans<r-l:
                    ans2 = str1[l:r]
                    ans = r-l
            solve(str1,l+1,r)
            solve(str1,l,r-1)


if __name__ == "__main__":
    str1 = "aa"
    ans = 0
    ans2 = ""
    (solve(str1,0,len(str1)))
    print (ans2)
    print (ans)