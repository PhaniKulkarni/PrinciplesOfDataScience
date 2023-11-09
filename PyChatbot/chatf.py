import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# In[3]:


class QASystem:


    def __init__(self, filepath):
        self.df = pd.read_csv(filepath, delimiter=';')
        self.questions_list = self.df['Query'].tolist()
        self.answers_list = self.df['Response'].tolist()

        self.vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)

        self.X = self.vectorizer.fit_transform([self.preprocess(q) for q in self.questions_list])


    def preprocess(self, text):
        lemmatizer = WordNetLemmatizer()
        stemmer = PorterStemmer()
        text = re.sub(r'[^\w\s]', '', text)

        tokens = nltk.word_tokenize(text.lower())
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        #stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]

        return ' '.join(lemmatized_tokens)

    def get_response(self, text):
        print("text:",text)
        processed_text = self.preprocess(text)
        vectorized_text = self.vectorizer.transform([processed_text])
        similarities = cosine_similarity(vectorized_text, self.X)
        max_similarity = np.max(similarities)
        print(max_similarity)
        if max_similarity >= 0.6:  # You can use your threshold value here
            max_similar_question_index = np.argmax(similarities)
            response = self.answers_list[max_similar_question_index]
            return response
        else:
            response = "Your query seems to be incomplete. Please provide more details"
            return response







