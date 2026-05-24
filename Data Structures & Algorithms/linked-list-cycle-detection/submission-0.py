# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head.next is None:
            return False
        fast = head.next.next

        
        while slow is not None and fast is not None:
            #print(slow.val, fast.val)
            if slow == fast:
                return True
            
            slow = slow.next

            if fast.next is None:
                return False
            
            fast = fast.next.next

        return False

        