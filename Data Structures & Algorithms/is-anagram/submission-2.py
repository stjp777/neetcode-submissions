class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort(key=str.lower)
        
        t.sort(key=str.lower)
        
        if t == s: return True;
        else: return False;