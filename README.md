# YouTube Video Downloader

## 📌 Overview
The **YouTube Video Downloader** is a simple desktop application built with Python and Tkinter that allows users to download YouTube videos easily. The application uses the `pytube` library to fetch and download videos in the highest available resolution.

---

## 🚀 Features
✔ **Simple UI** – Easy-to-use graphical interface using Tkinter.  
✔ **High-Quality Downloads** – Automatically selects the highest resolution available.  
✔ **Error Handling** – Alerts the user if the URL is invalid or if an error occurs.  
✔ **Status Notifications** – Displays messages before and after the download.  
✔ **Lightweight & Fast** – No unnecessary dependencies, ensuring smooth performance.

---

## 🛠️ Installation
### **1️⃣ Prerequisites**
Ensure you have **Python 3.x** installed. If not, download it from [python.org](https://www.python.org/).

### **2️⃣ Install Dependencies**
Run the following command to install the required libraries:
```bash
pip install pytube tkinter
```

---

## 📌 Usage
### **1️⃣ Run the Application**
Execute the script using:
```bash
python main.py
```

### **2️⃣ Enter YouTube URL**
- Copy the YouTube video URL and paste it into the text box.
- Click the **DOWNLOAD** button.
- The video will be saved in the same directory as the script.

---

## 📝 Code Snippet
```python
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

dock = tk.Tk()
dock.geometry('500x300')
dock.resizable(0, 0)
dock.title("YouTube Video Downloader")

tk.Label(dock, text="YouTube Video Downloader", font="arial 20 bold").pack(pady=10)

link = tk.StringVar()
tk.Label(dock, text="Paste Link Here:", font="arial 12 bold").pack()
entry = tk.Entry(dock, width=60, textvariable=link)
entry.pack(pady=5)

def Downloader():
    try:
        yt = YouTube(link.get().strip())
        video = yt.streams.get_highest_resolution()
        messagebox.showinfo("Downloading", f"Downloading: {yt.title}")
        video.download()
        messagebox.showinfo("Success", "Download Completed Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

tk.Button(dock, text="DOWNLOAD", font="Verdana 12 bold", bg="orange", padx=10, command=Downloader).pack(pady=15)

dock.mainloop()
```

---

## ⚠️ Troubleshooting
If you encounter **HTTP Error 403: Forbidden**, try the following fixes:
1. **Update Pytube**: `pip install --upgrade pytube`
2. **Use Itag Selection**: Replace `.get_highest_resolution()` with `yt.streams.get_by_itag(22)`
3. **Use OAuth for Age-Restricted Videos**: `YouTube(url, use_oauth=True, allow_oauth_cache=True)`
4. **Clear Pytube Cache**: `pytube --clear-cache`

---

## 💡 Future Enhancements
🔹 Add an option to select video resolution before downloading.  
🔹 Enable batch downloads for multiple video URLs.  
🔹 Provide an option to download audio-only files.  

---

## 📜 License
This project is **open-source** and available under the MIT License.

---

## 🤝 Contributing
If you’d like to improve this project, feel free to fork the repository and submit a pull request!

---

## 📩 Contact
📧 Email: nischal.maharjan1233@gmail.com  
🔗 GitHub: [GitHubProfile](https://github.com/nisch-mhrzn)

