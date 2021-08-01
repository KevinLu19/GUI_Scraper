import tkinter as ttk
from tkinter import font
from tkinter.constants import LEFT
from ttkthemes import ThemedTk

import News_Scraper

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

def label_frame_template(*args):
    label_frame = ttk.LabelFrame(window, text=args)
    return label_frame

def populate_labels():
    anime_news_obj = News_Scraper.AnimeNews()
    news = anime_news_obj.individual_anime_news_cell()

    anime_news_title.config(text=news)

window = ThemedTk(theme="arc")
# window = ttk.Tk()
window.geometry("400x500")

# label_frame = label_frame_template()
# # labelframe = ttk.LabelFrame(window, text="Example Frame")
# # labelframe.pack(fill="both", expand="yes", padx=10, pady=10)
# label_frame.pack(fill="both", expand="yes", padx=10, pady=10)

anime_news_frame = ttk.LabelFrame(window)
anime_news_frame.pack()

anime_news_title = ttk.Label(window,font=("Calibri Bold", 12))
anime_news_title.pack()


# anime_news_body_text = ttk.Label(window, font=("Calibiri", 18))
# anime_news_body_text.grid(row=1, padx=50)

# example_anime_item = ttk.Label(label_frame, text="Anime News Title Goes here\n")
# example_anime_item.pack()

# exampleanime_2 = ttk.Label(label_frame, text="Anime News Body\n")
# exampleanime_2.pack(side=LEFT)




# label_frame2 = label_frame_template()
# # label_frame2.pack(fill="both", expand="yes", padx=10, pady=10)
# label_frame2.grid(row=0, sticky="N", padx= 10)

# example_anime_item = ttk.Label(label_frame2, font=("Calibri", 20) ,text="Anime News Title Goes here")
# example_anime_item.grid(row= 0)

populate_labels()

window.mainloop()
