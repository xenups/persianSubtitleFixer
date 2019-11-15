import tkinter as tk
from tkinter import *
from tkinter import filedialog
from SRTWalker import SubFinderThread

from tkinter.messagebox import showinfo
from functools import partial


class MainGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        # initialize the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('700x300')
        self.title('SRT Converter')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        self.store_button = Button(self, text='select path', command=self.open_dialogue, bd=4, width=10,
                                   activebackground='lightgrey', font='Bnazanin 10 bold')
        self.store_button.place(x=10, y=50)
        self.path_label = Label(self, text=" path ")
        self.path_label.place(x=10, y=10)
        self.listbox = Listbox(container, width=100, height=10)

        scrollbar = Scrollbar(container, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.pack()
        self.listbox.place(x=30, y=100)
        self.listbox.insert(END, "a list entry")
        # self.listbox.config(width=0)

    def add_subtitle_to_listbox(self, names):
        self.listbox.insert(END, names)

    def open_dialogue(self):
        folder_name = filedialog.askdirectory()
        self.path_label.config(text=folder_name)

        self.listbox.delete(0, tk.END)
        t = SubFinderThread(self.add_subtitle_to_listbox, folder_name)
        t.start()
        # self.store_button['state'] = DISABLED


if __name__ == "__main__":
    app = MainGUI()

    # app.titleBar.titleLabel['text'] = "test 2"

    # t.start()

    app.mainloop()
