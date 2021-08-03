print ("lets go")

import math

test = 10
print (math.exp(test))
print (math.log(test))


from collections import defaultdict

test = defaultdict(list)
print (test[1])
test[1] = 2
print (test)
del test[1]
print (test)

import heapq

test = [1]
heapq.heapify(test)
heapq.heappush(test,2)
temp = heapq.heappop(test)

