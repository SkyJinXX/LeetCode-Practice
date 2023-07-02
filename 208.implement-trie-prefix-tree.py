#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crt_dic = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not crt_dic.children[i]:
                crt_dic.children[i] = TrieNode()

            crt_dic = crt_dic.children[i]
            
        crt_dic.isWord = True

    def search(self, word: str) -> bool:
        crt_dic = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not crt_dic.children[i]:
                return False
            crt_dic = crt_dic.children[i]
        return crt_dic.isWord

    def startsWith(self, prefix: str) -> bool:
        crt_dic = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not crt_dic.children[i]:
                return False
            crt_dic = crt_dic.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

