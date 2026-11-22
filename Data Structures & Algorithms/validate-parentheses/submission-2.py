class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == "(" or item == "{" or item == "[":
                stack.append(item)
            else:
                if stack == []:
                    return False
                matching = stack.pop()
                if item == ")" and matching == "(":
                    continue
                elif item == "}" and matching == "{":
                    continue
                elif item == "]" and matching == "[":
                    continue
                else:
                    return False
        return stack == []
                