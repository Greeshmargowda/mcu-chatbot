
# Marvel Cinematic Universe movie data

MCU_MOVIES = {
    "Phase 1": [
        {
            "id": 1,
            "title": "Iron Man",
            "year": 2008,
            "chronological_order": 3,
            "summary": "Genius billionaire Tony Stark builds a high-tech suit of armor and becomes Iron Man after being held captive in an Afghan cave.",
            "connections": ["The Avengers", "Iron Man 2", "Iron Man 3"],
            "post_credit": "Nick Fury approaches Tony Stark about the Avenger Initiative.",
            "key_characters": ["Tony Stark/Iron Man", "Pepper Potts", "James Rhodes", "Obadiah Stane"]
        },
        {
            "id": 2,
            "title": "The Incredible Hulk",
            "year": 2008,
            "chronological_order": 4,
            "summary": "Dr. Bruce Banner becomes the Hulk as he searches for a cure to his condition while fighting the Abomination.",
            "connections": ["The Avengers", "Shang-Chi and the Legend of the Ten Rings"],
            "post_credit": "Tony Stark meets with General Ross about putting a team together.",
            "key_characters": ["Bruce Banner/Hulk", "General Thaddeus Ross", "Betty Ross", "Emil Blonsky/Abomination"]
        },
        {
            "id": 3,
            "title": "Iron Man 2",
            "year": 2010,
            "chronological_order": 5,
            "summary": "Tony Stark faces pressure to share his technology while combating a vengeful villain with ties to his father's legacy.",
            "connections": ["Iron Man", "The Avengers", "Black Widow"],
            "post_credit": "Agent Coulson reports the discovery of Thor's hammer in New Mexico.",
            "key_characters": ["Tony Stark/Iron Man", "Natasha Romanoff/Black Widow", "Nick Fury", "Ivan Vanko/Whiplash"]
        },
        {
            "id": 4,
            "title": "Thor",
            "year": 2011,
            "chronological_order": 6,
            "summary": "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans on Earth where he learns humility.",
            "connections": ["The Avengers", "Thor: The Dark World", "Thor: Ragnarok"],
            "post_credit": "Nick Fury shows Dr. Selvig the Tesseract, unknowingly observed by Loki.",
            "key_characters": ["Thor", "Loki", "Jane Foster", "Odin"]
        },
        {
            "id": 5,
            "title": "Captain America: The First Avenger",
            "year": 2011,
            "chronological_order": 1,
            "summary": "Steve Rogers, a rejected military soldier, transforms into Captain America after taking a dose of a super-soldier serum during WWII.",
            "connections": ["The Avengers", "Captain America: The Winter Soldier", "Avengers: Endgame"],
            "post_credit": "Nick Fury approaches Captain America about a mission with worldwide ramifications.",
            "key_characters": ["Steve Rogers/Captain America", "Peggy Carter", "Bucky Barnes", "Red Skull"]
        },
        {
            "id": 6,
            "title": "Marvel's The Avengers",
            "year": 2012,
            "chronological_order": 7,
            "summary": "Earth's mightiest heroes must come together and learn to fight as a team to stop Loki and his alien army from enslaving humanity.",
            "connections": ["All Phase 1 movies", "Avengers: Age of Ultron", "Loki (series)"],
            "post_credit": "The Other tells Thanos that challenging the Avengers would be 'to court death.'",
            "key_characters": ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Loki", "Nick Fury"]
        }
    ],
    "Phase 2": [
        {
            "id": 7,
            "title": "Iron Man 3",
            "year": 2013,
            "chronological_order": 8,
            "summary": "Tony Stark struggles with PTSD after the Battle of New York while facing a mysterious terrorist called the Mandarin.",
            "connections": ["Iron Man", "Iron Man 2", "Avengers: Age of Ultron"],
            "post_credit": "Tony Stark recounts his story to Dr. Bruce Banner, who falls asleep during it.",
            "key_characters": ["Tony Stark/Iron Man", "Pepper Potts", "James Rhodes/War Machine", "Aldrich Killian"]
        },
        {
            "id": 8,
            "title": "Thor: The Dark World",
            "year": 2013,
            "chronological_order": 9,
            "summary": "Thor teams up with his treacherous brother Loki to save the Nine Realms from the Dark Elves led by Malekith.",
            "connections": ["Thor", "Avengers: Endgame", "Loki (series)"],
            "post_credit": "Lady Sif and Volstagg entrust the Aether to the Collector; Thor returns to Jane Foster on Earth.",
            "key_characters": ["Thor", "Loki", "Jane Foster", "Malekith"]
        },
        {
            "id": 9,
            "title": "Captain America: The Winter Soldier",
            "year": 2014,
            "chronological_order": 10,
            "summary": "Steve Rogers teams with Black Widow and Falcon to unravel a conspiracy within S.H.I.E.L.D. while facing a mysterious assassin known as the Winter Soldier.",
            "connections": ["Captain America: The First Avenger", "Captain America: Civil War", "The Falcon and the Winter Soldier"],
            "post_credit": "Baron von Strucker experiments on Quicksilver and Scarlet Witch with Loki's scepter; Bucky visits the Captain America museum exhibit.",
            "key_characters": ["Steve Rogers/Captain America", "Natasha Romanoff/Black Widow", "Sam Wilson/Falcon", "Bucky Barnes/Winter Soldier"]
        },
        {
            "id": 10,
            "title": "Guardians of the Galaxy",
            "year": 2014,
            "chronological_order": 11,
            "summary": "A group of intergalactic misfits team up to protect a powerful Infinity Stone from a fanatical warrior named Ronan.",
            "connections": ["Guardians of the Galaxy Vol. 2", "Avengers: Infinity War", "Avengers: Endgame"],
            "post_credit": "Baby Groot dances to Jackson 5's 'I Want You Back'; the Collector is visited by Howard the Duck in his destroyed collection room.",
            "key_characters": ["Peter Quill/Star-Lord", "Gamora", "Drax", "Rocket", "Groot"]
        },
        {
            "id": 11,
            "title": "Avengers: Age of Ultron",
            "year": 2015,
            "chronological_order": 12,
            "summary": "The Avengers battle Ultron, an artificial intelligence obsessed with causing human extinction, while encountering Quicksilver and Scarlet Witch.",
            "connections": ["The Avengers", "Captain America: Civil War", "WandaVision"],
            "post_credit": "Thanos puts on the Infinity Gauntlet and says 'Fine, I'll do it myself.'",
            "key_characters": ["Tony Stark/Iron Man", "Steve Rogers/Captain America", "Thor", "Bruce Banner/Hulk", "Natasha Romanoff/Black Widow", "Clint Barton/Hawkeye", "Wanda Maximoff/Scarlet Witch", "Vision"]
        },
        {
            "id": 12,
            "title": "Ant-Man",
            "year": 2015,
            "chronological_order": 13,
            "summary": "Cat burglar Scott Lang must aid his mentor Dr. Hank Pym in safeguarding the Ant-Man technology and pull off a heist to save the world.",
            "connections": ["Captain America: Civil War", "Ant-Man and the Wasp", "Avengers: Endgame"],
            "post_credit": "Hank Pym shows Hope van Dyne a new Wasp suit; Captain America and Falcon have captured the Winter Soldier.",
            "key_characters": ["Scott Lang/Ant-Man", "Hope van Dyne", "Hank Pym", "Darren Cross/Yellowjacket"]
        }
    ],
    "Phase 3": [
        {
            "id": 13,
            "title": "Captain America: Civil War",
            "year": 2016,
            "chronological_order": 14,
            "summary": "Political pressure mounts to install a system of accountability when the Avengers' actions lead to collateral damage, causing a rift between Captain America and Iron Man.",
            "connections": ["Captain America: The Winter Soldier", "Black Panther", "Spider-Man: Homecoming", "Avengers: Infinity War"],
            "post_credit": "Bucky goes into cryo-sleep in Wakanda; Peter Parker explores his new tech from Tony Stark.",
            "key_characters": ["Steve Rogers/Captain America", "Tony Stark/Iron Man", "Bucky Barnes/Winter Soldier", "T'Challa/Black Panther", "Peter Parker/Spider-Man"]
        },
        {
            "id": 14,
            "title": "Doctor Strange",
            "year": 2016,
            "chronological_order": 15,
            "summary": "After a career-ending car accident, brilliant neurosurgeon Dr. Stephen Strange discovers the hidden world of magic and alternate dimensions.",
            "connections": ["Thor: Ragnarok", "Avengers: Infinity War", "Doctor Strange in the Multiverse of Madness"],
            "post_credit": "Strange agrees to help Thor find his father; Mordo begins hunting sorcerers.",
            "key_characters": ["Stephen Strange/Doctor Strange", "Wong", "The Ancient One", "Karl Mordo"]
        },
        {
            "id": 15,
            "title": "Guardians of the Galaxy Vol. 2",
            "year": 2017,
            "chronological_order": 16,
            "summary": "The Guardians of the Galaxy travel throughout the cosmos as they help Peter Quill learn more about his mysterious parentage.",
            "connections": ["Guardians of the Galaxy", "Avengers: Infinity War"],
            "post_credit": "Multiple scenes including teenage Groot and the original Guardians team.",
            "key_characters": ["Peter Quill/Star-Lord", "Gamora", "Drax", "Rocket", "Baby Groot", "Ego"]
        },
        {
            "id": 16,
            "title": "Spider-Man: Homecoming",
            "year": 2017,
            "chronological_order": 17,
            "summary": "Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.",
            "connections": ["Captain America: Civil War", "Avengers: Infinity War", "Spider-Man: Far From Home"],
            "post_credit": "Captain America films a PSA about patience; Vulture meets with Scorpion in prison.",
            "key_characters": ["Peter Parker/Spider-Man", "Tony Stark/Iron Man", "Adrian Toomes/Vulture", "May Parker"]
        }
    ]
    # (Additional movies would continue here)
}

