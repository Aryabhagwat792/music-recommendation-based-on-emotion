# history.py

history = []

def add_record(emotion, songs):
    history.append({
        "emotion": emotion,
        "songs": songs
    })

def get_history():
    return history
