arr = [2,-3,4,1,-1]
newRes = []
if not arr:
  print(0)
else:
  for i in range(0,9):
    for j in range(i+1,9):
      res = sum(arr[i:j])
      newRes.append(res)
  print(max(newRes))



