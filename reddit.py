import praw
import random

def get_random(sub,  top):
    red = praw.Reddit(client_id='4RQBZlc44ClWmg',
                        client_secret='8BmDm4ASnR1ymLnF3eJePsI8AFA',
                        user_agent='python:com.example.:v0.0.1 (by /u/spiritonia)')
    subr = 'None'
    try:
        subr = red.subreddit(sub)
        if top:
            memes_submissions = subr.top()
        else:
            memes_submissions = subr.hot()
        submissions = []
        for subm in memes_submissions:
            if 'imgur' in subm.url and 'jpg' in subm.url or 'png' in subm.url:
                submissions.append(subm)
    except:
            return "error", subr.display_name
    return random.choice(submissions).url, subr.display_name


