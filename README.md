# Tweet-sentiment-extraction
# Problem statement 
 Twitter Sentiment Extraction with Machine Learning
# Introduction
In recent years, a huge number of people have been attracted to social media platforms like Twitter, Facebook, Instagram etc. People use social sites to express their emotions, beliefs or opinions about things, places or personalities. It's not only people expressing their views, but social media has evolved to a greater dimension where brands, politicians, journalists, influencers all co-exists together with different agendas like promoting products/ideologies, entertaining people, demanding justice and whatnot.

As the title suggests in this project we are going to do Tweet Sentiment Extraction. It is the process of 'computationally' determining whether a piece of writing is positive, negative or neutral. It's also known as opinion mining, deriving the opinion or attitude of a speaker. 

We will use Natural Language Processing (NLP) to make sense of human language, and machine learning to automatically deliver accurate results.
Before that it’s important to go through some terms:

Stemming: Stemming is the process of reducing inflection in words to their root forms such as mapping a group of words to the same stem even if the stem itself is not a valid word in the Language.

Lemmatization: Lemmatization, unlike Stemming, reduces the inflected words properly ensuring that the root word belongs to the language. In Lemmatization root word is called Lemma. A lemma (plural lemmas or lemmata) is the canonical form, dictionary form, or citation form of a set of words.

# Scope
In the times where hate across social media platforms has visibly increased and triggered debates on mental health, we believe such an analysis will allow people to recognize whether the tweets on an account are on the negative or positive side. Thus, negative tweets with foul language/message can be hidden from a group of people below certain age or it can help brands to study their audience.

# Approach
•	Dataset
https://www.kaggle.com/c/tweet-sentiment-extraction/data

•	Data Visualization
We add a column to our data frame called ‘text length’ that contains the length of the tweet. We do this to see if there is relationship or a pattern between the sentiment and length of the tweet.

•	Data Transforming
Simply there are three steps our data will be going through:
1)	Count Vectorizer: converts data into bag of words with user defined analyzer called smooth.
This analyzer removes urls, punctuation, stop words, lemmatizes words, stems the words and then returns the result.
2)	Tf-Idf transformer: defines how important a word is.
3)	Classifier: classifies the class of tweet (Positive, Negative, Neutral.)\
   •	The main algorithms that have been used here for classification, supervised learning are:\
     o	Logistic Regression\
     o	Support Vector Classifier\
     o	Random Forest Classifier\
    Others like Gradient Boosting Classifier and Bagging Classifier were also used but their performance scores were much lesser than the algorithms mentioned above even after       tuning their hyperparameters, hence, they are not shown in the code.

# Output
1)	Logistic Regression\
•	Score: 0.691

![](Output%20images/LR.png)

2)	Support Vector Classifier\
•	Score: 0.694

![](Output%20images/SVM.png)

3)	Random Forest Classifier\
•	Score: 0.71

![](Output%20images/RFC.png)

# Conclusion
The three different classifiers give three different scores but Random Forest Classifier gives the highest with higher precision and recall as well.
