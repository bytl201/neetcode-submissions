# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head

        left, right = dummy_node, head
        for _ in range(n):
            right = right.next


        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy_node.next