import praw

reddit = praw.Reddit("bot1")

for comment in reddit.redditor("<redditor>").comments.new(limit=None):
    # print(comment.body.split("\n", 1)[0][:79])
    print(comment.body)