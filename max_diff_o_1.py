def solution(arr):
    x=0
    y=0
    x_new = 0
    y_new = 0
    max = 0
    for i in arr:
        if i == 1:
            if abs((x+1)-y)>abs((x_new+1)-y_new):
                x = x+1
                x_new = 1
                y_new = 0
            else:
                x = x_new + 1
                y = y_new
                x_new = 1
                y_new = 0
        else:
            if abs(x-(y+1))>abs(x_new-(y_new+1)):
                y = y+1
                x_new = 0
                y_new = 1
            else:
                y = y_new + 1
                x = x_new
                x_new = 0
                y_new = 1
        print (x,y)
        print (x_new,y_new)
        print (" ")
        if abs(x-y)>max:
            max = abs(x-y)
    print (max)

if __name__ == "__main__":
    arr = [1,1,0,0,0,0,1,0,0,0,1]
    solution(arr)