def move_zeros(nums):
    for x in nums:
        if x==0:
            nums.remove(x)
            nums.insert(len(nums), x)
    return nums