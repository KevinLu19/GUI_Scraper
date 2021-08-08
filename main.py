import tkinter
import Gui_main


if __name__ == "__main__":
    root = tkinter.Tk()
    # app = Gui_main.AnimeNews(master=root)
    app = Gui_main.main()
    app.geometry("400x700")
    app.title("Anime News")
    app.configure(bg="white")
    app.iconbitmap("favicon.ico")
    app.mainloop()