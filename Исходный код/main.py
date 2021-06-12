from tkinter import *
from functions import GIU
import sys

def start_app():
	window = Tk()
	window.wm_attributes('-fullscreen', True)
	window.title("Веселый матан")
	
	top = Toplevel(window)
	top.wm_attributes('-fullscreen', True)
	top.title("Веселый матан")
	top.overrideredirect(1)
	
	top.iconbitmap('all_pictures\\book.ico')
	window.iconbitmap('all_pictures\\book.ico')

	giu = GIU(window, top)
	
	top.mainloop()
	window.mainloop



start_app()
