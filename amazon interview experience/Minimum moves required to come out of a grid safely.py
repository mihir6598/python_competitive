def solve(arr):
    fire = [[0 for i in range(len(arr))] for j in range(len(arr))]
    visited = [[0 for i in range(len(arr))] for j in range(len(arr))]
    
    fire_q = []
    person_q = []
    
    moves_x = [1, -1, 0, 0]
    moves_y = [0, 0, 1, -1]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                fire[i][j] = 1
                fire_q.append((i,j,0))
            if arr[i][j] == 1:
                visited[i][j] = 1
                person_q.append((i,j,0))
    depth = 0
    while fire_q and person_q:
        print (fire_q)
        print (person_q)
        while fire_q and fire_q[0][2] == depth:
            t = fire_q.pop(0)
            for i in range(len(moves_x)):
                
                x = t[0] + moves_x[i]
                y = t[1] + moves_y[i]
                temp = (x,y,depth+1)
                # print (temp)
                if temp[0]>=0 and temp[0]<len(arr) and temp[1]>=0 and temp[1]<len(arr) and fire[temp[0]][temp[1]] != 1:
                    # print ("in")
                    fire_q.append(temp)
                    # print (fire_q)
                    fire[temp[0]][temp[1]] = 1
        
        while person_q and person_q[0][2] == depth:
            t = person_q.pop(0)
            for i in range(len(moves_x)):
                x = t[0] + moves_x[i]
                y = t[1] + moves_y[i]
                temp = (x,y,depth+1)
                if temp[0]>=0 and temp[0]<len(arr) and temp[1]>=0 and temp[1]<len(arr) and visited[temp[0]][temp[1]] != 1 and fire[temp[0]][temp[1]] != 1:
                    if temp[0] == 0 or temp[0] == len(arr)-1 or temp[1] == 0 or temp[1] == len(arr)-1:
                        return depth + 1
                    # print ("in")
                    # print (person_q)
                    person_q.append(temp)
                    visited[temp[0]][temp[1]] = 1
                
        depth = depth + 1    
    return -1            
                 
    


if __name__ == "__main__":
    arr = [ [ 0, 0, 0, 0 ],
             [ 2, 0, 0, 0 ],
             [ 2, 1, 0, 0 ],
             [ 2, 2, 0, 0 ] ]
    print (solve(arr))