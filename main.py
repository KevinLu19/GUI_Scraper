import tkinter
import Gui_main


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Gui_main.AnimeNews(master=root)
    app.master.title("Anime News")
    app.master.geometry("400x500")
    app.mainloop()