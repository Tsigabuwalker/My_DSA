import random

class RandomizedCollection:
    def __init__(self):
        self.nums = []  # List of all values
        self.idx_map = {}  # val -> set of indices in nums

    def insert(self, val: int) -> bool:
        # Add val to nums
        self.nums.append(val)
        # Add index to idx_map
        if val in self.idx_map:
            self.idx_map[val].add(len(self.nums) - 1)
            return False  # val already existed
        else:
            self.idx_map[val] = {len(self.nums) - 1}
            return True  # first insertion

    def remove(self, val: int) -> bool:
        if val not in self.idx_map or not self.idx_map[val]:
            return False  # val not present
        
        # Remove an index of val from idx_map
        remove_idx = self.idx_map[val].pop()
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        # Swap removed element with the last element if not the same
        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val
            # Update the idx_map for last_val
            self.idx_map[last_val].remove(last_idx)
            self.idx_map[last_val].add(remove_idx)
        
        # Remove the last element
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
