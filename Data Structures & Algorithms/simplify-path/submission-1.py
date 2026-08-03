class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        
        for curr in paths:
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "" and curr != '.':
                stack.append(curr)
        
        return '/' + '/'.join(stack)