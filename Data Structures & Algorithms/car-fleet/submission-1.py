class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinedps=[]
        for i in range(len(position)):
            combinedps.append([position[i],speed[i]])
        combinedps.sort()
        mstack=[]
        # print(combinedps)
        for ps in reversed(combinedps):
            if not mstack:
                mstack.append([[ps[0]],ps[1]])
            elif ps[1]<=mstack[-1][1]:
                # time = (target-ps[0])
                mstack.append([[ps[0]],ps[1]])
            elif ps[1]>mstack[-1][1]:
                time = (target-mstack[-1][0][0])/mstack[-1][1]
                if time*ps[1]>=(target-ps[0]):
                    pair = mstack.pop()
                    pair[0].append(ps[0])
                    mstack.append(pair)

                else:
                    mstack.append([[ps[0]],ps[1]])
            
        return len(mstack)