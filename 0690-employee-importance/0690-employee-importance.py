class Solution:
    def getImportance(self, employees, id: int) -> int:
        # Build a map from id -> Employee object
        emp_map = {emp.id: emp for emp in employees}
        
        # DFS to sum importance
        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total
        
        return dfs(id)
