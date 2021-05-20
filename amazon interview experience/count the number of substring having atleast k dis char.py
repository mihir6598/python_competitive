from collections import defaultdict

def solve(s,k):
    mp = defaultdict(int)
    start = 0
    end = 0
    n = len(s)
    ans = 0
    while end<n:
        c = s[end]
        end += 1
        mp[c] += 1
        
        while len(mp)>= k:
            temp = s[start]
            start += 1
            mp[temp] -= 1
            if mp[temp] == 0:
                del mp[temp]
            ans += n - end +1
    return ans
            
if __name__ == "__main__":
    s = "abcca"
    k = 3
    print (solve(s,k))