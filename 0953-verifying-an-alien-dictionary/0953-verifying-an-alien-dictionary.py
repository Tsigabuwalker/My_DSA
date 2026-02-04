class Solution:
    def isAlienSorted(self, words, order):
        # Step 1: Create a mapping of each character to its rank in the alien language
        order_map = {}
        for index, char in enumerate(order):
            order_map[char] = index

        # Step 2: Compare each consecutive pair of words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare character by character
            for j in range(min(len(word1), len(word2))):
                c1 = word1[j]
                c2 = word2[j]

                if order_map[c1] < order_map[c2]:
                    # word1 < word2 → correct order, move to next pair
                    break
                elif order_map[c1] > order_map[c2]:
                    # word1 > word2 → wrong order
                    return False
            else:
                # Words match up to the shorter length, so check lengths
                if len(word1) > len(word2):
                    return False

        return True
