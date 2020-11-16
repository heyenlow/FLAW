import numpy as np
import tensorflow as tf
import nltk as nltk
from tensorflow import keras
from tensorflow.keras import layers


print(np.version)
print(tf.version)

textFile = open("inputTest.txt", "r")
textTest = textFile.read()


#creates a dictionary of words and the number of their occurances
def count_words(text):
    words = {"test" : 0}
    for word in text.split():
        if word in words:
            words[word] = words[word] + 1 
        else:
            words[word] = 1
    return words

def print_Dict(dictionary):
    for word in dictionary:
        print(word + dictionary[word])
    return

print(print_Dict(count_words(textTest)))

#this is a test another