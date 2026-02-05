class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H))
            events.append((R, H))
        
        events.sort()

        res = [[0, 0]]
        live_heights = [0]
        
        def push(val):
            live_heights.append(val)
            curr = len(live_heights) - 1
            while curr > 0:
                parent = (curr - 1) // 2
                if live_heights[curr] > live_heights[parent]:
                    live_heights[curr], live_heights[parent] = live_heights[parent], live_heights[curr]
                    curr = parent
                else:
                    break

        def remove(val):
            for i in range(len(live_heights)):
                if live_heights[i] == val:
                    live_heights[i] = live_heights[-1]
                    live_heights.pop()
                    sift_down(i)
                    break

        def sift_down(curr):
            while True:
                left = 2 * curr + 1
                right = 2 * curr + 2
                largest = curr
                if left < len(live_heights) and live_heights[left] > live_heights[largest]:
                    largest = left
                if right < len(live_heights) and live_heights[right] > live_heights[largest]:
                    largest = right
                if largest != curr:
                    live_heights[curr], live_heights[largest] = live_heights[largest], live_heights[curr]
                    curr = largest
                else:
                    break

        for x, h in events:
            if h < 0:
                push(-h)
            else:
                remove(h)
            
            max_h = live_heights[0]
            if res[-1][1] != max_h:
                res.append([x, max_h])
        
        return res[1:]