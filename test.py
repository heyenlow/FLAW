import numpy as np
import tensorflow as tf
import nltk as nltk
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
        for word in sent.split():
            if word in words:
                words[word] = words[word] + 1 
            else:
                words[word] = 1
    return words


#puts all sentences into a list
#assuming test is only sentences that end in periods
def extract_sentences(file_name):
    stopWords = ['is', 'and']
    textFile = open(file_name, "r")
    textTest = textFile.read().lower()
    cleanText = remove_stop_words(textTest, stopWords)
    l = []
    for sentences in re.split("\s*\.\s*", cleanText):
        l.append(sentences)        
    return l

#sents = list of sentences
#stop_words = list of stop words
def remove_stop_words(sents, stop_words):
    for word in stop_words:
        sents = re.sub("\s*\\b" + word + "\\b", '', sents)
    return sents


def print_Sentences(sents):
    count = 0
    for sent in sents:
        print(f"{count} : {sent}")
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


wordCount = count_words(extract_sentences("inputTest.txt"))
sentences = extract_sentences("inputTest.txt")
weight = weight_Dict(wordCount)
print("----SENTENCES----")
print_Sentences(sentences)
print("----WORD COUNT----")
print_Dict(wordCount)
print("----WORD WEIGHTS----")
print_Dict(weight)
#this is a test another




#KERAS

model = Sequential()
model.add(Dense(len(wordCount), input_dim = 8, activation='relu'))