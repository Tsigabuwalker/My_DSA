
class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        curr = self.head.next
        i = 2

        while curr:
            if random.randint(1, i) == 1:
                res = curr.val
            curr = curr.next
            i += 1

        return res
