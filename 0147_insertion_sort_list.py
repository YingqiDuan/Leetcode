# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(head.val, head)

        # 'pre' is the last node of the sorted portion.
        # 'cur' is the node to be inserted into the sorted portion.
        pre, cur = dummy, head
        while cur:
            # correct order
            if pre.val <= cur.val:
                pre, cur = cur, cur.next
                continue
            # find the correct spot, start from the dummy node
            p = dummy
            # stop when we reach a node whose next node has a value greater
            while p.next.val <= cur.val:
                p = p.next

            # save next node
            t = cur.next
            # insert
            cur.next = p.next
            p.next = cur
            # remove cur
            pre.next = t
            # move to next node
            cur = t
        return dummy.next
