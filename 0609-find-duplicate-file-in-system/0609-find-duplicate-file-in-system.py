class Solution:
    def findDuplicate(self, paths):
        content_map = {}   # content -> list of file paths
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            # iterate over files in this directory
            i = 1
            while i < len(parts):
                file_info = parts[i]
                
                # find position of '('
                j = 0
                while file_info[j] != '(':
                    j += 1
                
                name = file_info[:j]
                content = file_info[j+1:-1]   # remove '(' and ')'
                
                full_path = directory + "/" + name
                
                # manually handle dictionary insertion
                if content not in content_map:
                    content_map[content] = []
                
                content_map[content].append(full_path)
                
                i += 1
        
        # collect only duplicates
        result = []
        for content in content_map:
            if len(content_map[content]) > 1:
                result.append(content_map[content])
        
        return result
