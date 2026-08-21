class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[]
        dig1="INF"
        dig2="INF"
        count1=0
        count2=0
        for i in range(n):

            if dig1==nums[i]:
                count1+=1
            elif dig2==nums[i]:
                count2+=1
            elif count1==0:
                dig1=nums[i]
                count1+=1
            elif count2==0:
                dig2=nums[i]
                count2+=1
            else:
                count1-=1
                count2-=1
        
        count1=0
        count2=0
        for i in range(n):
            if nums[i]==dig1:
                count1+=1
            if nums[i]==dig2:
                count2+=1
        if count1>(n//3):
            ans.append(dig1)
        if count2>(n//3):
            ans.append(dig2)
        return ans