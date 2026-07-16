class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_hash = [[0 for i in range(26)] for j in range(1000)]
        for i, strr in enumerate(strs):
            for j in range(len(strr)):
                list_hash[i][ord(strr[j])-97]+=1

        list_dict = dict()
        for i in range(len(strs)):
            if tuple(list_hash[i]) in list_dict:
                list_dict[tuple(list_hash[i])].append(strs[i])
            else:
                list_dict[tuple(list_hash[i])]=[strs[i]]


        ans = []
        for lst in list_dict.values():
            ans.append(lst)
        return ans