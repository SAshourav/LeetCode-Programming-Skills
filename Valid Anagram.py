# one way of solving this can be : 

class Solution(object):
    def isAnagram(self, s, t):
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s==t

#but this takes 50ms time which is a huge time complexity . we can reduce it by using the dictionary method

class Solution(object):
    def isAnagram(self, s, t):
        char_count = defaultdict(int)

        for ch in s:
            char_count[ch] += 1

        for ch in t:
            if ch not in char_count or char_count[ch] == 0:
                return False
            char_count[ch] -= 1

        return True

  #this takes only 24ms time
  
