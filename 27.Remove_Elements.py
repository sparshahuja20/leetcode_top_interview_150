


def removeElemts(nums, val):
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k += 1
    return k

nums = [0,1,2,2,3,0,4,2]
result = removeElemts(nums, 2)
print(result)