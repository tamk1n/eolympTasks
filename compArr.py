arr1 = [3, 8, 6, 12, 5]
arr2 =[64, 124, 9, 36, 25]
newArr=[]

for i in arr1:
    newArr.append(i**2)
if arr2.sort() == newArr.sort():
    print(False)

a = [1,2]
b= [1,2,3]

print(arr2.sort() == newArr.sort())
print(newArr)