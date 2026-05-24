class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        visit = set()
        for r in range(len(s)):
            if s[r] not in visit:
                visit.add(s[r])
                maxLen = max(maxLen, (r-l + 1))
                continue
            else:
                while s[r] in visit:
                    visit.remove(s[l])
                    l += 1
                
                visit.add(s[r])
        return maxLen



        