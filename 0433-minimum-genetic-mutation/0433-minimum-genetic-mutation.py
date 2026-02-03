from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # Convert bank to a set for O(1) lookups
        gene_bank = set(bank)
        
        # If the end target isn't in the bank, it's impossible
        if endGene not in gene_bank:
            return -1
        
        # Queue stores (current_gene, mutation_count)
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            curr_gene, count = queue.popleft()
            
            # If we reached the target, return the steps
            if curr_gene == endGene:
                return count
            
            # Try all possible single-character mutations
            for i in range(len(curr_gene)):
                for char in "ACGT":
                    mutation = curr_gene[:i] + char + curr_gene[i+1:]
                    
                    if mutation in gene_bank and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, count + 1))
                        
        return -1