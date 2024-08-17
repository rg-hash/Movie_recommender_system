# Movie Recommendation System

This project is a content-based movie recommendation system that suggests movies similar to a selected movie based on their tags. The system utilizes Natural Language Processing (NLP) techniques to analyze the content of movies and recommend those with similar features.

## Project Structure

movie_recommendation/
│
├── app.py                  # Flask application file
├── functions.py            # Contains the recommendation function and data processing logic
├── movies.pkl              # Pickle file containing the movie data
├── recomm.ipynb            # Jupyter notebook for initial exploration and development
├── tmdb_5000_movies.csv    # CSV file containing movie data (used to create movies.pkl)
├── templates/
│   └── index.html          # HTML template for the web interface
└── static/                 # (Optional) Directory for static files like CSS and JS



## Usage
Home Page: Select a movie from the dropdown menu and click "Get Recommendations" to see a list of recommended movies.
Recommendation Logic: The system uses the CountVectorizer to convert movie tags into numerical vectors and then calculates the cosine similarity between them to find the most similar movies.

## Data Source
The movie data used in this project comes from the TMDb 5000 Movie Dataset available on Kaggle.
