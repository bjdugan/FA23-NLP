# NLP streamlit
import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data as vega_data
import altair as alt
# to handle >5000 rows
alt.data_transformers.enable("vegafusion")
usa = alt.topo_feature(vega_data.us_10m.url, "states")

# note: might need to chnange to current directory to run locally, e.g
# cd "c:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/"
# streamlit run "c:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/map.py"

# see https://docs.streamlit.io/library/get-started/create-an-app#lets-put-it-all-together

# point this to github "https://github.iu.edu/bjdugan/FA23-NLP/blob/main/mcdonalds_reviews.csv"
# though it fails with error "C error: Expected 1 fields in line 100, saw 3" delimiter issue? guessing type issue?
#data = pd.read_csv("C:/Users/Brendan/Documents/Courses/Data Science MS-Cert/FA23-DSCI D590/group project/mcdonalds_reviews.csv", 
                   #delimiter=",")
data = pd.read_csv("/Users/olgavyrvich/Macdonalds/mcdonalds_reviews.csv", 
                   delimiter=",")

# create store_id from unique lat/lon
latlon = pd.DataFrame(
         {"latitude": data.latitude.unique(),
          "longitude": data.longitude.unique(),
          })
latlon["store_id"] = [i for i in range(1, len(latlon)+1)]

data = data.join(latlon.set_index(["latitude", "longitude"]), 
                 on = ["latitude", "longitude"], 
                 how = "left")

st.markdown("## Mapping customer sentiment")
# we can use boilerplate language here if at all
'''Understanding customer sentiment can be crucial to business decisions. While customers provide ratings (:star:), 
they also provide a large body of qualitative feedback that can be difficult to assess at scale. 
Using NLP methods, sentiments ("positive" or "negative") predicted from text reviews as well as polarity scores allow further
insight into customers' attitudes that can help identify low-performing stores for intervention or high-performing stores to model after.
'''

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
if (state_selected) == None:
    group_var = "state_abb"
    group_var_label = "state"
    lat_lon = [39.8282, 98.5796]
else:
    group_var = "store_id"
    group_var_label = "store"
    lat_lon = [
        d.latitude.mean(),
        d.longitude.mean()
    ]
# in encoding can use e.g. x='sum(name)' alt.X('name', aggregate='sum')
map_state = alt.Chart(usa).mark_geoshape(
    stroke = "white",
    fill = "grey"
).transform_lookup(
    lookup = "id", 
    from_ = alt.LookupData(data = d, 
                           key = "state_id", 
                           fields = np.array(d.columns))
).encode().project(
    type = "albersUsa"
).properties(
    height = 600,
    width = 800,
)

map_sent = alt.Chart(d).transform_aggregate(
    latitude = "mean(latitude)",
    longitude = "mean(longitude)",
    positive_reviews = "sum(sentiment_num)",
    total_reviews = "count()",
    avg_sentiment = "mean(sentiment_num)",
    avg_polarity = "mean(polarity)",
    groupby = [group_var]
).mark_circle(size = 150).encode(
    latitude = "latitude:Q",
    longitude = "longitude:Q",
    color = alt.Color("avg_sentiment:Q",
                      scale = alt.Scale( #type = "quantize", 
                                        scheme = "redblue",
                                        domain = [0, 1])),
    tooltip = list(
        [group_var + ":N", 
        "positive_reviews:Q",
        "total_reviews:Q",
        "avg_sentiment:Q",
        "avg_polarity:Q"
    ])
).properties(
    title = "Review sentiments by " + group_var_label
)

plt = map_state + map_sent

st.altair_chart(plt, 
                use_container_width = True,
                theme = "streamlit")

if st.checkbox("Preview data", value = True):
    st.subheader("Raw data")
    st.write(d[["store_id", "state_name", "sentiment", "polarity", "review_clean"]])
