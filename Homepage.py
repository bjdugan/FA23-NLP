

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multipage App",
    page_icon="",
)

st.sidebar.success("Select a page above.")

image = Image.open("/Users/olgavyrvich/Macdonalds/McDonald's_SVG_logo.svg.png")
st.image(image, '') 


st.write("""
# I'm Loving It?: Sentiment analysis of McDonald's customer reviews


Our goal for our application is to be able to create and display sentiment
scores for McDonald's locations based on customer feedback left through Google reviews. 

The dataset used for this analysis, downloaded from https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews
""")
st.write('---')



st.write("""
#  Reviews Visualization
In this section the data is explored barplots visualization methods. 
""")
st.write('---')


st.write("""
#  map
Mapping customer sentiment 
""")
st.write('---')