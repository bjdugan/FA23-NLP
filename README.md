# FA23-NLP
FA23-DSCI D590 Natural Language Processing Group 10 Project  
I'm Loving It? Sentiment Analysis of McDonald's Customer Reviews
Olga Vyrvich, Jill Henry, Brendan Dugan

## Project Description
### Objectives and Usefulness
The project of sentiment analysis will help to find out the perception of customers towards McDonald's USA stores. The results of the analysis can help the company understand the main areas that resonate with their customers and areas that require improvement in quality and customer satisfaction. These results can help management of McDonald’s make data-driven decisions to improve the customer experience and increase brand profitability. The Sentiment analysis is an indispensable way to understand the experience and interaction of a client with a brand, service, product. This project will help management of McDonald's understand what customers don't like and what they like. And what conditions lead to negative or positive reviews, as well as customer expectations and how they change over time, as well as regional differences in customer sentiment. Our web app allows management and staff of McDonald's to understand customer sentiment and will increase customer satisfaction.  

The Streamlit [app](https://fa23-nlp-xghi77bgedswwkskxpvcz6.streamlit.app/) can be viewed here: (https://fa23-nlp-xghi77bgedswwkskxpvcz6.streamlit.app/). Due to inactivity, it might take a moment to load the first time.

### Data
The dataset we chose is located on [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews). It was compiled by Nidula Elgiriyewithana. Nidula specified that the use cases for the data in a learning or research context could be sentiment analysis, location-based analysis, category analysis, or time-based analysis. It contains over 33,396 scraped Google reviews of McDonald’s restaurants across the US. 48% of reviewers gave 4 or 5 stars (positive), 14% of reviewers gave 3 stars (neutral), and 37% gave 1 or 2 stars (negative), so the data is fairly balanced overall. The output is a .csv file, and it contains the following columns:  
 - Reviewer_id: unique number to identify each anonymized reviewer
 - Store_name: location name (only contains “McDonald’s” value)
 - Category: store type (only contains “Fast food restaurant” value)
 - Store_address: McDonald’s location address
 - Latitude: latitude coordinate of McDonald’s location
 - Longitude: longitude coordinate of McDonald’s location
 - Rating_count: number of ratings the McDonald’s location has
 - Review_time: how long ago the rating was published from when the data was put on Kaggle
 - Review: text of the review
 - Rating: how many stars the reviewer gave

These data are not cleaned, and will need to have some processing done. The review column text will need to be tokenized, have stopwords removed, and have either lemmatization or stemming done. Something important to note is that there will likely be typos, slang, or abbreviations because of the nature of user-inputted text. There are also some question mark symbols (�), likely indicating something that was put in the Google review that can’t be displayed in a .csv file (i.e. emoji, other special punctuation). Some other punctuation may need to be removed like commas or dashes, but punctuation may need to be kept in because some reviewers may choose to express their positive or negative opinions using punctuation (like with excessive exclamation points). We will have to evaluate the data and come up with a decision based on our findings. We also would want to extract the state and/or zip code from the store_address field for sentiment analysis based on geographic location. In addition, we would want to just have the number indicating how many stars rather than have the word “star” or “stars” in the rating column.

### Functionality
Our goal for our application is to be able to create and display sentiment scores for McDonald's locations based on customer feedback left through Google reviews. This app will employ NLP and sentiment analysis Python libraries to clean, process, and generate sentiment scores at various levels of aggregation. Given some of the other features available in the dataset, we may try to plot the sentiments scores against customer ratings or plot sentiments by various levels of geographic aggregation (e.g., by state or region rather than individual stores), or present comparative information for selected stores (e.g., how does McDonald's at location X compare to other shops in the same state?), provide examples or wordclouds of the reviews associated with sentiment scores, and offer other summary statistics. We hope that by enabling end users to filter and sort results we can better assist them in understanding what McDonald's customers think.

