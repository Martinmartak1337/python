from platform import system
from os import getlogin
import tkinter
import urllib.request


def func():
    os_system = system()
    user = getlogin()
    try:
        if os_system != 'Linux':
            exit()
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        gui = tkinter.Tk()
        gui.geometry('640x480')
        gui.title("Error")
        tkinter.Label(gui, text=f"An error occurred while trying to run the application {user} please close the window "
                                f"and "
                                "report the error at github/truemartinosss" + " " +
                                external_ip).pack()
        gui.mainloop()
    except Exception:
        pass


func()
