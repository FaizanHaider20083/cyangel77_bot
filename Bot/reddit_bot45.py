import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "fromaddr"

toaddr = "toaddr"

reddit = praw.Reddit(client_id = 'dZgHviGKVAV2Kw',
client_secret = '7HQadaouf7W428xNwHCjY26cbVQASw',
user_agent = 'console: message_bot 1.0',
username = 'Standard_Simp8640',
password = 'jackson_hugh11')

message = "Hey, I saw your post and I just wanted to invite you to our group on FB where we are about to give a shit ton of expert relationship and breakup advice. We also host Q/A every week! We are copy-pasting this message to you but we did read your post and think you can get a lot out of this. If you reply back, I’ll personally message you back! let me know if you want the link to it :)"

keywords = ['Help','Advice',"I don't know",'Idk','what to do','what should','anger','angry','guilt','Guilty','Fear','afraid','gaslight','gaslighting','emotional','manipulated','manipulation','narc','narcissist','codependent','codependency']

def check_author(author):
    
    file_read = open("comment_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if author in line:
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0
count = 0
i = 50

subreddits = ['relationship_advice','relationships','BreakUp','BreakUps','ExNoContact']
inbox_keywords = ['yes','yeah','sure','alright','Yes','Yeah','Sure','Alright']


while (i >0):
    for topic in subreddits:
        print("Searching through subreddits")
        subreddit = reddit.subreddit(topic)
        for submission in subreddit.new(limit = 10):
            author = str(submission.author)
            check = check_author(author)
            if check == 0:
                submission_text = str(submission.selftext)
                try:
                    for keyword in keywords:
                        if keyword in submission_text:
                            check2 = check_author(author)
                            if check2 == 0:
                                reddit.redditor(author).message('Relationship Advice', message)
                                print(author)
                                print("Message sent")
                                    
                                message_list = open("comment_list.txt",'a+')
                                message_list.write('\n' + author)
                                message_list.close()
                                links = open("links.txt","a+")
                                links.write('\n' + submission.url)
                                links.write('\n' + 'Message sent to' + author)
                                links.write('\n' + '****************************' + '\n')
                                links.close()
                            continue
                except praw.exceptions.APIException as e:
                    if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                        print("Lol this user has a whitelist, there is no way to message them, giving up")
    time.sleep(600)
    count += 1
    if count%100 == 0:
        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Subreddits links"

        # string to store the body of the mail
        body = "Links of the submissions the bot sent a message to"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "links.txt"
        attachment = open("links.txt", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, 'password')

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()




    
        



