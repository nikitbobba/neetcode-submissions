class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        for c in s:
            if c in s_table:
                s_table[c] += 1
            else:
                s_table[c] = 1
        
        for c in t:
            if c not in s_table:
                return False
            else:
                if s_table[c] < 1:
                    return False
                else:
                    s_table[c] -= 1
        
        for key in s_table.keys():
            if s_table[key] > 0:
                return False
        return True
        