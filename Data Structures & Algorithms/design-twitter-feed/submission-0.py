class Twitter:

    def __init__(self):
        self.user_ids = 501
        self.idx = 0
        self.matrix = {u_id: deque(maxlen=10) for u_id in range(1, self.user_ids)}
        self.follower = {u_id:{u_id} for u_id in range(1, self.user_ids)}
        # print(matrix)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.matrix[userId].append([self.idx,tweetId])
        self.idx += 1
        # print(userId,":",self.matrix[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        follow_li = list(self.follower[userId])
        news = []
        for f in follow_li:
            news.extend(self.matrix[f])
        news.sort(reverse = True, key=lambda x: x[0])
        return [val for idx,val in news[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        # print('f:',followerId,self.follower[followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
        # print('uf:',followerId,self.follower[followerId])
