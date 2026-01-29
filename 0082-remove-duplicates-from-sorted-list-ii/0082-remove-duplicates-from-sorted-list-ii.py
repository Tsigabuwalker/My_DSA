class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # If current node has duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with this value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next
