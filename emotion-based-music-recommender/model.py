# model.py

SONGS = {
    "happy": [
        "Pharrell Williams - Happy",
        "Bruno Mars - Uptown Funk",
        "Katy Perry - Roar",
        "Justin Timberlake - Can't Stop the Feeling"
    ],
    "sad": [
        "Adele - Someone Like You",
        "Coldplay - Fix You",
        "Passenger - Let Her Go"
    ],
    "angry": [
        "Eminem - Lose Yourself",
        "Linkin Park - Numb",
        "Imagine Dragons - Believer"
    ],
    "relaxed": [
        "Marconi Union - Weightless",
        "Ed Sheeran - Perfect",
        "Coldplay - Yellow"
    ]
}

def detect_emotion():
    return "happy"   # demo logic


def recommend_songs(emotion):
    return SONGS.get(emotion, [])
