# khiphop-bot

## Description

* This project is a collection of scripts that better the state of the [r/khiphop](https://www.reddit.com/r/khiphop/) subreddit, which represents Korean Hip-Hop and R&B.

## Pre-Reqs
You'll need the following tools:
* Code editor or IDE (I recommend VS Code)
* Python 3.6+ ([Install here](https://www.python.org/downloads/))
* PRAW ([Install/Update here](https://praw.readthedocs.io/en/stable/getting_started/installation.html))
    * PRAW supports Python 3.6+.

## How to use (for future, if this becomes open source)

1. Clone the repository.
2. In the src/loginCredentials.py file, input the login credentials inside the quotation marks.
    * You can find the **client_id** and **client_secret** [here](https://www.reddit.com/prefs/apps). If you don't see a section called "developed applications", then you'll need to register for an account via the "are you a developer? create an app..." button.
    * **Username** and **password** is self-explanatory.
    * **User_agent** is basically a string of text that's sent with HTTP requests to identify the program making the request. In layman's terms, just enter the name of your program. For example, mine could be called "khiphop-bot".
3. Look for a script you want to use in the doc (documentation) directory. The corresponding source code is available in the src (source code) directory with the same filename. 


