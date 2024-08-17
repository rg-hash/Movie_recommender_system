from flask import Flask, request, render_template
from functions import recommend, selected_movies

# Initialize Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html', movies=selected_movies)

# Define the recommendation route
@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie = request.form['movie']
    recommendations = recommend(movie)
    return render_template('index.html', movies=selected_movies, recommendations=recommendations, selected_movie=movie)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
