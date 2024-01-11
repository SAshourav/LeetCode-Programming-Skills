#not that optimized solution

class Solution(object):
    def moveZeroes(self, nums):
        iteration = 0
        while (iteration < len(nums)):
            for i in range(len(nums)):
                if nums[i] == 0 and len(nums) > i+1:
                    temps = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temps
            iteration += 1
        



#Optimize Solution

class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return

        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1
