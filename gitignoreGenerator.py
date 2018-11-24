from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import requests
import os

class gitignoreGenerator:

    def __init__(self, master):
        self.master = master
        master.title(".gitignore Generator")
        languagelbl = Label(master, text='Select programming language')
        languagelbl.pack()
        languagelistbox = Listbox(master)
        languagelistbox.pack()

        for item in ['Actionscript', 'Ada', 'Agda']:
            languagelistbox.insert(END, item)

        enterBtn = Button(master, text='Generate', command=lambda: self.genGitignore(languagelistbox.get(ACTIVE)))
        enterBtn.pack()

    def genGitignore(self, language):
        url = 'https://raw.githubusercontent.com/github/gitignore/master/' + language + '.gitignore'
        r = requests.get(url)
        directory = filedialog.askdirectory(initialdir="/")
        f = open(directory + '/' + language + '.gitignore', 'a')
        f.write(r.text)
        if os.path.isfile(directory + '/' + language + '.gitignore'):
            messagebox.showinfo('Sucess', '.gitignore file sucessfuly created')
        else:
            messagebox.showerror('Error', 'something went wrong, file not created')

root = Tk()
root.geometry('300x250')
generator = gitignoreGenerator(root)
root.mainloop()
