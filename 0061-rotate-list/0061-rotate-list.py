# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Compute effective rotations
        k = k % length
        if k == 0:
            return head  # No rotation needed
        
        # Step 3: Connect tail to head to make it circular
        tail.next = head
        
        # Step 4: Find the new tail: (length - k) steps from the start
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 5: New head is next of new tail
        new_head = new_tail.next
        new_tail.next = None  # Break the circle
        
        return new_head
