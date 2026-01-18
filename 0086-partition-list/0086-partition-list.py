class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes to start our "less than" and "greater/equal" lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to the current last node in the two lists
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                # Add to the "before" list
                before.next = curr
                before = before.next
            else:
                # Add to the "after" list
                after.next = curr
                after = after.next
            
            # Move to the next node in the original list
            curr = curr.next
        
        # IMPORTANT: Terminate the "after" list to prevent a cycle
        after.next = None
        
        # Connect the "before" list with the "after" list
        before.next = after_head.next
        
        # Return the head of the combined partitioned list
        return before_head.next