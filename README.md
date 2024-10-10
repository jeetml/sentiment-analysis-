# IMDb Movie Review Sentiment Analysis

This project is a web application that allows users to analyze the sentiment of IMDb movie reviews. The app scrapes reviews from IMDb using the movie's IMDb ID, processes the text, and determines whether the sentiment is positive or negative using a pre-trained machine learning model. The app is built using Streamlit, and the model utilizes Natural Language Processing (NLP) techniques.

## Features

- **Scrapes IMDb reviews:** Retrieve movie reviews from IMDb based on the IMDb ID entered by the user.
- **Sentiment analysis:** Classifies each review as either positive or negative using a pre-trained sentiment analysis model.
- **Interactive interface:** Built using Streamlit for ease of use with visual output (warnings for negative reviews and success for positive ones).

## Libraries Used

- `requests`: For making HTTP requests to IMDb.
- `BeautifulSoup (bs4)`: For web scraping the movie reviews.
- `pandas`: Data manipulation and analysis.
- `pickle`: For loading the pre-trained sentiment analysis model and scaler.
- `scikit-learn`: For machine learning tasks like TfidfVectorizer and data transformation.
- `Streamlit`: For building the web application interface.
- `nltk`: Natural Language Toolkit for text processing (e.g., stopwords).

## How It Works

1. **Input Movie ID**: The user enters an IMDb Movie ID (e.g., `tt0422091` for *Pride & Prejudice*).
2. **Scrape Reviews**: The app scrapes the first few movie reviews from the IMDb page using `requests` and `BeautifulSoup`.
3. **Sentiment Analysis**: Each review is passed through a machine learning model that classifies the sentiment as either positive or negative. 
4. **Display Results**: Reviews are displayed in the app, with negative reviews shown as warnings and positive ones as success messages.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/jeetml/sentiment-analysis-.git
    cd imdb-sentiment-analysis
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Pre-trained Model**: Ensure that you have the following pre-trained model files:
    - `model.pkl`: The trained sentiment analysis model.
    - `scaler.pkl`: The TfidfVectorizer or any scaling mechanism you used.

   Place these files in the project directory.

4. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## How to Use

1. Run the application as shown in the setup.
2. Enter a valid IMDb Movie ID in the text input field. Example: `tt0111161` for *The Shawshank Redemption*.
3. The app will scrape reviews from IMDb for the given movie.
4. Reviews will be displayed along with their sentiment (positive or negative).

## Project Structure

```
📦imdb-sentiment-analysis
 ┣ 📂models
 ┃ ┣ 📜model.pkl
 ┃ ┗ 📜scaler.pkl
 ┣ 📜app.py
 ┣ 📜requirements.txt
 ┗ 📜README.md
```

## Example

- Movie ID: `tt0111161` (*The Shawshank Redemption*)
- The app scrapes and displays 10 reviews from IMDb.
- Sentiment is analyzed, and reviews are displayed with warning (negative) or success (positive) markers.

## Future Improvements

- Add more reviews by enabling pagination.
- Use advanced NLP techniques such as BERT for more accurate sentiment analysis.
- Implement language detection and support for multilingual reviews.

## Requirements

- Python 3.8+
- Libraries:
    - `streamlit`
    - `requests`
    - `beautifulsoup4`
    - `pandas`
    - `nltk`
    - `scikit-learn`

Install all dependencies using the `requirements.txt`.
