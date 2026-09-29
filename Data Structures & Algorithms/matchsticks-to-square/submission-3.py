class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        n=len(matchsticks)
        side = sum(matchsticks)
        if not side%4==0:
            return False
        else:
            side=side//4
        sides=[0]*4

        def make(index):
            if index==n:
                if  sides[0]==sides[1]==sides[2]==sides[3]:
                    return True
            else:

                for i in range(4):
                    if sides[i]+matchsticks[index]<=side:
                        sides[i]+=matchsticks[index]
                        if make(index+1):
                            return True
                        sides[i]-=matchsticks[index]
            return False
        return make(0)



