import praw


reddit = praw.Reddit(client_id = '4Y-ybqnRtI3Xog',
                     client_secret = 'NzTLmfzHxZjsq-XYHaf_I-ySysjGnw',
                     user_agent = 'console: flairbot 1.0',
                     username = 'outrageous-Pen184',
                     password = '7371+10270')
                     




subreddit_file = open("Subreddits.txt",'r+')
template = "6bd28436-1aa7-11e9-9902-0e05ab0fad46"



for topic in subreddit_file:
        
    subreddit = reddit.subreddit(topic)

    for submission in subreddit.new(limit = 20):
        print ("..........................")
        author_list = []
        flair_author_list = []
        print(submission.title)
        for comment in submission.comments:
            
            if hasattr(comment,"body"):
                author_list.append(comment.author)
                print(comment.author)
                print("...")

            if hasattr(comment,"comments"):
                for morecomments in comment.comments:
                    author_list.append(morecomments.author)
                
                    if hasattr(morecomments,"comments"):
                        for evenmorecomments in comment.comments:
                            author_list.append(evenmorecomments.author)

           
        author_set = set(author_list)
        for i in author_set:
            if author_list.count(i) >= 5 :
                
                flair_author_list.append(i)
        for k in flair_author_list:
            reddit.subreddit(topic).flair.set(k,"Multiple Comments",template)
                            

    
            
