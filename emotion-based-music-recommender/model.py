# model.py

def detect_emotion():
    # dummy logic (you can improve later)
    return "happy"


def recommend_songs(emotion):
    songs = {
        "happy": ["Happy - Pharrell Williams", "Uptown Funk", "Can't Stop the Feeling"],
        "sad": ["Someone Like You", "Let Her Go", "Fix You"],
        "angry": ["Believer", "Numb", "Stronger"],
        "calm": ["Perfect", "Night Changes", "Stay"],
        "excited": ["On Top of the World", "Thunder", "Firework"]
    }
    return songs.get(emotion.lower(), ["No songs found"])


def get_all_songs():
    return [
        "Happy - Pharrell Williams",
        "Uptown Funk",
        "Someone Like You",
        "Let Her Go",
        "Believer",
        "Numb",
        "Perfect",
        "Night Changes",
        "Firework"
    ]


def search_song(query):
    all_songs = get_all_songs()
    return [song for song in all_songs if query.lower() in song.lower()]
