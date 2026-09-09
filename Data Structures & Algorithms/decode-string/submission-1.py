class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch=="]":
                temp=""
                while stack and stack[-1]!="[":
                    temp =stack.pop()+temp
                stack.pop()
                multi = ""
                while stack and  '0' <= stack[-1] <= '9':
                    multi = stack.pop()+multi
                # print(temp)
                multi = int(multi)
                stack.append(multi*temp)
            else:
                stack.append(ch)
        # print(stack)
        return "".join(stack)