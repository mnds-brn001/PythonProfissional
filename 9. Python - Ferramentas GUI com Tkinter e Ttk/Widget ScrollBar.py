import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Python Tkinter")
#root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text1 = tk.Text(root, height=10, font="Gill-Sans-MT 24")
text1.grid(row=0, column=0, sticky="ew")

scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=text1.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")

text1["yscrollcommand"] = scrollbar.set

root.mainloop()