import numpy as np
import tensorflow as tf
import nltk as nltk
from tensorflow import keras
from tensorflow.keras import layers
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
    textTest = textFile.read()
    cleanText = remove_stop_words(textTest, stopWords)
    l = []
    for sentences in re.split("\s*\.\s*", textTest):
        l.append(sentences)        
    return l

#sents = list of sentences
#stop_words = list of stop words
def remove_stop_words(sents, stop_words):
    for word in stop_words:
        sents = re.sub(f"\s*\b{word}\b", ' ', sents)

    return sents


def print_Sentences(sents):
    count = 0
    for sent in sents:
        print(f"{count} : {sent}")
        count += 1
    return

def print_Dict(dictionary):
    for word in dictionary:
        print(f"{word:<15} {dictionary[word]}")
    return

print_Dict(count_words(extract_sentences("inputTest.txt")))
print_Sentences(extract_sentences("inputTest.txt"))

#this is a test another