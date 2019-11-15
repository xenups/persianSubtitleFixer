import tkinter as tk
from tkinter import *
from tkinter import filedialog
from SRTWalker import SRTHandler

from tkinter.messagebox import showinfo
from functools import partial


class MainGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        # initialize the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('500x320')
        self.title('SRT Convertor')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        store_button = Button(self, text='select path', command=self.opendialoug, bd=4, width=10,
                              activebackground='lightgrey', font='Bnazanin 10 bold')
        store_button.place(x=10, y=50)
        self.path_lable = Label(self, text=" path ")
        self.path_lable.place(x=10, y=10)

    def opendialoug(self):
        folder_name = filedialog.askdirectory()
        self.path_lable.config(text=folder_name)
        srt = SRTHandler(folder_name)
        print(srt.search_srt_files())


if __name__ == "__main__":
    app = MainGUI()

    # app.titleBar.titleLabel['text'] = "test 2"

    # t.start()

    app.mainloop()