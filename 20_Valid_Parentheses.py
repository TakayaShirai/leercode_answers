class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.appendleft(s[i])
            elif s[i] == ")" and len(stack) > 0 and stack[0] == "(":
                stack.popleft()
            elif s[i] == "}" and len(stack) > 0 and stack[0] == "{":
                stack.popleft()
            elif s[i] == "]" and len(stack) > 0 and stack[0] == "[":
                stack.popleft()
            else:
                return False
        
        return len(stack) == 0
