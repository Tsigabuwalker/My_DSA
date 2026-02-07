class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        alice_moves = 0
        bob_moves = 0
        i = 0
        
        while i < n:
            j = i
            # Find consecutive same-color block
            while j < n and colors[j] == colors[i]:
                j += 1
            length = j - i
            if length >= 3:
                if colors[i] == 'A':
                    alice_moves += length - 2
                else:
                    bob_moves += length - 2
            i = j  # Move to next block
        
        return alice_moves > bob_moves
