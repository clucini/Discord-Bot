import praw
import random

def get_random(sub,  top):
    red = praw.Reddit(client_id='4RQBZlc44ClWmg',
                        client_secret='8BmDm4ASnR1ymLnF3eJePsI8AFA',
                        user_agent='python:com.example.:v0.0.1 (by /u/spiritonia)')
    if top:
        memes_submissions = red.subreddit(sub).top()
    else:
        memes_submissions = red.subreddit(sub).hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    return submission.url


