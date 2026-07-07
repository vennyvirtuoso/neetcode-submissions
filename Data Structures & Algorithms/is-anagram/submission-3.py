class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = [0 for _ in range(26)]
        # print(ord('a'))
        for ch in s:
            letter_count[ord(ch)-97]+=1
        
        for ch in t:
            letter_count[ord(ch)-97]-=1
        for num in letter_count:
            if num!=0:
                return False
        return True