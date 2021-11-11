# See ../doc/sortAllCollections.md for documentation
# Instructions:
# 1. Input the subreddit name on line 18.
# 2. Run program.

import praw
from loginCredentials import client_id_login, client_secret_login, password_login, user_agent_login, username_login

reddit = praw.Reddit(
    client_id = client_id_login,
    client_secret = client_secret_login,
    password = password_login,
    user_agent = user_agent_login,
    username = username_login
)

# Change parameter value to your subreddit name
subreddit = reddit.subreddit("khiphop")

# Reorders all collections in a subreddit
for collection in subreddit.collections:
    current_order = collection.sorted_links # Store current list of posts
    new_order = [] 
    for submission in current_order:
        new_order.append(submission) # Add each post to new list
    new_order.sort(key=lambda x: x.created_utc, reverse=False) # Sort new list by post (aka submission) date
    collection.mod.reorder(new_order) # Apply new order to current order
