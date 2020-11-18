import numpy as np
import tensorflow as tf
import nltk as nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import re

print(np.version)
print(tf.version)

#creates a dictionary of words and the number of their occurances
def count_words(sents):
    words = {}
    for sent in sents:
        for word in sent:
            if word in words:
                words[word] = words[word] + 1 
            else:
                words[word] = 1
    return words


#puts all sentences into a list
#assuming test is only sentences that end in periods
def extract_sentences(file_name):
    stop_words = set(stopwords.words('english'))
    textFile = open(file_name, "r")
    sentList = [word_tokenize(sent) for sent in sent_tokenize(textFile.read().lower())]

    l = []
    for sent in sentList:
        sl = []
        for word in sent:
            if word not in stop_words and word not in string.punctuation:
                sl.append(word)
        l.append(sl)

    return l

#sents = list of sentences
#stop_words = list of stop words
    
def print_Sentences(sents):
    count = 0
    s = ' '
    for sent in sents:
        print(f"{count} : {s.join(sent)}")
        count += 1
    return

def print_Dict(dictionary):
    for word in sorted (dictionary):
        print(f"{word:<15} {dictionary[word]}")
    return


def weight_Dict(dictionaryOfOccurences):
    weights = {}
    max = -1
    for word in dictionaryOfOccurences:
        if dictionaryOfOccurences[word] > max:
            max = dictionaryOfOccurences[word]

    for word in dictionaryOfOccurences:
        weights[word] = dictionaryOfOccurences[word] / max

    return weights

sentences = extract_sentences("longTextTest.txt")
wordCount = count_words(sentences)
weight = weight_Dict(wordCount)
print("----SENTENCES----")
print_Sentences(sentences)
print("----WORD COUNT----")
print_Dict(wordCount)
print("----WORD WEIGHTS----")
print_Dict(weight)
#this is a test another