def get_movie_by_title(title):
    """Return movie data by title"""
    for phase, movies in MCU_MOVIES.items():
        for movie in movies:
            if movie["title"].lower() == title.lower():
                return movie
    return None

def get_movies_by_phase(phase):
    """Return all movies in a specific phase"""
    if phase in MCU_MOVIES:
        return MCU_MOVIES[phase]
    return []

def get_all_movies_chronological():
    """Return all movies in chronological order"""
    all_movies = []
    for phase, movies in MCU_MOVIES.items():
        all_movies.extend(movies)
    return sorted(all_movies, key=lambda x: x["chronological_order"])

def get_all_movies_release():
    """Return all movies in release order"""
    all_movies = []
    for phase, movies in MCU_MOVIES.items():
        all_movies.extend(movies)
    return sorted(all_movies, key=lambda x: x["id"])

def get_connected_movies(title):
    """Return movies connected to the given title"""
    movie = get_movie_by_title(title)
    if not movie:
        return []
    
    connected = []
    for connection in movie["connections"]:
        connected_movie = get_movie_by_title(connection)
        if connected_movie:
            connected.append(connected_movie)
    
    return connected

def search_movies(query):
    """Search movies by query string in title or summary"""
    query = query.lower()
    results = []
    
    for phase, movies in MCU_MOVIES.items():
        for movie in movies:
            if query in movie["title"].lower() or query in movie["summary"].lower():
                results.append(movie)
    
    return results

def recommend_movies(preference, count=3):
    """Recommend movies based on user preferences"""
    all_movies = []
    for phase, movies in MCU_MOVIES.items():
        all_movies.extend(movies)
    
    preference = preference.lower()
    
    # Score movies based on preference
    scored_movies = []
    for movie in all_movies:
        score = 0
        
        # Check if preference appears in title
        if preference in movie["title"].lower():
            score += 5
            
        # Check if preference appears in summary
        if preference in movie["summary"].lower():
            score += 3
            
        # Check if preference appears in key characters
        for character in movie["key_characters"]:
            if preference in character.lower():
                score += 4
                break
                
        # Add to scored movies if there's any match
        if score > 0:
            scored_movies.append((score, movie))
    
    # Sort by score and get top count
    scored_movies.sort(reverse=True, key=lambda x: x[0])
    recommendations = [movie for score, movie in scored_movies[:count]]
    
    # If no specific recommendations, return newest movies first
    if not recommendations:
        return sorted(all_movies, key=lambda x: x["year"], reverse=True)[:count]
        
    return recommendations
