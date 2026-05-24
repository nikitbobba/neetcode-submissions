class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        window = {}
        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        l = 0
        need = len(countT)
        have = 0

        res, resLen = [-1,-1], float('inf')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                # we have all the necessay count for that letter in the window
                have += 1
            
            while need == have:
                # we have met the result condition
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Remove a char from the left now in order to get min possible window
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]: res[1]+1] if resLen != float('inf') else ""
        


        