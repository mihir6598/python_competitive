def toString(List): 
    return ''.join(List) 
    
def solve(s,l):
    if l == len(s):
        print (toString(s))
        return 
    for i in range(l,len(s)):
            s[i],s[l] = s[l],s[i]
            solve(s,l+1)
            s[i],s[l] = s[l],s[i]

if __name__ == "__main__":
    s = ['m','h','r']
    solve(s,0)