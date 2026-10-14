class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq_map=[0]*1001
        for h in hand:
            freq_map[h]+=1
        num_groups = len(hand)//groupSize
        if len(hand)%groupSize!=0:
            return False
        for i in range(num_groups):
            firstnz=-1
            for i in range(1001):
                if not freq_map[i]==0:
                    firstnz=i
                    break
            if firstnz==-1:
                return False
            else:
                for i in range(firstnz,firstnz+groupSize):
                    if freq_map[i]>0:
                        freq_map[i]-=1
                    else:
                        return False
        return True