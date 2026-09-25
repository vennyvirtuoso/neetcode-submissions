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

class PrefixTree:

    def __init__(self):
        self.children=dict()
        self.IsEnd=False
        self.root=Trie()

    def insert(self, word: str) -> None:
        self.root.insert(word,self.root)

    def search(self, word: str) -> bool:
        return self.root.search(word,self.root)

    def startsWith(self, prefix: str) -> bool:
        return self.root.search_prefix(prefix,self.root) 
        