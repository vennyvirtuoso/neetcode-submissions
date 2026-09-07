class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalstack = []
        for tk in tokens:
            if tk=="+" or tk == "*" or tk == "-" or tk =="/":
                first = evalstack.pop()
                second = evalstack.pop()
                if tk=="+":
                    evalstack.append(first+second)
                if tk=="-":
                    evalstack.append(second-first)
                if tk=="*":
                    evalstack.append(first*second)
                if tk=="/":
                    evalstack.append(int(second/first))
            else:
                evalstack.append(int(tk))
        return evalstack.pop()