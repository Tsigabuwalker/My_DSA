class Solution:
    def lastStoneWeight(self, stones):
        # Build max heap
        self.buildMaxHeap(stones)
        
        size = len(stones)
        
        while size > 1:
            # Extract largest
            first = stones[0]
            stones[0] = stones[size - 1]
            size -= 1
            self.heapify(stones, size, 0)
            
            # Extract second largest
            second = stones[0]
            stones[0] = stones[size - 1]
            size -= 1
            self.heapify(stones, size, 0)
            
            # If not equal, insert difference
            if first != second:
                stones[size] = first - second
                size += 1
                self.shiftUp(stones, size - 1)
        
        return stones[0] if size == 1 else 0

    def buildMaxHeap(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def shiftUp(self, arr, i):
        parent = (i - 1) // 2
        while i > 0 and arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
            parent = (i - 1) // 2