def dis_ins_case(input):
    count=0
    inputList = [i for i in input]
    for x in inputList:
        if inputList.count(x) > 1:
            inputList.remove(x)
            count+=1
    return count