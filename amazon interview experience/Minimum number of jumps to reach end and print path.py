def jump(arr):
        if len(arr) == 1:
            return 0
        if not arr:
            return 0
        i = 1
        ans = [0]
        cango = arr[0]
        jump = 0
        new = 0
        while i<len(arr):
            if i>cango:
                jump += 1
                if cango == new:
                    return -1    
                cango = new
                ans.append(new_i)
            if new < arr[i]+i:
                new_i = i
                new = arr[i]+i
            i += 1
            
        return ans + [len(arr)-1]

# https://leetcode.com/submissions/detail/480399089/
if __name__ == "__main__":
    arr = [3, 3, 0, 2, 1, 2, 4, 2, 0, 0]
    print (jump(arr))