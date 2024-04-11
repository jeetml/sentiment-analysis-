import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
def get_imdb_reviews(movie_id):
    base_url = f'https://www.imdb.com/title/{movie_id}/reviews?ref_=tt_ql_3'

    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        review_elements = soup.find_all('div', class_='text show-more__control')

        reviews = []
        for index, review_element in enumerate(review_elements):
            review_text = review_element.text.strip()
            reviews.append(review_text)

        return reviews
    else:
        return [f"Failed to retrieve reviews. Status code: {response.status_code}"]


def analyze_sentiment(review):
    model = pk.load(open('model.pkl','rb'))
    scaler = pk.load(open('scaler.pkl','rb'))

    review_scale = scaler.transform([review]).toarray()
    result = model.predict(review_scale)
    return result[0]


st.title('IMDb Movie Review Sentiment Analysis')

movie_id = st.text_input('Enter IMDb Movie ID (e.g., tt0422091):')

if movie_id:
    reviews = get_imdb_reviews(movie_id)
    st.header('Reviews:')
    for review in reviews:
        sentiment = analyze_sentiment(review)
        if sentiment == 0:
            st.warning(review)
        else:
            st.success(review)
