class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            print(window, maxLen)
            if s[r] in window:
                while s[r] in window:
                    print('in while', window, l)
                    window.remove(s[l])
                    l += 1
                
                window.add(s[r])
                continue
            else:
                window.add(s[r])
            maxLen = max(maxLen, r-l+1)

        
        return maxLen
        