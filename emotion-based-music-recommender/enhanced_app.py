import tkinter as tk
from tkinter import ttk, messagebox
import model
import history
import config

root = tk.Tk()
root.title("🎧 Emotion Music App")
root.geometry("650x650")
root.configure(bg=config.BG_COLOR)

# TITLE
tk.Label(
    root,
    text="🎵 Emotion-Based Music Recommender",
    font=("Arial", 20, "bold"),
    fg="white",
    bg=config.BG_COLOR
).pack(pady=20)

# EMOTION SELECT
emotion_var = tk.StringVar()

emotion_box = ttk.Combobox(root, textvariable=emotion_var, state="readonly")
emotion_box["values"] = ["happy", "sad", "angry", "relaxed"]
emotion_box.pack(pady=10)

# LISTBOX
listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=20)

# FUNCTIONS
def recommend():
    emotion = emotion_var.get()

    if emotion == "":
        messagebox.showwarning("Error", "Select emotion first")
        return

    songs = model.recommend_songs(emotion)

    listbox.delete(0, tk.END)

    for s in songs:
        listbox.insert(tk.END, "🎶 " + s)

    history.save_history(emotion)


def detect():
    emotion = model.detect_emotion()
    messagebox.showinfo("Detected Emotion", emotion)


def show_history():
    listbox.delete(0, tk.END)
    data = history.get_history()

    for d in data:
        listbox.insert(tk.END, d.strip())


def clear():
    listbox.delete(0, tk.END)

# BUTTONS
tk.Button(root, text="Recommend", command=recommend, bg="#1DB954", fg="white").pack(pady=5)
tk.Button(root, text="Detect Emotion", command=detect, bg="#1DB954", fg="white").pack(pady=5)
tk.Button(root, text="History", command=show_history, bg="#1DB954", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear, bg="#444", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white").pack(pady=5)

root.mainloop()
