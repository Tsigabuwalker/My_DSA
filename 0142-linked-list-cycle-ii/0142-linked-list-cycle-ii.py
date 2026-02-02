class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Phase 1: Detect the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle found! Move to Phase 2
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        
        # No cycle found
        return None