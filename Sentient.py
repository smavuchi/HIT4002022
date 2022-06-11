from tkinter import *
import numpy as np
import tweepy
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
import re
plt.style.use('fivethirtyeight')

root = Tk()
root.title(' Sentient ') #Title


width=1000
hight=900

root.geometry(f"{width}x{hight}")
root.minsize(width,hight) # minimum size
root.maxsize(width,hight)



banner = Frame(root,padx=15,pady=14, bg="red")
banner.pack()

heding = Label(banner, text="Sentient", font="comicsansms 20 bold")
heding.pack()



#section where we input information to be analysed
input_frame = Frame(root,padx=0,pady=30)
input_frame.pack(anchor="w")

input_frame1 = Frame(root,padx=0,pady=0, bg="yellow")
input_frame1.pack()

username = Label(input_frame, text=" UserID without @ :- ",justify=LEFT,font="comicsansms 10 bold", padx=30)
username.grid(row=2, column=1)

user_value = StringVar()
hash_value = StringVar()

userinput = Entry(input_frame, textvariable=user_value)
userinput.grid(row=2, column=2)

blank2 = Label(input_frame, text="OR")
blank2.grid(row=3, column=3)

hashtag = Label(input_frame, text="Enter Hash Tag with # :- ",font="comicsansms 10 bold", padx=30)
hashtag.grid(row=4, column=1)

hashinput = Entry(input_frame, textvariable=hash_value)
hashinput.grid(row=4, column=2)
#================User Input Part End ===================#

#section where twitter sentiment gui is shown
f1 = Frame(root,padx=15,pady=14)
f1.pack()

f2 = Frame(root,padx=15,pady=14)
f2.pack(anchor="w")
error = Label(f1, text="Please enter any one", fg="red")
error2 = Label(f1, text="Both entry not valid", fg="red")

#================Sentiment Part End===================#

hp = Label(f2, text="Happy:-",padx=15)
un = Label(f2, text="Unhappy:-",pady=5,padx=15)
im = Label(f2, text="Impartial:-",padx=15)
vw = Label(f2, text="Tweets:-",pady=50,padx=50)


def click(hp=None, un=None, im=None,tx=None):
    user_name = user_value.get()
    hash_name = hash_value.get()
    
    #the section where i put my details for my twitter development account tokens
    consumerKey = "vSLVsqIWRy1cSxTp1WrzmFYPf"
    consumerSecret = "K5sOHA8LYhj0qa2yNyAUSbsvQwoIRZtihEzTrJeqr90w77PJZo"
    accessToken = "1482408067023384576-TFvmlyttPmqiP23Nxm4sH9DQBtcdxd"
    accessTokenSecret = "xHcOnrPGllek92APLxB7xCKgxAlFfWCTlsr12UxtoQJHe"
    #============================End twitter API keys section===========================
    
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit = True) # api object
    
    if user_name == "" and hash_name == "":
        error.grid()
    elif hash_name == "":
        error.grid_remove()
        global number
        if number > 1:
            hp.grid_remove()
            un.grid_remove()
            im.grid_remove()

        
        post = api.user_timeline(screen_name=user_name, count = 1500, lang ="en", tweet_mode="extended")
        twitter = pd.DataFrame([tweet.full_text for tweet in post], columns=['Tweets'])
        def cleanTxt(text):
            text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
            text = re.sub('#', '', text) # Removing '#' hash tag
            text = re.sub('RT[\s]+', '', text) # Removing RT
            text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
            return text
        twitter['Tweets'] = twitter['Tweets'].apply(cleanTxt)
        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity
        def getPolarity(text):
            return TextBlob(text).sentiment.polarity
        twitter['Subjectivity'] = twitter['Tweets'].apply(getSubjectivity)
        twitter['Polarity'] = twitter['Tweets'].apply(getPolarity)
    #this section get the analysis done by using set limits to categorise the analysis
        def getAnalysis(score):
            if score < 0:
                return 'Unhappy'
            elif score  <= 0.2:
                return 'Impartial'
            else:
                return 'Happy'

        twitter['Analysis'] = twitter['Polarity'].apply(getAnalysis)
        happy = twitter.loc[twitter['Analysis'].str.contains('Happy')]
        unhappy = twitter.loc[twitter['Analysis'].str.contains('Unhappy')]
        impartial = twitter.loc[twitter['Analysis'].str.contains('Impartial')]
        print(twitter)

        
        happy_per = round((happy.shape[0]/twitter.shape[0])*100, 1)
        unhappy_per = round((unhappy.shape[0]/twitter.shape[0])*100, 1)
        impartial_per = round((impartial.shape[0]/twitter.shape[0])*100, 1)
        
        hp = Label(f2, text=f"Happy:- {happy_per}%",padx=15).grid(row=1, column=2)
        un = Label(f2, text=f"Unhappy:- {unhappy_per}%",pady=5,padx=15).grid(row=2, column=2)
        im = Label(f2, text=f"Impartial:- {impartial_per}%",padx=15).grid(row=3, column=2)
        vw = Label(f2, text=f"Tweets:- {twitter['Tweets']}",pady=100,padx=100).grid(row=4,column=2)

        Label(f2, text= f'{twitter}',width=300,height=500,row=4,column=2)

        
        number += 1
        
    elif user_name == "":
        error.grid_remove()
        if number > 1:
            hp.grid_remove()
            un.grid_remove()
            im.grid_remove()
        
        msgs = []
        msg =[]
        for tweet in tweepy.Cursor(api.search_tweets, q=hash_name).items(500):
            msg = [tweet.text] 
            msg = tuple(msg)                    
            msgs.append(msg)
  #this part cleans the scraped data of twitter by remiving information that may hinder analyisis
        def cleanTxt(text):
            text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
            text = re.sub('#', '', text) # Removing '#' hash tag
            text = re.sub('RT[\s]+', '', text) # Removing RT
            text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
            return text
        df = pd.DataFrame(msgs)
        df['Tweets'] = df[0].apply(cleanTxt)
        df.drop(0, axis=1, inplace=True)
        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity
        def getPolarity(text):
            return TextBlob(text).sentiment.polarity
        df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
        df['Polarity'] = df['Tweets'].apply(getPolarity)

        def getAnalysis(score):
            if score < 0:
                return 'Unhappy'
            elif score <= 0.2:
                return 'Impartial'
            else:
                return 'Happy'


        df['Analysis'] = df['Polarity'].apply(getAnalysis)
        happy = df.loc[df['Analysis'].str.contains('Happy')]
        unhappy = df.loc[df['Analysis'].str.contains('Unhappy')]
        impartial = df.loc[df['Analysis'].str.contains('Impartial')]
        print(df)

        happy_per = round((happy.shape[0]/df.shape[0])*100, 1)
        unhappy_per = round((unhappy.shape[0]/df.shape[0])*100, 1)
        impartial_per = round((impartial.shape[0]/df.shape[0])*100, 1)

        hp = Label(f2, text=f"Happy:- {happy_per}%", padx=15).grid(row=1, column=2)
        un = Label(f2, text=f"Unhappy:- {unhappy_per}%", pady=5, padx=15).grid(row=2, column=2)
        im = Label(f2, text=f"Impartial:- {impartial_per}%", padx=15).grid(row=3, column=2)
        vw = Label(f2, text=f"Tweets:- {df['Tweets']}", pady=100, padx=100).grid(row=4, column=2)

    else:
        error2.grid()

number=0
button = Button(input_frame1,text="Get Analysis", command=click, fg="blue",height = 1, width = 15)
button.grid(row=1, column=1)

root.mainloop()
