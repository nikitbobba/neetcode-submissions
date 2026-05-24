class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0 for i in range(len(nums))]

        prefix_total = 1
        for i in range(len(nums)):
            prefix_total *= nums[i]
            prefix.append(prefix_total)
        
        postfix_total = 1
        for i in range(len(nums)-1, -1, -1):
            postfix_total *= nums[i]
            postfix[i] = postfix_total
        
        output = []
        for i in range(len(nums)):
            prefix_idx = i - 1
            postfix_idx = i + 1

            prefix_val = 1 if prefix_idx < 0 else prefix[prefix_idx]
            postfix_val = 1 if postfix_idx > len(nums)-1 else postfix[postfix_idx]
            #print(prefix_val, postfix_val)
            output.append(prefix_val*postfix_val)
        return output
                