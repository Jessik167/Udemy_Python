class Solution:
    def twoSum(self, nums, target: int):
        hash = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash:
                return [i,hash[rest]]
            else:
                hash[nums[i]] = i



nums = [3,2,3,15,11]
targ = 18
s = Solution()
print(s.twoSum(nums,targ))