# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        slo = head
        fast = head.next

        while fast.next and fast.next.next:
            if fast == slo:
                return True
            fast = fast.next.next
            slo = slo.next
        
        return False
