# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None
        walker = second_half
        while walker:
            temp = walker.next
            walker.next = prev
            prev = walker
            walker = temp

        left, right = head, prev
        while right:
            temp_left = left.next
            temp_right = right.next

            left.next = right
            right.next = temp_left

            left = temp_left
            right = temp_right


