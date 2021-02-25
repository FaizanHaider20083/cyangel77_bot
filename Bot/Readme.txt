***** Reddit flair bot **********

******* Flares users who have more than 5 comments on a submission in a subreddit.*************

This is the tutorial guide for the Reddit Bot. You need to have python installed to run the bot.

You can install python from www.python.org . Alternative you can use pycharm which works in a similar manner. Download pycharm from www.jetbrains.com/pycharm . 

****** Files in the bot *********

4 Folders named praw. They are represent Python Reddit API Wrapper. They are the engine of the bot. You do not need to make any changes to them. However, changes in the code of those folders can affect the working of the bot, so I advice to leave them alone.

There is a file named Subreddits.txt in the folder. Enter the subreddits that you want the bot to moderate. However keep the format in this manner.

Subreddit1
Subreddit2
SUbreddit3


For eg

Television
Jokes
Coding

If you open the file you will see the subreddit "tes_ting".Obviously it was meant for testing purposes. You can erase the text and write your own subreddits but adhere to the format prescribed above.



The final file is the code for the bot.I have named the bot as reddit_flair_bot. I will explain the code in detail.


The 4th line of the code initiate reddit interaction. The various parameters are technical gibberish that doesn't concern us. But pay close attention to the username and password parameters. These are the credentials that the bot uses. You can change the username and password, but insert them in the respective parameters within the quotations and take due notice of the comma.

The rest of the code is the mechanism to obtain those who have commented more than 5 times. But there is one last thing that interests us. The last line of the code assigns the flair. By default I am assigning the flair "Multiple comments". Change it to whatever you want but again keep in mind the quotations and the commas.


***********P.S - The bot only works with an account that has moderator privileges. This is limited by Reddit's own rules, and nothing can be done about it.************


********* Thank you for hiring me. Hope you are satisfied with my work.***********



