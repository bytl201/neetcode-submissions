
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break the link and keep a pointer to the second half of the linked list
        slow2 = slow.next
        slow.next = None

        # reverse the second half of the linked list
        prev = None
        while slow2:
            temp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = temp

        # modify the linked list and connect the nodes
        left, right = head, prev
        while right:
            # next nodes
            left_next = left.next
            right_next = right.next

            # link the nodes
            left.next = right
            right.next = left_next

            # move the pointers to the right
            left = left_next
            right = right_next
