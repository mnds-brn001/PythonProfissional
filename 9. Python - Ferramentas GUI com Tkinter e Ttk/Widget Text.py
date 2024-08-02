from tkinter import Tk, Text, ttk


root=Tk()
root.title("Python Tkinter")

text = Text(
    root,
    height=8,
    width=10,
    font="Gill-Sans-MT 22",
    bg="#FF2D0F",
    fg="#FFCE45"
)
text.pack()


root.mainloop()