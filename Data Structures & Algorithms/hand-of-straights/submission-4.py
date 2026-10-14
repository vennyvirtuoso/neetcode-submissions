class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq_map=dict()
        for h in hand:
            freq_map[h]=freq_map.get(h,0)+1
        num_groups = len(hand)//groupSize
        if len(hand)%groupSize!=0:
            return False
        for i in range(num_groups):
            firstnz=-1
            for key,val in freq_map.items():
                # print(val)
                if not val==0:
                    firstnz=key
                    break
            if firstnz==-1:
                # print("yes-1")
                return False
            else:
                for i in range(firstnz,firstnz+groupSize):
                    if i in freq_map:
                        if freq_map[i]>0:
                            freq_map[i]-=1
                        else:
                            return False
                    else:
                        return False
        return True