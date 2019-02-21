import tkinter

window = tkinter.Tk()

background = tkinter.Canvas(window, bg="black", height=250, width=300)

coord = 10, 50, 240, 210
arc = background.create_arc(coord, start=0, extent=150, fill="white")
background.pack()

window.mainloop()


