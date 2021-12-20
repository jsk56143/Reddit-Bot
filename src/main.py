# See ../doc/main.md for documentation
# Instructions:
# 1. Input the subreddit name without "r/" on line 18.
# 2. Run program.

import praw
import os
from constants import teaserComment, discussionComment, varietyComment, musicComment_BrokeTitleFormat, musicComment_NotALinkPost

reddit = praw.Reddit(
    client_id = os.environ['reddit_client_id'],
    client_secret = os.environ['reddit_secret_login'],
    password = os.environ['reddit_password'],
    user_agent = os.environ['reddit_user_agent'],
    username = os.environ['reddit_username']
)

# Input subreddit name
subreddit = reddit.subreddit("khiphop")

# TEASER
def replyToTeaserPost(submission):
    comment = submission.reply(teaserComment)
    comment.mod.distinguish(how='yes', sticky=True)
    submission.mod.approve()

#def addToArtCollection(submission):
#    if "i.redd.it" in submission.url:
        #add it to current month's collection
            #get collection
            #check if it's full
            #if full, make a new one

#DISCUSSION
def checkPostBodyLength(submission):
    if submission.is_self and len(submission.selftext) < 450:
        comment = submission.reply(discussionComment)
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove(mod_note="Body too short")

#VARIETY
def checkLangAtEnd(submission):
    title = submission.title
    if not("[ENG]" in title or "[ENG SUB]" in title or "[RAW]" in title):
        comment = submission.reply(varietyComment)
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove()

#MUSIC
def checkLinkPost(submission):
    if submission.is_self or "i.redd.it" in submission.url or "v.redd.it" in submission.url:
        comment = submission.reply(musicComment_NotALinkPost)
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove()

def checkDash(submission):
    if " - " not in submission.title:
        comment = submission.reply(musicComment_BrokeTitleFormat)
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove()

# Check stream for rule-breaking posts
for submission in subreddit.stream.submissions(skip_existing=True):
    if submission.link_flair_text == "Teaser":
        replyToTeaserPost(submission)
        #addToArtCollection(submission)
    elif submission.link_flair_text == "Discussion":
        checkPostBodyLength(submission)
    elif submission.link_flair_text == "Variety":
        checkLangAtEnd(submission)
    elif submission.link_flair_text == "Music Video" or submission.link_flair_text == "Audio" or submission.link_flair_text == "Live" or submission.link_flair_text == "Album":
        checkLinkPost(submission)
        checkDash(submission)
