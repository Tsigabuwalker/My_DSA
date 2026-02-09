class Solution:
    def connect(self, root):
        current = root

        while current is not None:
            dummy = Node(0)
            tail = dummy

            while current is not None:
                if current.left is not None:
                    tail.next = current.left
                    tail = tail.next

                if current.right is not None:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            current = dummy.next

        return root
