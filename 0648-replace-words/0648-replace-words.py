class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()
        
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True
        
        def find_root(word):
            node = root
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    return word
                node = node.children[ch]
                prefix += ch
                if node.end:
                    return prefix
            return word
        
        words = sentence.split(" ")
        for i in range(len(words)):
            words[i] = find_root(words[i])
        
        return " ".join(words)
