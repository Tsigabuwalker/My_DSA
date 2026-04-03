class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)
        
        visited = [False] * n
        queue = [id]
        visited[id] = True
        
        current_level = 0
        
        while queue and current_level < level:
            next_queue = []
            
            for person in queue:
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        next_queue.append(f)
            
            queue = next_queue
            current_level += 1
        
        freq = {}
        
        for person in queue:
            for video in watchedVideos[person]:
                if video in freq:
                    freq[video] += 1
                else:
                    freq[video] = 1
        
        result = list(freq.keys())
        result.sort(key=lambda x: (freq[x], x))
        
        return result