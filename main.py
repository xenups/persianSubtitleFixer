import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
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

        self.last_search_label = Label(self, text="  ")
        self.last_search_label.place(x=30, y=265)

        self.listbox = Listbox(container, width=100, height=10)

        vscrollbar = Scrollbar(container, orient="vertical", command=self.listbox.yview)
        hscrollbar = Scrollbar(container, orient="horizontal", command=self.listbox.xview)

        vscrollbar.pack(side="right", fill="y")
        hscrollbar.pack(side="bottom", fill="x")

        self.listbox.config(xscrollcommand=hscrollbar.set, yscrollcommand=vscrollbar.set)
        self.listbox.pack()
        self.listbox.place(x=30, y=100)
        self.listbox.insert(END, "a list entry")
        # self.listbox.config(width=0)

    def add_subtitle_to_listbox(self, names):
        self.listbox.insert(END, names)
        self.last_search_label.config(text=names)

    def open_dialogue(self):
        try:
            folder_name = filedialog.askdirectory()
            self.path_label.config(text=folder_name)
            if folder_name:
                self.listbox.delete(0, tk.END)
                self.last_search_label.config(text=" ")
                t = SubFinderThread(self.add_subtitle_to_listbox, folder_name)
                t.start()
        except:
            messagebox.showerror("ERROR", "Problem in opening folder")

        # self.store_button['state'] = DISABLED


if __name__ == "__main__":
    app = MainGUI()

    # app.titleBar.titleLabel['text'] = "test 2"

    # t.start()

    app.mainloop()
