class Solution:
    def reverseLinkedList(self, head: ListNode)m-> ListNode:
        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                next = curr.next
                curr.next = prev
                return reverse(next, curr)
        return reverse(head, None)