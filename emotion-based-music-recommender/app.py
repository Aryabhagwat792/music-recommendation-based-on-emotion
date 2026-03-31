import tkinter as tk
import model
import history

root = tk.Tk()
root.title("Music App")
root.geometry("500x500")

entry = tk.Entry(root)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

def recommend():
    emotion = entry.get()

    songs = model.recommend_songs(emotion)

    listbox.delete(0, tk.END)

    if not songs:
        listbox.insert(tk.END, "No songs found")
        return

    for s in songs:
        listbox.insert(tk.END, s)

    history.save_history(emotion)


tk.Button(root, text="Recommend", command=recommend).pack()

root.mainloop()
