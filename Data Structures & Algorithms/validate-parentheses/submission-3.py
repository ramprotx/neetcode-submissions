class Solution:
    def isValid(self, s:str)->bool:
        stack=[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1]==closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False


    # def isValid(self, s: str) -> bool:
    #     while '()' in s or '{}' in s or'[]' in s:
    #         s = s.replace('()', '')
    #         s = s.replace('{}', '')
    #         s = s.replace('[]', '')
    #     return s == ''


    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     mapping = {')': '(', '}': '{', ']': '['}
    #     for char in s:
    #         if char in mapping:
    #             top_element = stack.pop() if stack else '#'
    #             if mapping[char] != top_element:
    #                 return False
    #         else:
    #             stack.append(char)
    #     return not stack