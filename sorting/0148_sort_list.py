# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check empty
        if not head or not head.next:
            return head

        # uses two pointers to find the middle of the list
        slow, fast = head, head.next
        # By the time the fast pointer reaches the end of the list,
        # the slow pointer will be at the midpoint.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        # breaks the list into two
        slow.next = None

        # recursive sorting
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            # Comparison
            if l1.val < l2.val:
                # the smaller value is appended
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next
