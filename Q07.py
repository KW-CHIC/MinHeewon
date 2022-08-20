# 두 수의 합 (p.173)

def twoSum(nums, target):
    for i in nums:
        rest = target - i
        n = nums.index(i)
        
        if rest in nums[n+1:]:
                res = [nums.index(i), nums[n+1:].index(rest) + (n+1)]
                print(res)
                break

twoSum([2,7,11,15], 9)
