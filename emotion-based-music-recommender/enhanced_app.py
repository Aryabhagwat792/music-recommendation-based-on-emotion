import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import model
import config
import history

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Enhanced Music App 🎵")
root.geometry("520x550")
root.configure(bg=config.BG_COLOR)

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="🎧 Enhanced Emotion Music App",
    font=("Arial", 20, "bold"),
    fg=config.TITLE_COLOR,
    bg=config.BG_COLOR
)
title.pack(pady=20)

# ---------------- SEARCH ----------------
search_entry = tk.Entry(root, font=("Arial", 14))
search_entry.pack(pady=10)
search_entry.insert(0, "Search song...")

# ---------------- EMOTION ----------------
emotion_var = tk.StringVar(value="happy")

emotion_box = ttk.Combobox(
    root,
    textvariable=emotion_var,
    font=("Arial", 12),
    values=["happy", "sad", "angry"],
    state="readonly"
)
emotion_box.pack(pady=5)

# ---------------- FUNCTIONS ----------------
def detect():
    try:
        emotion = model.detect_emotion()
        messagebox.showinfo("Emotion", f"Detected: {emotion}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def recommend():
    try:
        emotion = emotion_var.get().strip().lower()
        songs = model.recommend_songs(emotion)
        messagebox.showinfo("Songs 🎵", "\n".join(songs))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_song():
    query = search_entry.get()
    songs = model.search_song(query)
    messagebox.showinfo("Search Results", "\n".join(songs))

def show_all():
    songs = model.get_all_songs()
    messagebox.showinfo("All Songs", "\n".join(songs))

def exit_app():
    root.destroy()

# ---------------- BUTTON STYLE ----------------
def btn(text, cmd, color):
    tk.Button(
        root,
        text=text,
        command=cmd,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        width=25,
        height=2,
        bd=0
    ).pack(pady=8)

# ---------------- BUTTONS ----------------
btn("🎭 Detect Emotion", detect, "#ff4d4d")
btn("🎵 Recommend Songs", recommend, "#4da6ff")
btn("🔍 Search Song", search_song, "#ffa64d")
btn("📜 Show All Songs", show_all, "#4dff88")
btn("❌ Exit", exit_app, "#b30000")

# ---------------- RUN ----------------
root.mainloop()
