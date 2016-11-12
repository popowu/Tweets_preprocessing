# http://bruce3557.logdown.com/posts/291096/jieba-sklearn-calculation-of-chinese-tfidf
import jieba
import sys
import re

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

def del_url(line):

    return re.sub(r'https?:\/\/.*', "", line)

swList = [line.rstrip('\n') for line in open('SmartStoplist.txt')]

corpus = []
contents = ""
with open("excluded_user_out_foodie.txt",'r') as f:
	lines = f.readlines()
	for line in lines:
		temp = line.strip().split('\t')
		if len(temp) == 2: #some lines in file don't have userID
			contents += del_url(str(temp[1]))

corpus.append(contents)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
print (tfidf.shape)

words = vectorizer.get_feature_names()
scores = {}
for i in range(len(corpus)):
	# print ('----Document %d----' % (i))
	for j in range(len(words)):
		if words[j] in swList:
			continue
		# if tfidf[i,j] > 0.002 and tfidf[i,j] < 0.003:
		scores.update({words[j]: tfidf[i,j]})
# print (scores)
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:50]:	
	print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))




# # http://bruce3557.logdown.com/posts/291096/jieba-sklearn-calculation-of-chinese-tfidf
# import jieba
# import sys
# import re

# from sklearn import feature_extraction
# from sklearn.feature_extraction.text import TfidfVectorizer

# swList = [line.rstrip('\n') for line in open('SmartStoplist.txt')]

# corpus = []
# contents = ''
# userIDList = ['2888045174']
# with open("excluded_user_out_foodie.txt",'r') as f:
# 	lines = f.readlines()
# 	for line in lines:
# 		# print (line)
# 		temp = line.strip().split('\t')
# 		if temp[0] in userIDList:
# 			contents += re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', temp[1])

# corpus.append(contents)

# vectorizer = TfidfVectorizer()
# tfidf = vectorizer.fit_transform(corpus)
# print (tfidf.shape)

# words = vectorizer.get_feature_names()
# scores = {}
# for i in range(len(corpus)):
# 	# print ('----Document %d----' % (i))
# 	for j in range(len(words)):
# 		if words[j] in swList:
# 			continue
# 		# if tfidf[i,j] > 0.002 and tfidf[i,j] < 0.003:
# 		scores.update({words[j]: tfidf[i,j]})
# # print (scores)
# sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# for word, score in sorted_words[:30]:
#     print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))