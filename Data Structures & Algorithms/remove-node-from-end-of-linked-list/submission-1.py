# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        size = 1
        cur = head
        while cur:
            cur = cur.next
            size += 1
        
        
        res = ListNode(0, head)
        prev = res
        cur = res.next
        i = 1
        while cur:
            if i == size - n:
                prev.next = cur.next
                break

            cur = cur.next 
            prev = prev.next
            i += 1


        return res.next
        