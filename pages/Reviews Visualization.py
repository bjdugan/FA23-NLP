import streamlit as st
import pandas as pd
import plotly.express as px

st.write("""
# Reviews Visualization 
""")
st.write('---')

#data = pd.read_csv("https://raw.github.iu.edu/bjdugan/FA23-NLP/main/mcdonalds_reviews.csv?token=GHSAT0AAAAAAAAAU2AJ5DZIEXWDV7RL6BUYZL6KG5Q",
#                   delimiter=",")
data = pd.read_csv("https://raw.githubusercontent.com/bjdugan/FA23-NLP/main/mcdonalds_reviews.csv",
                   delimiter = ",")

st.write("## Sentiment Analysis Based on Reviews")
if st.checkbox("Show Data"):
    st.write(data[["store_id", "state_name", "sentiment", "polarity", "review_clean"]])

sentiment=data['sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Reviews':sentiment.values})

st.write("Aggregate sentiments of reviews")
st.plotly_chart(
    px.bar(sentiment, x='Sentiment', y='Reviews', color= 'Reviews', height=500)
)

state_data=data['state_abb'].value_counts()
st.write("Total reviews by state")
state_data=pd.DataFrame({'Sentiment':state_data.index,'Reviews':state_data.values})

fig1 = px.bar(state_data, x='Sentiment', y='Reviews', color= 'Reviews',height=500)
st.plotly_chart(fig1)

st.sidebar.subheader("Sentiments by State:")
choice = st.sidebar.multiselect("States", ('FL ','TX', 'CA', 'NY','NJ','NV','PA','UT','IL','DC','VA'), key = '0')

if len(choice)>0:
    st.write("Sentiments by state")
    state_data=data[data.state_abb.isin(choice)]
    fig2 = px.histogram(state_data, x='state_abb', y='sentiment', histfunc='count', 
                        color='sentiment',labels={'sentiment':'reviews'}, 
                        height=600, width=800)
    st.plotly_chart(fig2)




