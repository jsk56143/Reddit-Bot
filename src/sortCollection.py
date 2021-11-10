import praw
from loginCredentials import client_id_login, client_secret_login, password_login, user_agent_login, username_login

reddit = praw.Reddit(
    client_id = client_id_login,
    client_secret = client_secret_login,
    password = password_login,
    user_agent = user_agent_login,
    username = username_login
)

subreddit = reddit.subreddit("khiphop")

# Sort collections chronologically (oldest to newest)
# Input collection UUID and then run program
collection = subreddit.collections("b1c98d3c-723c-408d-bbff-a33ee7d5ddb9")
current_order = collection.sorted_links
new_order = []
for submission in current_order:
    new_order.append(submission)
new_order.sort(key=lambda x: x.created_utc, reverse=False)
collection.mod.reorder(new_order)
