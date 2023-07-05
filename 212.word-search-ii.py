#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crt_dic = self.root
        for c in word:
            if c not in crt_dic.children:
                crt_dic.children[c] = TrieNode()

            crt_dic = crt_dic.children[c]
            
        crt_dic.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        trie = Trie()
        for w in words:
            trie.insert(w)

        m = len(board)
        n = len(board[0])
        
        for y in range(m):
            for x in range(n):
                def dfs(xx, yy, crt_dic):
                    char = board[yy][xx]
                    if char == '#':
                        return

                    if char in crt_dic.children:
                        if crt_dic.children[char].word:
                            res.append(crt_dic.children[char].word)
                            crt_dic.children[char].word = "" # Trim
                        board[yy][xx] = '#'

                        # do something
                        if xx + 1 < n:
                            dfs(xx + 1, yy, crt_dic.children[char])
                        if yy + 1 < m:
                            dfs(xx, yy + 1, crt_dic.children[char])
                        if xx - 1 >= 0:
                            dfs(xx - 1, yy, crt_dic.children[char])
                        if yy - 1 >= 0:
                            dfs(xx, yy - 1, crt_dic.children[char])

                        board[yy][xx] = char
                        if not crt_dic.children[char].children and not crt_dic.children[char].word: # Trim
                            crt_dic.children.pop(char)

                dfs(x, y, trie.root)
        
        return res

# @lc code=end

