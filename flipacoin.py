import praw
import random
import time


r = praw.Reddit(user_agent="Flip A Coin")
r.login()
print("Logged in")

match_words = ["can't decide","cant decide","must decide","need to decide"]
checkedComments = []


#run the bot
def run():
	#define the subreddit that you want to scan. For our purposes, we will use /r/test
    subreddit = r.get_subreddit("test")
    print("pulled subreddit")
    #pull comments. Here we pull 30 comments at a time
    comments = subreddit.get_comments(limit=30)
    print("pulled comments")
    #start scanning individual comments that we pulled
    print("starting loop")
    for comment in comments:
        #store the body of the comment in variable body
        body = comment.body.lower()
        #check for a match
        isMatch = any(string in body for string in match_words)
        if isMatch:
            print("match found! Comment ID =" + comment.id)
        else:
            print("no matches :c")
        if comment.id not in checkedComments and isMatch:
            print("in the loop")
            if random.randrange(1,10,1) > 5:
                coin = "heads"
            else:
                coin = "tails"
            print("coin flipped")
            comment.reply("Can't decide? Flip a coin! Choose what heads and tails are: \n\n\n\n\n" + "...." + "\n\n\n\n" + "Your coin landed on " + coin + "!")
            print("succesful reply")
            checkedComments.append(comment.id)
            print("comment ID appended to storage")
    print("loop finished..sleeping")


while True:
    run()
    time.sleep(10)
