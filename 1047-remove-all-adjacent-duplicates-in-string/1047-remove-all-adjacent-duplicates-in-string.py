class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        string = ""
        for char in s:
            if len(stack) != 0:
                top = stack[-1]
                if char == top:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        for char in stack:
            string += char
        return string