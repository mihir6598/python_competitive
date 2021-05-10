# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-full-time-referral-2020/
def solve(s):
    arr = [-1]*26
    
    for i in range(len(s)):
        arr[ord(s[i])-ord('a')] = i
    
    ans = []
    temp = ''
    m = 0
    for i in range(len(s)):
        m = max(m,arr[ord(s[i])-ord('a')])
        
        temp = temp + s[i]
        
        if m == i:
            ans.append(temp)
            temp = ''
    return ans


if __name__ == "__main__":
    s = "acbbcc"
    print (solve(s))