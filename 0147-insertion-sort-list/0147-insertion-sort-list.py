# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # dummy head of sorted list
        current = head

        while current:
            prev = dummy
            next_node = current.next  # save next node

            # find the correct position to insert current
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next
