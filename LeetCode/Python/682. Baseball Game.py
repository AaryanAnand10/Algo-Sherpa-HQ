class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            result.append(result[len(result)-1]+result[len(result)-2]) if i=='+' else result.append(result[len(result)-1]*2) if i=='D' else result.pop() if i=='C' else result.append(int(i)) 
        return sum(result)
