class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        def dfs(node):
            curr = node
            last = node
            
            while curr:
                next_node = curr.next
                
                # If current node has a child
                if curr.child:
                    # Flatten the child list
                    child_head = curr.child
                    child_tail = dfs(child_head)
                    
                    # Connect curr to child
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None
                    
                    # Connect child tail to next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    
                    last = child_tail
                    curr = child_tail
                else:
                    last = curr
                
                curr = curr.next
            
            return last
        
        dfs(head)
        return head
