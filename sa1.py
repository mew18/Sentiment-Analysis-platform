#reads data from twitter and performs sentiment analysis

import matplotlib.pyplot as plt
from textblob import TextBlob
import tweepy,numpy,re
import csv
import subprocess
import pandas as pd

consumer_key="LkBC7XiNG7wlzN8ZqEO5QiDQX"
consumer_secret="nsJsMWHWDdiWmCV6VIJOExxzVA4mqzORzDGOqlrbVCDoIqHByj"
access_token="1017815862676344832-Jsv6ye6Xhsc8yDtpbBjz4uYogcSNCp"
access_token_secret="Ot4ALAymmsi4atUft3fyCww0MuDUqaQ4F244a3Qys7hgc"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

phrase=input('Enter a hastag or a term you would like to search on Twitter  : ')
n=int(input('How many tweets would you like to analyze  : '))

tweets=tweepy.Cursor(api.search, q=phrase,lang='en').items(n)

tweets_as_text=[]
# tweet_csv=open('rj_tweets_csv.csv','a')
# writer=csv.writer(tweet_csv)

def percentage(part,whole):
    per=100 * float(part) / float(whole)
    return format(per,'.2f')

def tweet_as_token(tweet_ip):
    return ' '.join(    re.sub(  "( @[A-Za-z0-9]+ ) | ( [^0-9A-Za-z \t] ) | ( \w +:\ / \ / \S + )", " ",tweet_ip).split()  )

vpositive=0
positive=0
lpositive=0
vnegative=0
negative=0
lnegative=0
neutral=0
polarity=0

for t in tweets:
    # print(t.text)
    # tweets_as_text.append(tweet_as_token(t.text).encode('utf-8'))
    analysis =TextBlob(t.text)
    # print(analysis.sentiment)
    polarity=polarity+analysis.sentiment.polarity

    if(analysis.sentiment.polarity==0):
        neutral=neutral+1
    elif(analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <=1):
        vpositive=vpositive+1
    elif(analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <=0.6):
        positive=positive+1
    elif(analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <=0.3):
        lpositive=lpositive+1
    elif(analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <=0):
        lnegative=lnegative+1
    elif(analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <=-0.3):
        negative=negative+1
    elif(analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <=-0.6):
        vnegative=vnegative+1

# writer.writerow(tweets_as_text)
# tweet_csv.close()

vpositive=percentage(vpositive,n)
positive=percentage(positive,n)
lpositive=percentage(lpositive,n)
vnegative=percentage(vnegative,n)
negative=percentage(negative,n)
lnegative=percentage(lnegative,n)
neutral=percentage(neutral,n)

avgpolarity=polarity/n  

print("How many people are reacting on : " + phrase + " by analyzing : " + str(n) + " Tweets ")
print('\n')
print(' BRIEF REPORT : ')
# may be remove this code
if(avgpolarity==0):
    print('Neutral')
elif(avgpolarity>0.6 and avgpolarity <=1):
    print('Glad')
elif(avgpolarity>0.3 and avgpolarity <=0.6):
    print('Positive')
elif(avgpolarity>0 and avgpolarity <=0.3):
    print('Optimistic')
elif(avgpolarity>-0.3 and avgpolarity <=0):
    print('Pessimistic')
elif(avgpolarity>-0.6 and avgpolarity <= -0.3):
    print('Negative')
elif(avgpolarity>-1 and avgpolarity <=-0.6):
    print('Annoyed')

print('\n')
print('DETAILED REPORT : ')
print(str(vpositive) +"% people were glad" )
print(str(positive) +"% people were positive" )
print(str(lpositive) +"% people were optimistic" )
print(str(neutral)+ "% people were neutral")
print(str(lnegative) +"% people were pessimistic" )
print(str(negative) +"% people were negative" )
print(str(vnegative) +"% people were annoyed" )

labels=['Glad [' + str(vpositive)+'%]','Positive ['+ str(positive)+' % ]' ,'Optimistic [' + str(lpositive)+'%]', 'Neutral ['+ str(neutral) + ' % ]','Pessimistic [' + str(lnegative)+' % ]', 'Negative [' + str(negative) +' %]','Annoyed ['+ str(vnegative) +' % ]' ]
sizes=[vpositive,positive,lpositive,neutral,lnegative,negative,vnegative]
colors=['darkblue','blue','lightblue','grey','silver','white']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("How many people are reacting on : " + phrase + " by analyzing : " + str(n) + " Tweets ")
plt.axis('equal')
plt.tight_layout()
plt.show()

ans=input(' Do you wish to see the tweets ? ')

if(ans=='y' or ans=='Y' or ans=='yes' or ans=='Yes'):
    print('if statement works but tweets dont show up')
    # with open('rj_tweets_csv.csv', 'r') as csvFile:
    #     reader = csv.reader(csvFile)
    #     for row in reader:
    #         print(row)
    # csvFile.close() do something about this escape character
    # df=pd.read_csv("C:\Users\MR_ME\rj_tweets_csv.csv")
    


# input('Press ENTER to exit')
