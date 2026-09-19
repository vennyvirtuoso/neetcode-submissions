class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for bill in bills:
            if bill!=5:
                change=bill-5
                if change==5:
                    if not five:
                        return False
                    else:
                        five-=1
                if change==15:
                    if five:
                        if ten:
                            five-=1
                            ten-=1
                        elif five>2:
                            five-=3
                        else:
                            return False
                    else:
                        return False
                if bill==10:
                    ten+=1
            else:
                five+=1
        return True