import tkinter as tk
import tkinter.ttk
from tkinter import ttk 
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

# anime_news = News_Scraper.AnimeNews()

window = ThemedTk(theme="arc")
ttk.Button(window, text="Quit", command=window.destroy).pack()

example_text = "Anime title: Random Anime Title Goes Here"

labelframe = tkinter.LabelFrame(window, text="Example Frame")
labelframe.pack(fill="both", expand="yes")
 
left = tkinter.Label(labelframe, text=example_text, bg="#d9b6ef")
left.pack()

window.mainloop()
