import numpy as np
import tensorflow as tf
import nltk as nltk
from tensorflow import keras
from tensorflow.keras import layers
import re


print(np.version)
print(tf.version)




#creates a dictionary of words and the number of their occurances
def count_words(l):
    words = {"------------" : 0}
    for sentence in l:
        for word in sentence.split():
            if word in words:
                words[word] = words[word] + 1 
            else:
                words[word] = 1
    return words


#puts all sentences into a list
#assuming test is only sentences that end in periods
def extract_sentences(file_name):
    textFile = open(file_name, "r")
    textTest = textFile.read()
    l = ['']
    for sentences in re.split("\s*\.\s*", textTest):
        l.append(sentences)        
    return l



def print_Sentences(l):
    count = 0
    for sentences in l:
        print(f"{count} : {sentences}")
        count += 1
    return

def print_Dict(dictionary):
    for word in dictionary:
        print(f"{word:<15} {dictionary[word]}")
    return

print_Dict(count_words(extract_sentences("inputTest.txt")))
print_Sentences(extract_sentences("inputTest.txt"))

#this is a test another