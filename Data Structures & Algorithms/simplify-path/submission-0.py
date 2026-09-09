class Solution:
    def simplifyPath(self, path: str) -> str:
        filtered = ""
        for ch in path:
            if filtered and ch==filtered[-1]=="/":
                continue
            else:
                filtered+=ch
        # print(filtered)
        stack=[]
        # stack.append("/")
        n = len(filtered)
        # print(n)
        i=0
        while i<n:
            to_push=""
            while i<n and filtered[i]!="/":
                to_push+=filtered[i]
                i+=1
            if to_push=="..":
                if not stack:
                    continue
                stack.pop()
            elif to_push==".":
                continue
            else:
                if to_push!="":
                    stack.append(to_push)
            i+=1
        ans=""
        # print(stack)
        while stack:
            # print(stack.pop())
            ans = "/"+stack.pop()+ans
        if ans=="":
            return "/"
        return ans



