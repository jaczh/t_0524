class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, data in enumerate(nums):
            m = target - data
            if m in d:
                return [d[m], i]
            else:
                d[data] = i

#modify 2
