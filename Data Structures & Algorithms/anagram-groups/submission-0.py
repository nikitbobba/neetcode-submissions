class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            letters = [0] * 26
            for c in word.lower():
                idx = ord(c) - ord('a')
                letters[idx] += 1
            print(d)
            if tuple(letters) in d:
                d[tuple(letters)].append(word)
            else:
                d[tuple(letters)] = [word]
        
        return d.values()
            

        