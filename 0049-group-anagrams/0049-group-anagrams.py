from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use a defaultdict to handle keys that don't exist yet
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key for the anagram group
            # Sorting "eat", "tea", and "ate" all result in "aet"
            key = "".join(sorted(s))
            
            # Append the original string to the corresponding list
            anagram_map[key].append(s)
            
        # Return only the grouped lists
        return list(anagram_map.values())