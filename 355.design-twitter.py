#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
import heapq
class Twitter:

    def __init__(self):
        self.follow_dic = {}
        self.twitts_dic = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitts_dic:
            self.twitts_dic[userId] = [(self.time, tweetId)]
        else:
            self.twitts_dic[userId].append((self.time, tweetId))

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        # initiate max_heap
        if userId not in self.follow_dic:
            self.follow_dic[userId] = {userId}
        for followeeId in self.follow_dic[userId]:
            if followeeId in self.twitts_dic:
                # print(self.twitts_dic[followeeId][-1][0], self.twitts_dic[followeeId][-1][1], followeeId, -1)
                heapq.heappush(max_heap, (-self.twitts_dic[followeeId][-1][0], self.twitts_dic[followeeId][-1][1], followeeId, -1))
        
        newsFeed = []
        while len(newsFeed) < 10 and max_heap:
            time, tweetId, followeeId, i  = heapq.heappop(max_heap)

            newsFeed.append(tweetId)
            if i - 1 >= -len(self.twitts_dic[followeeId]):
                heapq.heappush(max_heap, (-self.twitts_dic[followeeId][i - 1][0], self.twitts_dic[followeeId][i - 1][1], followeeId, i - 1))

        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_dic:
            self.follow_dic[followerId] = {followerId, followeeId}
        else:
            self.follow_dic[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_dic and followeeId in self.follow_dic[followerId]:
            self.follow_dic[followerId].remove(followeeId)
# @lc code=end

