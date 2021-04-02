# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-7-months-experienced/
def solve(n,o,c,ans):
    if c == n:
        print (ans)
        return
    if o>c:
        solve(n,o,c+1,ans+'}')
        if o<n:
            solve(n,o+1,c,ans+'{')
    else:
        solve(n,o+1,c,ans+'{')
if __name__ == "__main__":
    solve(3,0,0,'')