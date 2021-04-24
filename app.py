#!/usr/bin/env python
# coding: utf-8
### developed by sai
### connect sairamdgr8@gmail.com
# In[1]:


#!pip install gradio


# In[2]:


import gradio as gr
from textblob import TextBlob


# In[3]:


def greet(Sai_made_Sentimental_Analysis):
    x=TextBlob(Sai_made_Sentimental_Analysis)
    if x.sentiment.polarity>0:
        return "The given tweet looks:positive"
    elif x.sentiment.polarity<0:
        return "The given tweet looks:negative"
    else:
        return "The given tweet looks:neutral"
iface=gr.Interface(fn=greet,inputs="text",outputs="text")
iface.launch()


# In[ ]:




