import sys
class Trie:
    def __init__(self):
        self.word_index = -1
        self.char_dic = {}
def wordSearch(n: int, m: int, grid: list, k: int, words_list: list):
    # generate res list
    res = ['No'] * k
    # generate Trie for words_list
    root_trie = Trie()
    for i in range(k):
        crt_trie = root_trie
        for c in words_list[i]:
            if c not in crt_trie.char_dic:
                crt_trie.char_dic[c] = Trie()
            crt_trie = crt_trie.char_dic[c]
        crt_trie.word_index = i
    
    # iterate the grid
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for r in range(n):
        for c in range(m):
            for dr, dc in directions: # for each cell, iterate through it's four directions
                def iterateOneDirection(r, c, dr, dc):
                    crt_trie = root_trie
                    while -1 < r < n and -1 < c < m:
                        if grid[r][c] in crt_trie.char_dic:
                            if crt_trie.char_dic[grid[r][c]].word_index != -1:
                                res[crt_trie.char_dic[grid[r][c]].word_index] = 'Yes' # change res list
                                if not crt_trie.char_dic[grid[r][c]].char_dic: # delete empty trie
                                    del crt_trie.char_dic[grid[r][c]]
                                    break
                            crt_trie = crt_trie.char_dic[grid[r][c]]
                            r += dr
                            c += dc
                        else:
                            break
                iterateOneDirection(r, c, dr, dc)
    
    return res

if __name__ == "__main__" and '--debug' not in sys.argv:
    n, m = list(map(int,input().split()))
    grid = []
    for r in range(n):
        grid.append(list(map(int, input().split())))

    k = int(input().strip())
    words_list = input().split()

    res = wordSearch(n, m, grid, k, words_list)

    print(' '.join(res))
else:
    n, m, grid, k, words_list = [3, 3, [['C', 'A', 'T'],['I', 'D', 'O'], ['N', 'O', 'M']], 4, ['CAT', 'TOM', 'ADO', 'MOM']]
    res = wordSearch(n, m, grid, k, words_list)

    print(' '.join(res))