class Solution(object):
    def isAnagram(self, s, t):
        list_t = list(t)
        list_s = list(s)
        list_t.sort()
        list_s.sort()
        if list_t == list_s:
            return True
        return False
        
        
        
        