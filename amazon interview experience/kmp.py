def coumputeLPS(pat,M,lps):
    len = 0
    i = 1
    
    while i<M:
        if pat[len] == pat[i]:
            len += 1
            lps[i] = len
            i = i + 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                len = 0
                i += 1

def KMPSearch(pat,txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    i = 0
    coumputeLPS(pat,M,lps)
    print (lps)
    
    while i<N:
        print (i,j)
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print ("found at " + str(i-j))
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    

if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCAB"
    KMPSearch(pat, txt)