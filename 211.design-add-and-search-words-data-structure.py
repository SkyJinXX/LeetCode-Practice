#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        crt_dic = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not crt_dic.children[i]:
                crt_dic.children[i] = TrieNode()

            crt_dic = crt_dic.children[i]
            
        crt_dic.isWord = True

    def search(self, word: str) -> bool:
        stk = [(self.root, 0)]
        # print(word)
        while stk:
            crt_dic, i = stk.pop()
            # print([chr(index + ord('a')) for index, item in enumerate(crt_dic.children) if item is not None], word[i] if i < len(word) else 'complete')

            if i == len(word):
                if crt_dic.isWord:
                    return True
                else:
                    continue

            if word[i] == '.':
                for j in range(len(crt_dic.children)):
                    if crt_dic.children[j]:
                        stk.append((crt_dic.children[j], i + 1))
            else:
                j = ord(word[i]) - ord('a')
                if not crt_dic.children[j]:
                    continue
                crt_dic = crt_dic.children[j]
                stk.append((crt_dic, i + 1))

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

