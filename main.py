import re
import praw
import time
import threading
reddit = praw.Reddit(
    client_id='zRFmLVVtIrtotSAiwLQU0Q',
    client_secret='KQQgQEj87V7t4u4Ob9FYTscq1BdL6w',
    user_agent='Kerbal_Bot',
    username='Kerbal_Bot',
    password='pVzNkPER9JmFYAf' #TODO: Change bot username and remove password from code
)

subreddit = reddit.subreddit('bot_playground') #TODO: move to env file


# Keyword to look for in comments
comment_keyword = '!hello'

def handle_comment(comment):
    if comment_keyword in comment.body:
        try:
            reply_text = f"Hii {comment.author.name}"
            comment.reply(reply_text)
            print(f"Replied to comment from {comment.author.name}")
        except Exception as e:
            print(str(e))
            time.sleep(10)

def handle_submission(submission):
    try:
        title_upper = submission.title.upper()
        self_text_upper = submission.selftext.upper()
        reply_text = f"Title: {title_upper}\n\nContent: {self_text_upper}"
        submission.reply(reply_text)
        print(f"Replied to submission {submission.id}")
    except Exception as e:
        print(str(e))
        time.sleep(10)

def comment_stream():
    for comment in subreddit.stream.comments(skip_existing=True):
        handle_comment(comment)

def submission_stream():
    for submission in subreddit.stream.submissions(skip_existing=True):
        handle_submission(submission)

if __name__ == '__main__':
    comment_thread = threading.Thread(target=comment_stream)
    submission_thread = threading.Thread(target=submission_stream)

    comment_thread.start()
    submission_thread.start()