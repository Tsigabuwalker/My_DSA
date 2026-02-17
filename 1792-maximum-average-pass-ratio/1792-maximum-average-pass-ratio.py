class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        heap = []
        
        def heapify_up(i):
            while i > 0:
                parent = (i - 1) // 2
                if heap[parent][0] >= heap[i][0]:
                    break
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
        
        def heapify_down(i):
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                
                if left < n and heap[left][0] > heap[largest][0]:
                    largest = left
                if right < n and heap[right][0] > heap[largest][0]:
                    largest = right
                
                if largest == i:
                    break
                
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
        
        for p, t in classes:
            heap.append([gain(p, t), p, t])
            heapify_up(len(heap) - 1)
        
        for _ in range(extraStudents):
            top = heap[0]
            p = top[1] + 1
            t = top[2] + 1
            heap[0] = [gain(p, t), p, t]
            heapify_down(0)
        
        total = 0
        for g, p, t in heap:
            total += p / t
        
        return total / len(classes)
