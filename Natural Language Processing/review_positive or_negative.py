# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:42:23 2021

@author: Dhiraj Wagh
"""
#Importing the liabraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset.
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

# Cleaing the tasks.
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review = review.lower()
review = review.split()
ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]

review = ' '.join(review)