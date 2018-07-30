# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle2(self, head):
        fast, slow = head, head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False
