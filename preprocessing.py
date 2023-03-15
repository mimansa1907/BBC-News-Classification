import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
import tensorflow as tf
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pickle

decode_class = {
    1:'business',
    2:'tech',
    3:'politics',
    4:'sport',
    5:'entertainment'
}

stopwordlist = stopwords.words('english')
stopwordlist.extend(['ha','wa','u','said','would','could','should','also'])

# def preprocessText(inputText):
#     # print(type(inputText))
#     try:
#         inputText = inputText.lower()
#         inputText = re.sub(r'[^a-zA-z- ]*',"",inputText)
#         inputText = re.sub(r' [a-zA-Z] ',"",inputText)
#         sent_list = word_tokenize(inputText)
#         list1 = []
#         for i in sent_list:
#             list1.append(WordNetLemmatizer().lemmatize(i))
#     except:
#         return 'None'
#     # print(list1)
#     return len(list1)
#     # return 'done'

def preprocess_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-zA-z- ]*',"",sentence)
    sentence = re.sub(r' [a-zA-Z] ',"",sentence)
    sent_list = word_tokenize(sentence)
    sentence = " ".join([i for i in sent_list if i not in stopwordlist])
    return sentence

def predict_text_class(sentence):
    ### load model
    model = pickle.load(open('lgrmodel.pkl', 'rb'))
    return decode_class[model.predict([preprocess_sentence(sentence)])[0]]
