class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        s1_count = 0
        s2_count = 0
        index = 0
        recall = dict()  # index in s2 -> (s1_count, s2_count)

        while s1_count < n1:
            for c in s1:
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2_count += 1
            s1_count += 1

            if index in recall:
                s1_prev, s2_prev = recall[index]
                pre_loop_s2 = s2_prev
                loop_s1 = s1_count - s1_prev
                loop_s2 = s2_count - s2_prev

                remaining_s1 = n1 - s1_count
                loops = remaining_s1 // loop_s1

                s2_count += loops * loop_s2
                s1_count += loops * loop_s1

                # simulate the leftover s1 repeats
                for _ in range(n1 - s1_count):
                    for c in s1:
                        if c == s2[index]:
                            index += 1
                            if index == len(s2):
                                index = 0
                                s2_count += 1
                return s2_count // n2
            else:
                recall[index] = (s1_count, s2_count)

        return s2_count // n2
