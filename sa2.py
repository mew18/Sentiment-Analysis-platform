from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string
import nltk
from nltk.tokenize import word_tokenize,RegexpTokenizer
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
# nltk.download('punkt')
# nltk.download('vader_lexicon')

analyzer=SentimentIntensityAnalyzer()

def sentiment_analyzer_score(text):
    score=analyzer.polarity_scores(text)
    # print(text)
    print(score)

phrase=input('Enter a review ')

sentiment_analyzer_score(phrase)

def get_word_sentiment(text):
    tokenized_text=nltk.word_tokenize(text)
    pos_list=[]
    neu_list=[]
    neg_list=[]

    polarity=0   
    
    freq_dist=FreqDist(tokenized_text)
    print(freq_dist)
    freq_dist.plot(30,cumulative=False)
    plt.show()
    
    for word in tokenized_text:
        polarity=polarity+analyzer.polarity_scores(word)['compound']

        if( analyzer.polarity_scores(word)['compound']   ) >= 0.1:
            pos_list.append(word)    
        elif(analyzer.polarity_scores(word)['compound'])<= -0.1:
            neg_list.append(word)
        else:
            neu_list.append(word)

    if(polarity==0):
        print('The review was mostly neutral')
    elif(polarity>0):
        print('The review was classified as positive')
    elif(polarity<0):
        print('The review was classified as negative')
    
    print('POSITIVE :',pos_list)
    print('NEUTRAL :',neu_list)
    print('NEGATIVE :',neg_list)
            
    def count(list):
        return len(list)
    
    def percentage(len):
        per= 100 * float(len) / float (count(pos_list)+count(neg_list)+count(neu_list))
        return format(per,'.2f')

    pos_per=percentage(count(pos_list))
    neu_per=percentage(count(neu_list))
    neg_per=percentage(count(neg_list))

    print('POSITIVE :',pos_per)
    print('NEUTRAL :',neu_per)
    print('NEGATIVE :',neg_per)

    labels=['POSITIVE [' + str(pos_per)+'%]','NEUTRAL ['+ str(neu_per)+' % ]' ,'NEGATIVE [' + str(neg_per)+'%]']
    sizes=[pos_per,neu_per,neg_per]
    colors=['darkblue','blue','lightblue']
    patches,texts=plt.pie(sizes,colors=colors,startangle=90)
    plt.legend(patches,labels,loc="best")
    plt.title("The review : '" + phrase + "' consists of the following : ")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

       
get_word_sentiment(phrase)

# add: chart for :  freq of each word
