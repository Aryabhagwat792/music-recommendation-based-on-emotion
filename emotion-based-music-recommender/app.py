import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import model

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Music Emotion App 🎵")
root.geometry("500x500")
root.configure(bg="#121212")

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="🎧 Emotion Music App",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#121212"
)
title.pack(pady=20)

# ---------------- EMOTION SELECT ----------------
emotion_var = tk.StringVar(value="Happy")

emotion_label = tk.Label(
    root,
    text="Select Emotion:",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
)
emotion_label.pack(pady=5)

emotion_box = ttk.Combobox(
    root,
    textvariable=emotion_var,
    values=["Happy", "Sad", "Angry", "Calm", "Excited"],
    state="readonly",
    width=20
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
        emotion = emotion_var.get()
        songs = model.recommend_songs(emotion)
        messagebox.showinfo("Songs 🎵", "\n".join(songs))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_all():
    try:
        songs = model.get_all_songs()
        messagebox.showinfo("All Songs", "\n".join(songs))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def about():
    messagebox.showinfo("About", "Music Emotion App using Python + Tkinter")

def exit_app():
    root.destroy()

# ---------------- BUTTON STYLE ----------------
def create_btn(text, cmd, color):
    btn = tk.Button(
        root,
        text=text,
        command=cmd,   # ✅ IMPORTANT FIX
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        width=25,
        height=2,
        bd=0,
        activebackground="#333333"
    )
    btn.pack(pady=8)
    return btn

# ---------------- BUTTONS ----------------
create_btn("🎭 Detect Emotion", detect, "#ff4d4d")
create_btn("🎵 Recommend Songs", recommend, "#4da6ff")
create_btn("📜 Show All Songs", show_all, "#4dff88")
create_btn("ℹ️ About", about, "#ffcc00")
create_btn("❌ Exit", exit_app, "#b30000")

# ---------------- RUN ----------------
root.mainloop()
