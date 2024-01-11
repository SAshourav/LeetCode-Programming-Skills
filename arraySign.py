class Solution(object):
    def arraySign(self, nums):
        count = 0
        for single in nums:
            if single < 0:
                count += 1
            elif single == 0:
                return 0
        if count % 2 == 0:
            return 1
        else:
            return -1
