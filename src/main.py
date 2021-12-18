# See ../doc/main.md for documentation
# Instructions:
# 1. Input the subreddit name without "r/" on line 18.
# 2. Run program.

import praw
import os
from constants import teaserComment, discussionComment

reddit = praw.Reddit(
    client_id = os.environ['reddit_client_id'],
    client_secret = os.environ['reddit_client_secret'],
    password = os.environ['reddit_password'],
    user_agent = os.environ['reddit_user_agent'],
    username = os.environ['reddit_username']
)

# Input subreddit name
subreddit = reddit.subreddit("test484")

# Check stream for rule-breaking posts
for submission in subreddit.stream.submissions(skip_existing=True):
    if submission.link_flair_text == "teaser":
        comment = submission.reply(teaserComment)
        comment.mod.distinguish(how='yes', sticky=True)
        submission.mod.approve()
    elif submission.is_self and submission.link_flair_text == "discussion" and len(submission.selftext) < 450:
        comment = submission.reply(discussionComment)
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove(mod_note="Body too short")




