"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_imp = 0
        
        def dfs(cur_id):
            nonlocal total_imp
            
            for i, employee in enumerate(employees):
                if employee.id == cur_id:
                    ind = i
                    break
            
            total_imp += employees[ind].importance
            
            for sub in employees[ind].subordinates:
                dfs(sub)
        
        dfs(id)
        return total_imp