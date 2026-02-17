class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # store positions of each digit as a list
        pos = [[] for _ in range(10)]
        for i, ch in enumerate(s):
            pos[int(ch)].append(i)
        
        # pointer for each digit to track used indices
        pointer = [0] * 10

        for ch in t:
            digit = int(ch)
            # check if we have remaining occurrences of this digit
            if pointer[digit] >= len(pos[digit]):
                return False
            idx = pos[digit][pointer[digit]]
            pointer[digit] += 1

            # check if any smaller digit blocks this one
            for smaller in range(digit):
                if pointer[smaller] < len(pos[smaller]) and pos[smaller][pointer[smaller]] < idx:
                    return False
        return True
