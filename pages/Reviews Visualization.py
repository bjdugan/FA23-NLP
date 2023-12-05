

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from nltk.corpus import stopwords
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from nltk.stem import WordNetLemmatizer

st.write("""
# Reviews Visualization 
### Barplots of the dataset features
""")
st.write('---')


def sentiment(rating):
    if rating in ['1 star', '2 stars']:
        return 'negative'
    elif rating == '3 stars':
        return 'neutral'
    else:
        return 'positive'
    

data = pd.read_csv('/Users/olgavyrvich/Macdonalds/McDonald_s_Reviews.csv', encoding='latin1')
data['store_sentiment'] = data['rating'].apply(sentiment)


st.title("Sentiment Analysis Based on Reviews")
if st.checkbox("Show Data"):
    st.write(data.head(50))

sentiment=data['store_sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Reviews':sentiment.values})

fig = px.bar(sentiment, x='Sentiment', y='Reviews', color= 'Reviews',height=500)
st.plotly_chart(fig)


data['state'] = data['store_address'].str.split(', ').str[-2].str.split().str[0]
state_data=data['state'].value_counts()
state_data=pd.DataFrame({'Sentiment':state_data.index,'Reviews':state_data.values})

fig1 = px.bar(state_data, x='Sentiment', y='Reviews', color= 'Reviews',height=500)
st.plotly_chart(fig1)

st.sidebar.subheader("States by sentiment")
choice = st.sidebar.multiselect("States", ('FL ','TX', 'CA', 'NY','NJ','NV','PA','UT','IL','DC','VA'), key = '0')

if len(choice)>0:
    state_data=data[data.state.isin(choice)]
    fig2 = px.histogram(state_data, x='state', y='store_sentiment', histfunc='count', color='store_sentiment',labels={'store_sentiment':'reviews'}, height=600, width=800)
    st.plotly_chart(fig2)




