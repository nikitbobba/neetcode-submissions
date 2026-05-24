class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        for c in s:
            if c in first:
                first[c] += 1
            else:
                first[c] = 1
        
        for c in t:
            if c not in first:
                return False
            else:
                first[c] -= 1
        
        for letter in first:
            if first[letter] != 0:
                return False
        
        return True
        