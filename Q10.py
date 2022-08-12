# 배열 파티션1 (p.190)

def arrayPairSum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum

#def arrayPairSum(nums):
#    return sum(sorted(nums)[::2])

res = arrayPairSum([1, 4, 3, 2])
print(res)
