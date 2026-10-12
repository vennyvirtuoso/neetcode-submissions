import heapq
class Twitter:

    def __init__(self):
        self.tweets=dict()
        self.following=dict()
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.time,tweetId))
        else:
            self.tweets[userId]=[(self.time,tweetId)]
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users= self.following.get(userId,set())|{userId}
        heap=[]
        ans=[]
        for uid in users:
            if uid in self.tweets:
                uid_tweets=self.tweets[uid]
                for uid_tweet in reversed(uid_tweets):
                    heapq.heappush(heap,(-uid_tweet[0],uid_tweet[1]))
        for i in range(10):
            if heap:
                tp=heapq.heappop(heap)
                ans.append(tp[1])
        return ans




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId]={followeeId}
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
