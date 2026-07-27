# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # unlink the nodes after 'slow' node
        slow2 = slow.next
        slow.next = None

        # reverse the links to go in other direction (left)
        prev = None
        while slow2:
            temp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = temp

        # connect all the nodes together
        left, right = head, prev
        while right:
            next_left = left.next
            next_right = right.next

            left.next = right
            right.next = next_left

            left = next_left
            right = next_right
