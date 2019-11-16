import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from SRTWalker import SubFinderThread

from subtitleConvertor import SubtitleConvertor


class MainGUI(tk.Tk):
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def __init__(self, *args, **kwargs):
        # initialize the main window

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('700x310')
        self.resizable(width=FALSE, height=FALSE)

        self.title('SRT Converter')
        container = tk.Frame(self)
        self.center()
        self.list_file_address = []
        container.pack(side="top", fill="both", expand=True)

        self.store_button = Button(self, text='Select Folder', command=self.open_dialogue, bd=2, width=10,
                                   activebackground='lightgrey')
        self.store_button.place(x=30, y=50)

        self.convert_button = Button(self, text='Convert', command=self.convert_action, bd=2, width=10,
                                     activebackground='lightgrey')
        self.convert_button.place(x=120, y=50)

        self.path_label = Label(self, text=" ")
        self.path_label.place(x=10, y=10)
        self.last_search_label = Label(self, text="  ")
        self.last_search_label.place(x=30, y=265)
        self.listbox = Listbox(container, width=100, height=10)
        vertical_scrollbar = Scrollbar(container, orient="vertical", command=self.listbox.yview)
        horizontal_scrollbar = Scrollbar(container, orient="horizontal", command=self.listbox.xview)
        vertical_scrollbar.pack(side="right", fill="y")
        horizontal_scrollbar.pack(side="bottom", fill="x")

        self.listbox.config(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        self.listbox.pack()
        self.listbox.place(x=30, y=100)
        self.listbox.insert(END, "found subtitles: ")

    def add_subtitle_to_listbox(self, names):
        self.listbox.insert(END, names)
        self.last_search_label.config(text=names)
        self.list_file_address.append(names)

    def notify_subtitle_converted(self, names):
        self.listbox.insert(END, names)
        self.last_search_label.config(text=names)

    def open_dialogue(self):
        try:
            self.list_file_address = []
            folder_name = filedialog.askdirectory()
            self.path_label.config(text=folder_name)
            if folder_name:
                self.listbox.delete(0, tk.END)
                self.last_search_label.config(text=" ")
                t = SubFinderThread(self.add_subtitle_to_listbox, folder_name)
                t.start()
        except:
            messagebox.showerror("ERROR", "Problem in opening folder")

    def convert_action(self):
        if self.list_file_address:
            self.listbox.delete(0, tk.END)
            self.last_search_label.config(text=" ")
            t = SubtitleConvertor(self.notify_subtitle_converted, self.list_file_address)
            t.start()
        else:
            tk.messagebox.showwarning(
                "Warning",
                "Please select at least a path"
            )


if __name__ == "__main__":
    app = MainGUI()
    app.title("Persian/Arabic Subtitle Fixer")
    app.iconbitmap("icon.ico")
    app.mainloop()
