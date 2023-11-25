# NLP streamlit
import streamlit as st
import pandas as pd
import numpy as np
import zipfile

# note: must chnange to current directory to run locally, e.g
# cd "c:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/"
# streamlit run app.py

# see https://docs.streamlit.io/library/get-started/create-an-app#lets-put-it-all-together

# point this to github "https://github.iu.edu/bjdugan/FA23-NLP/blob/main/mcdonalds_reviews.csv"
# though it fails with error "C error: Expected 1 fields in line 100, saw 3" delimiter issue? guessing type issue?
data = pd.read_csv("C:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/mcdonalds_reviews.csv", 
                   delimiter=",")

state_selected = st.radio("Pick a state:", data.state_abb.unique(), horizontal = True, index = None)

# use all data unless filtered by state; no filter by default (index=None)
if (state_selected == None):
    d = data
else:
    d = data[data.state_abb == state_selected]

# compare to national averages
# https://docs.streamlit.io/library/api-reference/data/st.metric
c1, c2, c3 = st.columns(3)
c1_delta = d.sentiment_num.mean() - data.sentiment_num.mean()
c2_delta = d.polarity.mean() - data.polarity.mean()
c3_delta = d.rating_num.mean() - data.rating_num.mean()

c1.metric("Average sentiment (0 to 1)", d.sentiment_num.mean().round(2), 
          delta = c1_delta.round(2))
c2.metric("Average polarity (-1 to 1)", d.polarity.mean().round(2),
        delta = c2_delta.round(2))
c3.metric("Average :star:'s", d.rating_num.mean().round(2), 
          delta = c3_delta.round(2))

# cond: if state_selected == None show full data in map, otherwise show d (filtered to state)
# can this have the average sentiment by store? or other features?
# need to clear missing data from lat and lon
st.map(d[["latitude", "longitude", "sentiment_num"]]) 

if st.checkbox("Preview data"):
    st.subheader("Raw data")
    st.write(d)

# wordcloud for state or store? color by pos/neg.
