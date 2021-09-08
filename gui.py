from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import tkinter
import tkinter as tk
import border_frame_data
import selenium_main
import webbrowser
import urllib
import io

def template_frame_widget(frame_style, padding, frame_padx, frame_pady):
    created_template = ttk.Frame(style=frame_style, padding=padding)
    created_template.pack(padx=frame_padx, pady=frame_pady)

    return created_template

def template_news_url(frame, url_of_news):
    # # Clickable link label.
    # anime_news_url = tk.Label(anime_news_frame, font=("Calibri Bold", 12), fg="blue", cursor="hand2", bg="white")

    anime_news_url = tk.Label(frame, font=("Calibri Bold", 12), fg="blue", cursor="hand2", bg="white")
    anime_news_url.bind("<Button-1>",lambda event: webbrowser.open(anime_news_url.cget("text")))
    anime_news_url.pack(side=TOP, anchor=N, pady=10)

    anime_news_url.config(text=url_of_news)

    return anime_news_url

def template_news_title(frame, title_of_news):
    anime_news_title = tk.Text(frame, font=("Calibri Bold", 12), wrap="word", highlightthickness=0, borderwidth=0, height=1, bg="white")
    anime_news_title.insert("end", title_of_news)
    anime_news_title.config(state=DISABLED)

    anime_news_title.pack(side=TOP, pady=10, padx=8)

    return anime_news_title

def template_news_body(frame, news_text_body):
    anime_news_body = tk.Text(frame, font=("Calibri Bold", 10), wrap="word", highlightthickness=0, borderwidth=0, height=7)
    anime_news_body.insert("end", news_text_body)
    anime_news_body.config(state=DISABLED)

    anime_news_body.pack(side=BOTTOM, expand=True)

    return anime_news_body

# Turning image into byte in order to be used via ImageTK.
def get_image_byte_io(image):

    image_url_open = urllib.request.urlopen(image)
    raw_data = image_url_open.read()
    image_url_open.close()

    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)

    return photo

def populate_each_news(url, title, body, image):
    # Create new frame for each entry for the news
    anime_news_frame = template_frame_widget("RoundedFrame", 10, 15, 10)

    template_news_url(anime_news_frame, url)
    template_news_title(anime_news_frame, title)
    template_news_body(anime_news_frame, body)

    anime_news_image = tk.Label(anime_news_frame ,image=image)
    anime_news_image.image = image
    anime_news_image.pack(side=LEFT, anchor=W, padx=10)

def populate_labels():
    selen_obj = selenium_main.SeleniumMain()
    sel_obj_convert_to_list = list(selen_obj.individual_anime_news_cell())
    
    sel_obj_url = sel_obj_convert_to_list[0]
    sel_obj_title = sel_obj_convert_to_list[1]
    sel_obj_body = sel_obj_convert_to_list[2]

    news_url = sel_obj_url
    news_title = sel_obj_title
    news_body = sel_obj_body
    news_image = selen_obj.get_anime_image()

    print(news_image)
    image_photo = get_image_byte_io(news_image)

    for (url, title, body) in zip(news_url, news_title, news_body):
        url_of_anime_news = url
        titles_of_anime_names = title
        text_body_of_anime_news = body

        populate_each_news(url_of_anime_news, titles_of_anime_names, text_body_of_anime_news, image_photo)


window = tkinter.Tk()
window.geometry("400x700")
window.title("Anime News")
window.configure(bg="white")
window.iconbitmap("favicon.ico")

style = ttk.Style()

borderImage = tk.PhotoImage("borderImage", data=border_frame_data.borderImageData)
focusBorderImage = tk.PhotoImage("focusBorderImage", data=border_frame_data.focusBorderImageData)

style.element_create("RoundedFrame",
                    "image", borderImage,
                    ("focus", focusBorderImage),
                    border=16, sticky="nsew")
style.layout("RoundedFrame",
            [("RoundedFrame", {"sticky": "nsew"})])

populate_labels()

window.mainloop()