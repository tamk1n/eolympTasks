def solution(list):
    count = 0
    res = []
    one = ""
    for num in list:
      if one == "":
        last = int(num)
        one = int(num)
        count+=1
      else:
        if int(num) == last+1:
          count+=1
          last = int(num)
          if num == list[len(list)-1] and count >=3:
            res.append(str(one)+"-"+str(num))
          elif num == list[len(list)-1] and count == 2:
            res.extend([one, last])
        else:
          if count >= 3:
            res.append(str(one)+"-"+str(last))
            if num == list[len(list)-1]:
                res.append(num)
            one=int(num)
            count =1
            last = int(num)
          elif count == 1:
            if num == list[len(list)-1]:
              res.extend([last,num])
              break
            res.append(last)
            last = int(num)
            one=int(num)
          else:
            if num == list[len(list)-1]:
              res.extend([one,last,num])
              break
            res.extend([one, last])
            last = int(num)
            one=int(num)
            count=1
    y=""
    for x in res:
        if x == res[len(res)-1]:
            y+=f"{str(x)}"
        else:
            y+=f"{str(x)},"

    return y