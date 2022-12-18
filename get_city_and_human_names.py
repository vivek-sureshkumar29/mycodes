#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code that can extract city names and human names from a sentence.


# In[2]:


import nltk

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree



def get_human_names(text):
    text = text.title()
    
    nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
    for nltk_result in nltk_results:
        if type(nltk_result) == Tree:
            name = ''
            for nltk_result_leaf in nltk_result.leaves():
                name += nltk_result_leaf[0] + ' '
            name = name.strip()
            return name


# In[3]:


name = get_human_names("My name is Sam")
print (name)


# In[6]:


city = get_human_names("I live in Mumbai")
print (city)


# In[ ]:




