from tkinter import *

root = Tk()
root.title("Mybot Interface")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(1024, 600)
root.geometry("1024x600")
text = Label(root, text="Hello from Mybot")
text.pack()
text2 = Label(root, text="Hello ")
text2.pack()
# root.attributes("-fullscreen", True)+
root.mainloop()