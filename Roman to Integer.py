class Solution(object):
    def romanToInt(self, s):
        Values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        length = len(s)

        i = 0
        while i < length:
            if i < length - 1 and Values[s[i]] < Values[s[i + 1]]:
                value += Values[s[i + 1]] - Values[s[i]]
                i += 2 
            else:
                value += Values[s[i]]
                i += 1

        return value

