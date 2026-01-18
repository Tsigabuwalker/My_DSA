class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        # Dummy node helps handle the head of the list easily
        dummy = ListNode(0)
        dummy.next = head
        
        prev_group_tail = dummy
        
        while True:
            # 1. Check if there are k nodes left
            kth_node = self.getKthNode(prev_group_tail, k)
            if not kth_node:
                break
                
            next_group_start = kth_node.next
            
            # 2. Reverse the current group
            # We keep track of the node that will become the new tail
            curr = prev_group_tail.next
            prev = kth_node.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 3. Connect the previous group's tail to the new group head
            # prev is now the head of the reversed group
            new_group_tail = prev_group_tail.next
            prev_group_tail.next = prev
            prev_group_tail = new_group_tail
            
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr