class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c)%26] += 1
            
            t_key = tuple(key)
            if t_key in seen:
                seen[t_key].append(word)
            else:
                seen[t_key] = [word]
        
        return list(seen.values())
        