class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        min_cap_heap = []
        for i in range(n):
            min_cap_heap.append((capital[i], profits[i]))
            
        def heapify_up(heap, i, is_min):
            while i > 0:
                p = (i - 1) // 2
                if (is_min and heap[i][0] < heap[p][0]) or (not is_min and heap[i] > heap[p]):
                    heap[i], heap[p] = heap[p], heap[i]
                    i = p
                else: break

        def heapify_down(heap, i, is_min):
            size = len(heap)
            while True:
                l, r, target = 2*i + 1, 2*i + 2, i
                if l < size and ((is_min and heap[l][0] < heap[target][0]) or (not is_min and heap[l] > heap[target])):
                    target = l
                if r < size and ((is_min and heap[r][0] < heap[target][0]) or (not is_min and heap[r] > heap[target])):
                    target = r
                if target != i:
                    heap[i], heap[target] = heap[target], heap[i]
                    i = target
                else: break

        def push(heap, val, is_min):
            heap.append(val)
            heapify_up(heap, len(heap)-1, is_min)

        def pop(heap, is_min):
            if not heap: return None
            res = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                heapify_down(heap, 0, is_min)
            return res

        for i in range((n // 2) - 1, -1, -1):
            heapify_down(min_cap_heap, i, True)

        max_profit_heap = []
        current_w = w
        
        for _ in range(k):
            while min_cap_heap and min_cap_heap[0][0] <= current_w:
                cap, prof = pop(min_cap_heap, True)
                push(max_profit_heap, prof, False)
            
            if not max_profit_heap:
                break
                
            current_w += pop(max_profit_heap, False)
            
        return current_w