def solve(n,o,c,s):
    if c == n:
        final.append(s)
        return
    if o>c:
        solve(n,o,c+1,s+"}")
        if o < n:
            solve(n,o+1,c,s+"{")
    else:
        solve(n,o+1,c,s+"{")


if __name__ == "__main__":
    final = []
    solve(3,0,0,"")
    print (final)