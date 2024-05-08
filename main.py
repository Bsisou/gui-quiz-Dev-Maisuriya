import tkinter as tk

window = tk.Tk()
window.title("Quiz of Vexatious Contemplation")
window.geometry("300x300")

hello = tk.Label(text="Quiz of Vexatious Contemplation")
hello.pack()
button = tk.Button(text="Start")
button.pack()

tk.mainloop()