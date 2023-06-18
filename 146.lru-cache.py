#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        if len(self.cache) < 2 or key == self.tail:
            return self.cache[key]['val']
        
        # process original relationship
        if key == self.head and len(self.cache) != 1:
            self.head = self.cache[key]['nxt']
        if self.cache[key]['pre'] != None: # pre=0 会导致这句话不执行。但是我们的意思是 pre 为None的时候才不执行
            self.cache[self.cache[key]['pre']]['nxt'] = self.cache[key]['nxt']
        if self.cache[key]['nxt'] != None:
            tmp = self.cache[key]['nxt']
            self.cache[self.cache[key]['nxt']]['pre'] = self.cache[key]['pre']

        # process new relationship
        self.cache[self.tail]['nxt'] = key
        self.cache[key]['nxt'] = None
        self.cache[key]['pre'] = self.tail
        self.tail = key
        
        # if self.cache[key]['nxt'] == self.head:
        #     print(key, '.next:', self.cache[key]['nxt'])
        return self.cache[key]['val']

    def put(self, key: int, value: int) -> None:
        # the key already in cache, only have to modify and move the node
        if key in self.cache:
            self.cache[key]['val'] = value
            self.get(key)
            return

        # if exceed cap, move head 
        if len(self.cache) == self.cap:
            temp = self.head # store head
            if self.head == self.tail: # if xxx, clear tail
                self.tail = None
            self.head = self.cache[self.head]['nxt'] # move head
            self.cache[temp]['nxt']=None
            self.cache[temp]['pre']=None
            del self.cache[temp] # delete node
            if self.head in self.cache:
                self.cache[self.head]['pre'] = None

        # add node to cache
        if self.head == None:
            self.head, self.tail = key, key
            self.cache[key] = {'val': value, 'pre': None, 'nxt': None}
        else:
            self.cache[key] = {'val': value, 'pre': self.tail, 'nxt': None}
            test = self.cache[self.tail]
            self.cache[self.tail]['nxt'] = key
            self.tail = key
        
        # if key == 2896:
        #     print('2896来过')
        #     if key in self.cache:
        #         print('2896存在过', self.cache[2896])
        # if self.cache[key]['nxt'] == self.head:
        #     print(key, '.next:', self.cache[key]['nxt'])

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
def run_operations(operations, values):
    lru_cache = None
    for op, val in zip(operations, values):
        if op == "LRUCache":
            lru_cache = LRUCache(val[0])
            # print(f"LRUCache created with capacity {val[0]}")
        elif op == "put":
            lru_cache.put(val[0], val[1])
            # print(f"Put key {val[0]} with value {val[1]}")
        elif op == "get":
            result = lru_cache.get(val[0])
            # print(f"Get key {val[0]}, returned value: {result}")
if __name__ == "__main__":
    # operations = ["LRUCache", "put", "put", "get", "get"]
    # values = [[2], [1, 1], [2, 2], [1], [2]]
    run_operations(operations, values)




    # lRUCache = LRUCache(1)
    # lRUCache.put(2, 1) # cache is {2=1}
    # print(lRUCache.get(2)) # returns 1
    # lRUCache.put(3, 2) # LRU key was 2, evicts key 2, cache is {3=2}
    # print(lRUCache.get(2)) # returns -1 (not found)
    # print(lRUCache.get(3)) # returns 2