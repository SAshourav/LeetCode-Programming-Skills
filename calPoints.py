class Solution(object):
    def calPoints(self, operations):
        arr = []
        total_sum = 0

        for ch in operations:
            if ch.isdigit() or (ch[0] == '-' and ch[1:].isdigit()):
                arr.append(int(ch))
            elif ch == "C" or ch == 'c':
                if arr:
                    arr.pop()
            elif ch == "D" or ch == 'd':
                if len(arr) >= 1:
                    product = arr[-1] * 2
                    arr.append(product)
            elif ch == "+":
                if len(arr) >= 2:
                    add = arr[-1] + arr[-2]
                    arr.append(add)

        total_sum = sum(arr)
        return total_sum
