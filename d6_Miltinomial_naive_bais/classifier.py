import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import string
import nltk
from nltk.corpus import stopwords
import Dataset_Generator
from Dataset_Generator import get_topics
import fitz
import os

#pickle is just to save the model
import pickle

nltk.download('stopwords')
vectorizer=CountVectorizer()

def NB_Model_Train(dataset):
    input=dataset['Text']
    output=dataset['Title']
    input=vectorizer.fit_transform(input)
    #print(input)
    nb=MultinomialNB()
    nb.fit(input,output)
    return nb
    
def get_data_set():
    df=pd.read_csv('Dataset_final.csv')
    return df

def get_input_from_pdf():
    path=input('Enter the Path for pdf: ')
    doc=fitz.open(path)
    page=doc[0]
    text=page.get_text()
    translator = str.maketrans('', '', string.punctuation)
    nopunc = text.translate(translator)
    words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    words=' '.join(words)
    return words




if __name__=='__main__':
    print('DOCUMENT CLASSIFIER')
    dataset=get_data_set()
    model=NB_Model_Train(dataset)
    print('Model Training Successful !!')
    #Saving model file somewhere to be used by another file.
    pickle.dump(vectorizer, open('vectorizer.pickle', 'wb'))
    pickle.dump(model,open('Classification.model','wb'))
