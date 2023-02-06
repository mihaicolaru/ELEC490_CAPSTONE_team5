from tkinter import *

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# class nurse_login(Page):
#    def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         inputtxt = Text(self, height = 5, width = 20)
#         inputtxt.pack()

class compartment_select(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        text2 = Label(self, text="Select compartment ", bg="#013F78", font=('Verdana, 40'), fg="white")
        text2.pack(pady=29)

        compartment1_img = PhotoImage(file="Assets/compartment1.png")
        compartment1_button = Button(image=compartment1_img, bg="#013F78", border=0)
        compartment1_button.pack()

        compartment2_img = PhotoImage(file="Assets/compartment2.png")
        compartment2_button = Button(image=compartment2_img, bg="#013F78", border=0)
        compartment2_button.pack(pady=29)

        compartment3_img = PhotoImage(file="Assets/compartment3.png")
        compartment3_button = Button(image=compartment3_img, bg="#013F78", border=0)
        compartment3_button.pack()

class close_compartment(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       text2 = Label(self, text="Please close compartment", bg="#013F78", font=('Verdana, 40'), fg="white")
       text2.pack(pady=29)

class enjoy_meal(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       text2 = Label(self, text="Enjoy your meal!", bg="#013F78", font=('Verdana, 40'), fg="white")
       text2.pack(pady=29)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        # p1 = nurse_login(self)
        p2 = compartment_select(self)
        p3 = close_compartment(self)
        p4 = enjoy_meal(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # b1 = Button(buttonframe, text="Page 1", command=p1.show)
        b2 = Button(buttonframe, text="Page 2", command=p2.show)
        b3 = Button(buttonframe, text="Page 3", command=p3.show)
        b4 = Button(buttonframe, text="Page 4", command=p4.show)

        # b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p2.show()

if __name__ == "__main__":
    window = Tk()
    main = MainView(window)
    window.title("Mybot Interface")
    window.configure(background="#013F78")
    window.minsize(200, 200)
    window.maxsize(1024, 600)
    window.geometry("1024x600")
    window.mainloop()





def nurse_input_state():
    return

def compartment_select_State(): 
    text2 = Label(window, text="Select compartment ", bg="#013F78", font=('Verdana, 40'), fg="white")
    text2.pack(pady=29)

    compartment1_img = PhotoImage(file="Assets/compartment1.png")
    compartment1_button = Button(image=compartment1_img, bg="#013F78", border=0)
    compartment1_button.pack()

    compartment2_img = PhotoImage(file="Assets/compartment2.png")
    compartment2_button = Button(image=compartment2_img, bg="#013F78", border=0)
    compartment2_button.pack(pady=29)

    compartment3_img = PhotoImage(file="Assets/compartment3.png")
    compartment3_button = Button(image=compartment3_img, bg="#013F78", border=0)
    compartment3_button.pack()


def quitGame(event):
    window.destroy()
    

window = Tk()
window.title("Mybot Interface")
window.configure(background="#013F78")
window.minsize(200, 200)
window.maxsize(1024, 600)
window.geometry("1024x600")


# #creating background
# bgImage = ImageTk.PhotoImage(Image.open("Images/background.png")) 
# bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

# #creating button which supports png transparency
# quitImage = ImageTk.PhotoImage(Image.open("Images/quitImage.png"))
# quitButton = canvas.create_image(50, 50, image=quitImage)
# canvas.tag_bind(quitButton, "<Button-1>", quitGame)


# window.attributes("-fullscreen", True)+
window.mainloop()