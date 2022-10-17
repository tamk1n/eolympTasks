import math
def narcissistic(nar_num):
    length = len(str(nar_num))
    res=0
    numList=[]
    for item in str(nar_num):
        numList.append(item)
    print(numList)
    for digit in numList:
        res+=math.pow(int(digit), length)
    if res == nar_num:
        return True
    else:
        return False

print(narcissistic(153))