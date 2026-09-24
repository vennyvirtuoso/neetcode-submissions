class Trie:
    def __init__(self):
        self.children=dict()
        self.IsEnd=False
    def insert(self,word,root):
        node = root
        for ch in word:
            if not ch in node.children:
                temp= Trie()
                node.children[ch]=temp
                node=temp
            else:
                node=node.children[ch]
        node.IsEnd=True
        
    def search(self,word,root):
        node=root

        for i,ch in enumerate(word):
            if ch==".":
                ans=False
                for key in node.children.keys():
                    ans|=self.search(word[i+1:],node.children[key])
                return ans

            elif not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return True if node.IsEnd else False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
    def addWord(self, word: str) -> None:
        self.root.insert(word,self.root)
    def search(self, word: str) -> bool:
        return self.root.search(word,self.root)
        
