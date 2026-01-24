class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 1. Move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # 2. Reverse sublist
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next
