
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from marvel_data import *

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8080", "http://localhost:8081", "http://localhost:8082", "http://localhost:8083", "http://127.0.0.1:8080", "http://127.0.0.1:8081", "http://127.0.0.1:8082", "http://127.0.0.1:8083"]}})

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Get all movies either in release or chronological order"""
    order = request.args.get('order', 'release')
    
    if order == 'chronological':
        return jsonify(get_all_movies_chronological())
    else:
        return jsonify(get_all_movies_release())

@app.route('/api/movies/phase/<phase>', methods=['GET'])
def get_phase_movies(phase):
    """Get movies by phase"""
    movies = get_movies_by_phase(f"Phase {phase}")
    return jsonify(movies)

@app.route('/api/movies/<title>', methods=['GET'])
def get_movie(title):
    """Get movie by title"""
    movie = get_movie_by_title(title)
    if movie:
        return jsonify(movie)
    return jsonify({"error": "Movie not found"}), 404

@app.route('/api/movies/<title>/connections', methods=['GET'])
def get_movie_connections(title):
    """Get movies connected to the given title"""
    connections = get_connected_movies(title)
    return jsonify(connections)

@app.route('/api/search', methods=['GET'])
def search():
    """Search movies by query string"""
    query = request.args.get('q', '')
    results = search_movies(query)
    return jsonify(results)

@app.route('/api/recommend', methods=['GET'])
def recommend():
    """Recommend movies based on preferences"""
    preference = request.args.get('preference', '')
    count = int(request.args.get('count', 3))
    
    recommendations = recommend_movies(preference, count)
    return jsonify(recommendations)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process chat messages and return responses"""
    data = request.json
    message = data.get('message', '').lower()
    
    # Simple response logic based on message content
    if "recommend" in message or "suggestion" in message:
        if any(hero in message for hero in ["thor", "asgard", "loki"]):
            recommendations = recommend_movies("Thor", 3)
            return jsonify({
                "response": "Based on your interest in Thor, here are some recommendations:",
                "movies": recommendations
            })
        elif any(hero in message for hero in ["iron man", "stark", "tony"]):
            recommendations = recommend_movies("Iron Man", 3)
            return jsonify({
                "response": "For Iron Man fans, I'd recommend these movies:",
                "movies": recommendations
            })
        elif any(hero in message for hero in ["captain america", "steve rogers", "winter soldier"]):
            recommendations = recommend_movies("Captain America", 3)
            return jsonify({
                "response": "If you enjoy Captain America, check out these films:",
                "movies": recommendations
            })
        else:
            return jsonify({
                "response": "I'd recommend watching the MCU in release order for your first time. Start with Iron Man (2008)! Would you like me to tell you more about any specific movie?",
                "movies": get_all_movies_release()[:3]  # Return first 3 movies as recommendations
            })
    
    elif "order" in message or "sequence" in message or "watch" in message:
        if "chronological" in message:
            return jsonify({
                "response": "Here's the chronological order of the MCU films, starting with Captain America: The First Avenger which takes place during WWII.",
                "movies": get_all_movies_chronological()
            })
        else:
            return jsonify({
                "response": "Here's the release order of the MCU films, starting with Iron Man in 2008.",
                "movies": get_all_movies_release()
            })
    
    elif "phase" in message and any(str(num) in message for num in ["1", "2", "3", "4", "5"]):
        # Extract phase number
        for num in ["1", "2", "3", "4", "5"]:
            if num in message:
                phase_movies = get_movies_by_phase(f"Phase {num}")
                return jsonify({
                    "response": f"Here are the movies from Phase {num} of the MCU:",
                    "movies": phase_movies
                })
    
    elif any(movie_term in message for movie_term in ["iron man", "captain america", "thor", "hulk", "avengers", "guardians"]):
        # Extract movie title from message (simplified approach)
        for phase, movies in MCU_MOVIES.items():
            for movie in movies:
                if movie["title"].lower() in message:
                    return jsonify({
                        "response": f"Here's information about {movie['title']}:\n{movie['summary']}\nRelease year: {movie['year']}\n\nIt connects to: {', '.join(movie['connections'])}",
                        "movie": movie
                    })
    
    # Default response
    return jsonify({
        "response": "I'm your Marvel Cinematic Universe guide! You can ask me about movie orders, recommendations, or specific films. What would you like to know?"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
