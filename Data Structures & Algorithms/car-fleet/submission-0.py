class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = []
        for p,s in zip(position, speed):
            pairs.append((p,s))
        
        for p, s in sorted(pairs)[::-1]:
            ttd = (target-p) / s
            stack.append(ttd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        