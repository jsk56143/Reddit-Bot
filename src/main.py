# See ../doc/main.md for documentation
# Instructions:
# 1. Input the subreddit name without "r/" on line 18.
# 2. Run program.

import praw
import os
import json
from datetime import datetime
from constants import *

reddit = praw.Reddit(
    client_id = os.environ['reddit_client_id'],
    client_secret = os.environ['reddit_secret_login'],
    password = os.environ['reddit_password'],
    user_agent = os.environ['reddit_user_agent'],
    username = os.environ['reddit_username']
)

# Input subreddit name
subreddit = reddit.subreddit("khiphop")

# HELPER FUNCTIONS
# Format removal reason message
def formatRemovalReason(author, body):
    return header.format(author) + body + footer
    

# TEASER POST FLAIR
def replyToTeaserPost(submission):
    comment = submission.reply(teaserComment)
    comment.mod.distinguish(how='yes', sticky=True)
    submission.mod.approve()

# TODO: Need to also test with gallery posts
def addToArtCollection(submission):
    if "i.redd.it" in submission.url:
        with open('database.json', 'r') as openFile: # Read access
            json_object = json.load(openFile)
        current_uuid = json_object["collection"]["teaser_promo_art"].get("uuid")
        collection = subreddit.collections(current_uuid)
        if len(collection) < 100:
            collection.mod.add_post(submission)
        else:
            current_year = datetime.now().strftime("%Y")
            new_part_number = 0

            if current_year in collection.title:
                new_part_number = int(json_object["collection"]["teaser_promo_art"].get("part_number")) + 1
            else:
                new_part_number = 1
            
            title = "Promotional & Teaser Art - " + current_year + " (Part " + new_part_number + ")"
            description = "Welcome to the virtual gallery of promotional & teaser art in " + current_year + "."
            new_collection = subreddit.collections.mod.create(title, description)
            new_uuid = new_collection.collection_id

            json_object['collection']["teaser_promo_art"]["uuid"] = new_uuid
            json_object['collection']["teaser_promo_art"]["part_number"] = new_part_number
            with open('database.json', 'w') as openFile: # Write access
                openFile.write(json.dumps(json_object, indent=4, sort_keys=True)) # Pretty Print, Ensures JSON doesn't output to only one line 


# DISCUSSION POST FLAIR
def checkPostBodyLength(submission):
    if submission.is_self and len(submission.selftext) < 450:
        comment = submission.reply(formatRemovalReason(submission.author, discussionComment))
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove(mod_note="Body too short")


# VARIETY POST FLAIR
def checkLangAtEnd(submission):
    title = submission.title
    if not("[ENG]" in title or "[ENG SUB]" in title or "[RAW]" in title):
        comment = submission.reply(formatRemovalReason(submission.author, varietyComment))
        comment.mod.distinguish(how='yes', sticky=True) 
        submission.mod.remove()


# MUSIC POST FLAIR
def checkMusicPost(submission):
    removalReason = ""
    if submission.is_self or "i.redd.it" in submission.url or "v.redd.it" in submission.url:
        removalReason += musicComment_NotALinkPost
    if " - " not in submission.title:
        removalReason += musicComment_BrokeTitleFormat
    if len(removalReason) != 0:
        comment = submission.reply(formatRemovalReason(submission.author, removalReason))
        comment.mod.distinguish(how='yes', sticky=True)
        submission.mod.remove()

# Auto-moderate the stream
for submission in subreddit.stream.submissions(skip_existing=True):
    if submission.link_flair_text == "Teaser":
        replyToTeaserPost(submission)
        #addToArtCollection(submission)
    elif submission.link_flair_text == "Discussion":
        checkPostBodyLength(submission)
    elif submission.link_flair_text == "Variety":
        checkLangAtEnd(submission)
    elif submission.link_flair_text == "Music Video" or submission.link_flair_text == "Audio" or submission.link_flair_text == "Live" or submission.link_flair_text == "Album":
        checkMusicPost(submission)
