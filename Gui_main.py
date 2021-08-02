from tkinter.constants import BOTTOM, CENTER, LEFT, N, TOP, W
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import ttk

import border_frame_data
import tkinter as tk
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
    anime_news_image = tk.Label(anime_news_frame ,image=image_photo)
    anime_news_image.image = image_photo
    anime_news_image.pack(side=LEFT, anchor=W, padx=10)

def rounded_rect(canvas, x, y, w, h, c):
    canvas.create_arc(x,   y,   x+2*c,   y+2*c,   start= 90, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y+h-2*c, x+w, y+h, start=270, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y,   x+w, y+2*c,   start=  0, extent=90, style="arc")
    canvas.create_arc(x,   y+h-2*c, x+2*c,   y+h, start=180, extent=90, style="arc")
    canvas.create_line(x+c, y,   x+w-c, y    )
    canvas.create_line(x+c, y+h, x+w-c, y+h  )
    canvas.create_line(x,   y+c, x,     y+h-c)
    canvas.create_line(x+w, y+c, x+w,   y+h-c)

window = ThemedTk(theme="arc")
window.geometry("400x700")
window.title("Anime News")
window.configure(bg="white")

style = ttk.Style()

borderImage = tk.PhotoImage("borderImage", data=border_frame_data.borderImageData)
focusBorderImage = tk.PhotoImage("focusBorderImage", data=border_frame_data.focusBorderImageData)

style.element_create("RoundedFrame",
                     "image", borderImage,
                     ("focus", focusBorderImage),
                     border=16, sticky="nsew")
style.layout("RoundedFrame",
             [("RoundedFrame", {"sticky": "nsew"})])

anime_news_frame = ttk.Frame(style="RoundedFrame", padding=10)
anime_news_frame.pack(padx=15, pady=30)

# Clickable link label.
anime_news_url = tk.Label(anime_news_frame, font=("Calibri Bold", 12), fg="blue", cursor="hand2", bg="white")
anime_news_url.bind("<Button-1>",lambda event: webbrowser.open(anime_news_url.cget("text")))
anime_news_url.pack(side=TOP, anchor=N, pady=10)

anime_news_title = tk.Label(anime_news_frame,font=("Calibri Bold", 12), bg="white")
anime_news_title.pack(side=TOP, pady=10, padx=8)

number_of_screen_unit = 400
anime_news_body = tk.Label(anime_news_frame, font=("Calibri Bold", 10), wraplength=number_of_screen_unit, bg="white")
anime_news_body.pack(side=BOTTOM, pady=10, padx=8)

populate_labels()

window.mainloop()
