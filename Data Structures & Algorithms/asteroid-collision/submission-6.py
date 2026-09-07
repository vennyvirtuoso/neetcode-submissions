class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stateas= []

        for ast in asteroids:
            if not stateas:
                stateas.append(ast)
            else:
                while stateas and stateas[-1]>0 and ast<0:
                    if abs(ast)>abs(stateas[-1]):
                        stateas.pop()
                        # stateas.append(ast)
                    elif stateas and abs(ast)==abs(stateas[-1]):
                        stateas.pop()
                        ast=1001

                        break
                    elif stateas and abs(ast)<abs(stateas[-1]):
                        ast=1001
                        break
                if ast!=1001 and  (not stateas or ast>0 or ast<0 and stateas[-1]<0):
                    stateas.append(ast)
        return stateas