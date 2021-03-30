test = [(10,5),(10,1),(10,3),(1,10)]
print (sorted(test,key= lambda x:x[1]))
test2 = [1,2]
for i in map(lambda x:x+10,test2):
    print (i)