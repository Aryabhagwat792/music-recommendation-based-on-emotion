# history.py

HISTORY_FILE = "history.txt"


def save_history(text):
    with open(HISTORY_FILE, "a") as f:
        f.write(text + "\n")


def get_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return f.readlines()
    except:
        return []
