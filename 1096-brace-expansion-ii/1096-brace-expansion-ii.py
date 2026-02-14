class Solution:
    def braceExpansionII(self, expression: str):
        
        def helper(i):
            res = set()
            cur = {""}
            
            while i < len(expression):
                if expression[i].isalpha():
                    cur = {prefix + expression[i] for prefix in cur}
                    i += 1
                
                elif expression[i] == '{':
                    sub, i = helper(i + 1)
                    cur = {a + b for a in cur for b in sub}
                
                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1
                
                elif expression[i] == '}':
                    break
            
            return res | cur, i + 1
        
        result, _ = helper(0)
        return sorted(result)
