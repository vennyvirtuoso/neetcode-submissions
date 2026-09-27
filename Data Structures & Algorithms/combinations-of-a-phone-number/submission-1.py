class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        visited = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0,0],
            [0,0,0],
            [0,0,0,0],
        ]
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def permut(i,curr):
            if len(curr)==len(digits):
                ans.append(curr)
            else:
                for letter in mapping[digits[i]]:
                    permut(i+1,curr+letter)
        permut(0,curr="")
        if  ans==[""]:
            return []
        else:
            return ans