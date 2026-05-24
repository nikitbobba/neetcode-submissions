class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            if tuple(count) in store:
                store[tuple(count)].append(word)
            else:
                store[tuple(count)] = [word]
        return store.values()        