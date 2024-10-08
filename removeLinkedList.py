class Solution:
    def removeElements(self, head:ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            next = curr.next

            if curr.val == val:
                prev.next = next
            else:
                prev = curr
                curr = next
        return dummy.next