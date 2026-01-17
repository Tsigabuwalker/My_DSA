class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Recursive step
        first.next = self.swapPairs(second.next)
        second.next = first
        
        # Now 'second' is the new head of this sub-part
        return second