import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Initialize Genius API with your token
genius = lyricsgenius.Genius("YOUR_GENIUS_API_TOKEN")

# Function to fetch lyrics
def fetch_lyrics():
    song_title = song_entry.get()
    artist_name = artist_entry.get()
    
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            messagebox.showinfo("Not Found", "Lyrics not found for the given song.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the GUI
root = tk.Tk()
root.title("Lyrics Extractor")

# Song Title
tk.Label(root, text="Song Title").grid(row=0, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=40)
song_entry.grid(row=0, column=1, padx=10, pady=10)

# Artist Name
tk.Label(root, text="Artist Name").grid(row=1, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=40)
artist_entry.grid(row=1, column=1, padx=10, pady=10)

# Fetch Lyrics Button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Text Box to Display Lyrics
lyrics_text = tk.Text(root, wrap='word', width=60, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
