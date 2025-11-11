from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return len(stack) == 0

print(Solution.validateStackSequences(Solution(), [1,2,3,4,5], [4,5,3,2,1]))
print(Solution.validateStackSequences(Solution(), [1,2,3,4,5], [4,3,5,1,2]))
