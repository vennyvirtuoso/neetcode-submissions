class Solution:
    def XorTotal(self,index,nums,ans,rxor):
        # print(rxor)
        # print(index)
        # print(len(nums))
        if index<len(nums):
            if rxor==-1:
                rxor=nums[index]

            self.XorTotal(index+1,nums,ans,rxor)
            self.XorTotal(index+1,nums,ans,rxor^nums[index])
                # rxor = rxor^nums[index]
                
        else:
            ans[0]+=rxor
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=[0]
        self.XorTotal(0,nums,ans,rxor=-1)
        return ans[0]