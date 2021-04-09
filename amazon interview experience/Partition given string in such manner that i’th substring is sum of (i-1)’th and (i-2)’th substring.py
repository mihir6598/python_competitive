def findsequenceUtil(arr,first,second,ans):
    third = str(int(first)+int(second))
    for i in range(1,len(arr)+1):
        if arr[:i] == third:
            if i == len(arr):
                print (ans+[third])
                return True
            else: 
                return findsequenceUtil(arr[i:],second,third,ans+[third])
        elif int(arr[:i]) >= int(third):
            break
    
    return False

def findsequence(s):
    for i in range(1,len(s)//3+1):
        first = s[:i]
        for j in range(i+1,(len(s)+1-i)//2+1):
            second = s[i:j]
            ans = [first,second]
            if findsequenceUtil(s[j:],first,second,ans):
                return True
    else:
        return False

if __name__ == "__main__":
    s = "1111213"
    print (findsequence(s))