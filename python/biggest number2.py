class LargerNumKey(str):
    def __gt__(x, y):
        print (x,y)
        print (x+y > y+x)
        return x+y > y+x
        

def largestNumber( nums):
    largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
    return '0' if largest_num[0] == '0' else largest_num

nums = [2,10,23]
print (largestNumber(nums))