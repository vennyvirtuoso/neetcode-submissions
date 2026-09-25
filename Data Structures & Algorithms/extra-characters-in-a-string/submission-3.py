class Trie:
    def __init__(self):
        self.children = dict()
        self.IsEnd = False
    def insert(self,word,root):
        node = root
        for ch in word:
            if not ch in node.children:
                temp = Trie()
                node.children[ch]=temp
                node=temp
            else:
                node = node.children[ch]
        node.IsEnd = True
    def search(self, word,root):
        node = root

        for ch in word:
            if not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return True if node.IsEnd else False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for st in dictionary:
            root.insert(st,root)

        dp=[-1 for _ in range(len(s)+1)]
        dp[len(s)]=0

        def dfs(i):
            if dp[i]!=-1:
                return dp[i]
            res = 1+dfs(i+1)

            for j in range(i,len(s)):
                if root.search(s[i:j+1],root):
                    res=min(res,dfs(j+1))
            dp[i]=res
            return res

        return dfs(0)