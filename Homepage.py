import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="",
)

st.sidebar.success("Select a page above.")

#st.image("https://raw.github.iu.edu/bjdugan/FA23-NLP/main/McDonald's_SVG_logo.svg?token=GHSAT0AAAAAAAAAU2AJ4W4ZYHZXHRASTLDGZL6KMMQ")
st.image("https://raw.githubusercontent.com/bjdugan/FA23-NLP/main/McDonald's_SVG_logo.svg")
st.write("""
# I'm Loving It? Sentiment analysis of McDonald's customer reviews

Our goal is to be able to create and display sentiment
for McDonald's locations based on customer feedback left through over Google 30,000 
[reviews](https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews). 

Understanding customer sentiment can be crucial to business decisions. While customers provide ratings (:star:), 
they also provide a large body of qualitative feedback that can be difficult to assess at scale. 
Using NLP [methods](https://raw.github.iu.edu/bjdugan/FA23-NLP/main/clean.ipynb?token=GHSAT0AAAAAAAAAU2AJOOSI2TDNUPHQARHOZL6KPFA),
 sentiments ("positive" or "negative") predicted from text reviews as well as polarity scores and direct ratings :star: allow further
insight into customers' attitudes that can help identify low-performing stores for intervention or high-performing stores to model after.
""")
st.write('---')

st.write("""
##  Reviews Visualization
Barplots explore customer review sentiments. 
""")
st.write('---')

st.write("""
##  Map
Mapping customer sentiment.
""")

st.write('---')

st.write("""
    Note: text data have been cleaned but may contain offensive words.
    \nIU Fall 2023 DSCI-D590 Natural Language Processing
    \nGroup 10: Olga Vyrvich, Jill Henry, Brendan Dugan
"""
)
