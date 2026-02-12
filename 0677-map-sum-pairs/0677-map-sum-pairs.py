class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary for next letters
        self.value = 0      # Value if this node is the end of a key

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}  # To handle overwriting existing keys

    def insert(self, key: str, val: int) -> None:
        # Calculate delta if key exists
        delta = val
        if key in self.keys:
            delta -= self.keys[key]
        self.keys[key] = val

        # Insert/update in Trie
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += delta  # Update the sum along the path

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value
