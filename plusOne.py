class Solution(object):
    def plusOne(self, digits):
        result = []
        number = 0
        for ed in digits:
            number = (number * 10) + ed
        number += 1
        while number != 0:
            single = number % 10
            result.append(single)
            number = number // 10  

        result = list(reversed(result))
        return result
