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
            if uid in self.tweets and self.tweets[uid]:
                len_tw=len(self.tweets[uid])-1
                tweet_pair=self.tweets[uid][len_tw]
                heapq.heappush(heap,(-tweet_pair[0],tweet_pair[1],uid,len_tw))
        
        while heap and len(ans)<10:
            time,t_id,uid,idx=heapq.heappop(heap)
            ans.append(t_id)

            idx-=1
            if idx>=0:
                time,tweet_id=self.tweets[uid][idx]
                heapq.heappush(heap,(-time,tweet_id,uid,idx))
        return ans






    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId]={followeeId}
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
