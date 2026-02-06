class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        slots = 1  # start with one slot for the root

        for node in nodes:
            # occupy one slot
            slots -= 1

            # If slots become negative, invalid
            if slots < 0:
                return False

            # Non-null node generates two new slots
            if node != "#":
                slots += 2

        # All slots should be used
        return slots == 0
