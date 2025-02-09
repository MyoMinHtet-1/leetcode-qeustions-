#O(N^2) complexity time, a more efficient brute force method

class Solution(object):
    def twoSum(self, nums, target):
        for a in range(0, len(nums)):
            anchor = nums[a] #it stores an anchor value.
            for b in range(a+1, len(nums)):  
                if anchor + nums[b]== target:
                    return [a,b]


# O(n) complexity time,  
