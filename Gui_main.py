from tkinter.constants import BOTTOM, CENTER, DISABLED, LEFT, N, TOP, W
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import BooleanVar, ttk

import border_frame_data
import tkinter as tk
import News_Scraper
import webbrowser
import urllib
import io

# Turning image into byte in order to be used via ImageTK.
def get_image_byte_io(image):

    image_url_open = urllib.request.urlopen(image)
    raw_data = image_url_open.read()
    image_url_open.close()

    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)

    return photo

def populate_labels(anime_news_url, anime_news_title, anime_news_body, anime_news_frame):

    anime_news_obj = News_Scraper.AnimeNews()
    news = anime_news_obj.individual_anime_news_cell()
    news_image = anime_news_obj.get_anime_image()

    image_photo = get_image_byte_io(news_image)

    print ("-------")
    print (news)

    anime_news_url.config(text=news[0])
    # anime_news_title.config(text=news[1])
    anime_news_title.insert("end", news[1])
    anime_news_title.config(state=DISABLED)

    # anime_news_body.config(text=news[2])
    anime_news_body.insert("end", news[2])
    # Makes tk.text read only.
    anime_news_body.config(state=DISABLED)


    # Displaying Image Label.
    anime_news_image = tk.Label(anime_news_frame ,image=image_photo)
    anime_news_image.image = image_photo
    anime_news_image.pack(side=LEFT, anchor=W, padx=10)

# Taken from: https://stackoverflow.com/questions/51425633/tkinter-how-to-make-a-rounded-corner-text-widget
def rounded_rect(canvas, x, y, w, h, c):
    canvas.create_arc(x,   y,   x+2*c,   y+2*c,   start= 90, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y+h-2*c, x+w, y+h, start=270, extent=90, style="arc")
    canvas.create_arc(x+w-2*c, y,   x+w, y+2*c,   start=  0, extent=90, style="arc")
    canvas.create_arc(x,   y+h-2*c, x+2*c,   y+h, start=180, extent=90, style="arc")
    canvas.create_line(x+c, y,   x+w-c, y    )
    canvas.create_line(x+c, y+h, x+w-c, y+h  )
    canvas.create_line(x,   y+c, x,     y+h-c)
    canvas.create_line(x+w, y+c, x+w,   y+h-c)

def template_frame_widget(frame_style, padding, frame_padx, frame_pady):
    created_template = ttk.Frame(style=frame_style, padding=padding)
    created_template.pack(padx=frame_padx, pady=frame_pady)

    return created_template

def main():
    window = ThemedTk(theme="arc")
    window.geometry("400x700")
    window.title("Anime News")
    window.configure(bg="white")
    window.iconbitmap("favicon.ico")

    # Changes the style of widget frame. Gives rounded edges for corners. 
    style = ttk.Style()

    borderImage = tk.PhotoImage("borderImage", data=border_frame_data.borderImageData)
    focusBorderImage = tk.PhotoImage("focusBorderImage", data=border_frame_data.focusBorderImageData)

    style.element_create("RoundedFrame",
                        "image", borderImage,
                        ("focus", focusBorderImage),
                        border=16, sticky="nsew")
    style.layout("RoundedFrame",
                [("RoundedFrame", {"sticky": "nsew"})])

    # anime_news_frame = ttk.Frame(style="RoundedFrame", padding=10)
    # anime_news_frame.pack(padx=15, pady=30)

    anime_news_frame = template_frame_widget("RoundedFrame", 10, 15, 30)

    # Clickable link label.
    anime_news_url = tk.Label(anime_news_frame, font=("Calibri Bold", 12), fg="blue", cursor="hand2", bg="white")
    anime_news_url.bind("<Button-1>",lambda event: webbrowser.open(anime_news_url.cget("text")))
    anime_news_url.pack(side=TOP, anchor=N, pady=10)

    # anime_news_title = tk.Label(anime_news_frame,font=("Calibri Bold", 12), bg="white")
    anime_news_title = tk.Text(anime_news_frame, font=("Calibri Bold", 12), wrap="word", highlightthickness=0, borderwidth=0, height=1, bg="white")
    anime_news_title.pack(side=TOP, pady=10, padx=8)

    # number_of_screen_unit = 350
    # anime_news_body = tk.Label(anime_news_frame, font=("Calibri Bold", 10), wraplength=number_of_screen_unit, bg="white")
    anime_news_body = tk.Text(anime_news_frame, font=("Calibri Bold", 10), wrap="word", highlightthickness=0, borderwidth=0, height=10)
    #anime_news_body.pack(side=BOTTOM, pady=10, padx=8)
    anime_news_body.pack(side=BOTTOM, expand=True)

    populate_labels(anime_news_url, anime_news_title, anime_news_body, anime_news_frame)

    window.mainloop()

if __name__ == "__main__":
    main()