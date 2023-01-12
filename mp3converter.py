from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment

def convert_video_to_mp3():
    # video dosyasını seç
    video_path = filedialog.askopenfilename(initialdir = ".", title = "Select video file", filetypes = (("Video files", "*.mp4;*.mkv"), ("all files", "*.*")))

    # mp3 dosyasının kaydedileceği yolu seç
    mp3_path = filedialog.asksaveasfilename(initialdir = ".", title = "Save mp3 as", defaultextension=".mp3")

    # video dosyasını mp3 dönüştür
    AudioSegment.from_file(video_path, "mp4").export(mp3_path, format="mp3")
    print("Video to mp3 conversion successful!")

root = Tk()
root.title("Video to mp3 converter")

convert_button = Button(root, text="Convert video to mp3", command=convert_video_to_mp3)
convert_button.pack()

root.mainloop()

