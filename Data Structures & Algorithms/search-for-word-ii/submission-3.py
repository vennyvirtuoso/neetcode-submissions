class Trie:
    def __init__(self):
        self.children=dict()
        self.IsEnd=False

    def insert(self,word,root):
        node = root
        for ch in word:
            
            if not ch in node.children:
                temp = Trie()

                node.children[ch]=temp
                node= temp
            else:
                node = node.children[ch]
        node.IsEnd = True

    def search(self, word, root):
        node =root
        for ch in word:
            if not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return True if node.IsEnd else False
    def search_prefix(self,word,root):
        node =root
        for ch in word:
            if not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ans=[]
        m=len(board)
        n=len(board[0])
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        # trie creation
        root=Trie()
        for i in range(len(words)):
            root.insert(words[i],root)


        def trace(i,j,visited,node,curr):
            # print(curr)
            if node.IsEnd:
                ans.append(curr)
                node.IsEnd=False

            ch = board[i][j]
            if ch in node.children:
                curr+=board[i][j]
                visited[i][j]=1

                node=node.children[ch]
                if node.IsEnd:
                    ans.append(curr)
                    node.IsEnd=False


                # else: 
                if i-1>=0 and j>=0 and i-1<m and j<n and visited[i-1][j]==0:
                    trace(i-1,j,visited,node,curr)

                if i+1>=0 and j>=0 and i+1<m and j<n and visited[i+1][j]==0:
                    trace(i+1,j,visited,node,curr)

                if i>=0 and j-1>=0 and i<m and j-1<n and visited[i][j-1]==0:
                    trace(i,j-1,visited,node,curr)

                if i>=0 and j+1>=0 and i<m and j+1<n and visited[i][j+1]==0:
                    trace(i,j+1,visited,node,curr)

            visited[i][j]=0

                


        for i in range(len(board)):
            for j in range(len(board[0])):
                trace(i,j,visited,root,curr="")



        return ans