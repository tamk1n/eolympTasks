def longest_consec(strarr, k):
  n= len(strarr)
  if n<k or n==0 or k<=0:
    return ""
  else:
    values = []
    new = {}
    for i in range(0,n):
      res = "".join(strarr[i:i+k])
      length = len(res)
      new[res] = str(length) 
    
    for k, v in new.items():
      values.append(int(v))
      
    for k , v in new.items():
      if new[k] == str(max(values)):
        return k
        break
  