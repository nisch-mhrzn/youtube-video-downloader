import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Initialize Tkinter window
dock = tk.Tk()
dock.geometry('500x300')
dock.resizable(0, 0)
dock.title("YouTube Video Downloader")

# Title Label
tk.Label(dock, text="YouTube Video Downloader", font="arial 20 bold").pack(pady=10)

# URL Input
link = tk.StringVar()
tk.Label(dock, text="Paste Link Here:", font="arial 12 bold").pack()
entry = tk.Entry(dock, width=60, textvariable=link)
entry.pack(pady=5)

# Function to download the video
def Downloader():
    url_text = link.get().strip()
    
    if not url_text:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    try:
        yt = YouTube(url_text)
        video = yt.streams.get_highest_resolution()  # Get highest quality
        messagebox.showinfo("Downloading", f"Downloading: {yt.title}")
        video.download()
        messagebox.showinfo("Success", "Download Completed Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

# Download Button
tk.Button(dock, text="DOWNLOAD", font="Verdana 12 bold", bg="orange", padx=10, command=Downloader).pack(pady=15)

# Start Tkinter loop
dock.mainloop()
