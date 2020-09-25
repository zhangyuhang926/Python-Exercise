def r_arry(nums):
    res = []
    for i in range(len(nums)):
        for s in nums[i+1:]:
            if s > nums[i]:
                j = s
                break
            else:
                j = -1
        res.append(j)
    res[-1] = -1
    return res

nums = [9, 1, 5, 4, 6, 2, 4, 0]
print(r_arry(nums))