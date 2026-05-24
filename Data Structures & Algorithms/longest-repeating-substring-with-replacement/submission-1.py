class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if (r-l+1) - max(count.values()) <= k:
                # still a valid subsctring so we can keep going
                res = max(res, r-l+1)
                continue
            else:
                # we are above the k value so we need to shorten the window until the condition becomes true again
                while (r-l+1) - max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1
        
        return res
        