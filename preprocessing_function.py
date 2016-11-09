#function to help remove meaninfullless punctuation
import string
def removePun(tweet): 
	for c in string.punctuation:
		tweet= tweet.replace(c,"")
	return tweet
# print (removePun('Hi!!!!!!!'))

# ====================

#Function to help remove stopwords from a piece of text
from nltk.corpus import stopwords

StopWords = stopwords.words("english")
def removeStopWords(tweet):
	final = ' '.join([word for word in tweet.split() if word not in StopWords] )
	return final
# print (removeStopWords('i have a pen !!'))

# ====================

#function to reome hyperlinks(URL)
import re
def removeURL(tweet):
	tweet = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', tweet)
	return tweet
# print (removeURL('i have a pen !!https://www.youtube.com/watch?v=IvqVHybWK8w'))


# ====================

#function to remove # in HashTags and @  
def removeHash(tweet):
	result = ''
	for i in tweet.split(' '):
		if i.startswith('#') or i.startswith('@'): #remove @ amd #
			result += i[1:]
			result += ' '
		else:
			result += i
			result += ' '
	return result
# print (removeHash('i have a #pen.'))

