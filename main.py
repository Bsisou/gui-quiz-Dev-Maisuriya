import tkinter as tk
from PIL import Image, ImageTk

#5D088E is the primary purple colour for my quiz images

window = tk.Tk()
window.title("Quiz of Vexatious Contemplation")
window.geometry("634x469")
window.minsize(634, 469)

bg_image = Image.open("enternamepage.png")
bg_image = ImageTk.PhotoImage(bg_image)

quiz_frame = tk.Canvas(bg="whitesmoke")
quiz_frame.pack(expand=True, fill=tk.BOTH)

quiz_frame.create_image(0, 0, image=bg_image, anchor="nw")





tk.mainloop()
