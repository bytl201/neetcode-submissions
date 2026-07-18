# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, walker = None, head

        while walker:
            if walker.val == val:
                if prev:
                    prev.next = walker.next
                else:
                    head = walker.next
                    
            else:
                prev = walker
            walker = walker.next
            
        return head