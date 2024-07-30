import os
from tkinter import Tk

root = Tk()
root.minsize(300, 100)
root.title("<--<< The Icon")

# Add Icon to window Titlebar (2024) rev
if os.name == 'nt':
    homepath = os.path.expanduser('~')
    tempFile = os.path.join(homepath, 'Caveman Software', 'Icon', 'icon.ico')

    if (os.path.exists(tempFile) == True):
        root.wm_iconbitmap(default=tempFile)

    else:
        import create_icon
        print('File Created')
        root.wm_iconbitmap(default=tempFile)


root.mainloop()
