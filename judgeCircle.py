class Solution(object):
    def judgeCircle(self, moves):
        right = 0
        left = 0
        up = 0
        down = 0

        for mv in moves:
            if(mv == 'R'):
                right += 1
            elif mv == 'L':
                left += 1
            elif mv == 'U':
                up += 1
            elif mv == 'D':
                down += 1
        
        if right == left and up == down:
            return True
        else:
            return False


#all of this can be done just using inbuild count function !!!!!!!!!!!!!


