class Solution(object):
    def isMonotonic(self, nums):
        countIncrese = 0
        countDecrese = 0
        for i in range (len(nums)-1):
            if nums[i] > nums[i+1]:
                countDecrese += 1 
            if nums[i] < nums[i+1]:
                countIncrese += 1
        if countIncrese != 0 and countDecrese != 0:
            return False
        else:
            return True
        
