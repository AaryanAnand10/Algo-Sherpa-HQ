class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            result.append(result[len(result)-1]+result[len(result)-2]) if i=='+' else result.append(result[len(result)-1]*2) if i=='D' else result.pop() if i=='C' else result.append(int(i)) 
        return sum(result)



# alternative solution
 # class Solution:
 #    def calPoints(self, operations: List[str]) -> int:
 #        result=[]
 #        for i in range(len(operations)):
 #            if((operations[i]=='D')):
 #                result.append(result[-1]*2)
 #            elif(operations[i]=='+'):
 #                result.append((int(result[-2]))+int(result[-1]))
 #            elif(operations[i]=='C'):
 #                result.pop()
 #            else:
 #                result.append(int (operations[i]))
 #        return sum(result)
