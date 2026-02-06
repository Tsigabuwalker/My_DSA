class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store complete word at the end


class Solution:
    def findWords(self, board, words):
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # Step 2: DFS backtracking
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]

            # If we found a word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates

            # Mark cell as visited
            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            # Restore cell
            board[r][c] = char

            # Optimization: prune Trie
            if not next_node.children:
                node.children.pop(char)

        # Step 3: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
