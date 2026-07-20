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
            fast = fast.next
            fast = fast.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        left, right, new_list = head, prev, ListNode(-1, None)
        while left or right:
            if left:
                temp = left.next
                new_list.next = left
                new_list = new_list.next
                left = temp
            if right:
                temp = right.next
                new_list.next = right
                new_list = new_list.next
                right = temp

        walker = new_list.next
        while walker:
            print(walker.val)
            walker = walker.next
