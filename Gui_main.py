import tkinter as ttk
from tkinter import font
from tkinter.constants import LEFT
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

import News_Scraper
import webbrowser
import urllib
import io

# class AnimeNews(tkinter.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#         self.create_anime_news_entry()

#     def create_widgets(self):
#         self.hi_there = tkinter.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tkinter.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

#     def create_anime_news_entry(self):
#         test_frame = tkinter.LabelFrame(self)

# if __name__ == "__main__":
#     root = tkinter.Tk()
#     app = AnimeNews(master=root)
#     app.mainloop()

def get_image_byte_io(image):
    image_url_open = urllib.request.urlopen(image)
    raw_data = image_url_open.read()
    image_url_open.close()

    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)

    return photo

def populate_labels():
    anime_news_obj = News_Scraper.AnimeNews()
    news = anime_news_obj.individual_anime_news_cell()
    news_image = anime_news_obj.get_anime_image()

    image_photo = get_image_byte_io(news_image)

    print ("-------")
    print (news)

    anime_news_url.config(text=news[0])
    anime_news_title.config(text=news[1])
    anime_news_body.config(text=news[2])

    # Displaying Image Label.
    anime_news_image = ttk.Label(image=image_photo)
    anime_news_image.image = image_photo
    anime_news_image.pack()

window = ThemedTk(theme="arc")
window.geometry("400x500")

anime_news_frame = ttk.LabelFrame(window)
anime_news_frame.pack()

# Clickable link label.
anime_news_url = ttk.Label(window, font=("Calibri", 12), fg="blue", cursor="hand2")
anime_news_url.bind("<Button-1>",lambda event: webbrowser.open(anime_news_url.cget("text")))
anime_news_url.pack()

anime_news_title = ttk.Label(window,font=("Calibri Bold", 12))
anime_news_title.pack()

number_of_screen_unit = 400
anime_news_body = ttk.Label(window, font=("Calibri", 10), wraplength=number_of_screen_unit)
anime_news_body.pack()

populate_labels()

window.mainloop()
