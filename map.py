# NLP streamlit
import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data as vega_data
import altair as alt
# to handle >5000 rows
alt.data_transformers.enable("vegafusion")
usa = alt.topo_feature(vega_data.us_10m.url, "states")

# note: must chnange to current directory to run locally, e.g
# cd "c:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/"
# streamlit run "c:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/map_wdcld.py"

# see https://docs.streamlit.io/library/get-started/create-an-app#lets-put-it-all-together

# point this to github "https://github.iu.edu/bjdugan/FA23-NLP/blob/main/mcdonalds_reviews.csv"
# though it fails with error "C error: Expected 1 fields in line 100, saw 3" delimiter issue? guessing type issue?
data = pd.read_csv("C:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/mcdonalds_reviews.csv", 
                   delimiter=",")

state_selected = st.radio("Pick a state (refresh to reset):", data.state_abb.unique(), 
                          horizontal = True, index = None)

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

# in encoding can use e.g. x='sum(name)' alt.X('name', aggregate='sum')
map_state = alt.Chart(usa).mark_geoshape(
    stroke = "white",
    fill = "lightgrey"
).transform_lookup(
    lookup = "id", 
    from_ = alt.LookupData(data = d, 
                           key = "state_id", 
                           fields = np.array(d.columns))
).encode().project(
    type = "albersUsa"
).properties(
    height = 600,
    width = 600,
    title = "title"
)

if (state_selected) == None:
    group_var = "state_abb"
else:
    group_var = "store_id"

map_sent = alt.Chart(d).transform_aggregate(
    latitude = "mean(latitude)",
    longitude = "mean(longitude)",
    positive_reviews = "sum(sentiment_num)",
    total_reviews = "count()",
    avg_sentiment = "mean(sentiment_num)",
    avg_polarity = "mean(polarity)",
    groupby = ["state_abb"]
).mark_circle().encode(
    latitude = "latitude:Q",
    longitude = "longitude:Q",
    size = "avg_sentiment:Q",
    color = "avg_sentiment:Q",
    tooltip = list(
        ["state_abb:N", 
        "positive_reviews:Q",
        "total_reviews:Q",
        "avg_sentiment:Q",
        "avg_polarity:Q"
    ])
)

plt = map_state + map_sent

st.altair_chart(plt, 
                use_container_width = False,
                theme = "streamlit")

# add store id back to data and then change group_by to store_id if state_selected is not none

# if we want to show dataset with applicable filters
if st.checkbox("Preview data"):
    st.subheader("Raw data")
    st.write(d)
