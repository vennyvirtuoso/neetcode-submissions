class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans=[]
        def combination(i,curr,total):
            # if i<len(candidates)-1 and candidates[i]==candidates[i+1]:
            #     combination(i+1,curr,total)

            if total==target:
                ans.append(curr.copy())
                return 
            elif total<target and i<len(candidates):


                curr.append(candidates[i])
                combination(i+1,curr,total+candidates[i])
                curr.pop()
                while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                    i=i+1
                combination(i+1,curr,total)
                




        combination(0,[],0)
        return ans  