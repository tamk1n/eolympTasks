def in_array(a1, a2):
  r=[]
  for x in a1:
    for y in a2:
      if "".join(y.split(x)) != y and x not in r:
        r.append(x)
        r.sort()
  return r