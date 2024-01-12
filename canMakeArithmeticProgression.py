class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[0] - arr[1]
        i = 1
        while i < len(arr) - 1:
            diff_con = arr[i] - arr[i + 1]
            if not diff == diff_con:
                return False
            i += 1
            diff = diff_con
        return True


# more optimized 

        arr = sorted(arr)

        diff = arr[1] - arr[0]

        for i in range(0,len(arr) - 1):
            if (arr[i + 1] - arr[i] != diff):
                return False
        
        return True
