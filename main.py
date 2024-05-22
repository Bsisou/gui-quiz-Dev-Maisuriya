import tkinter as tk
from PIL import Image, ImageTk

#5D088E is the primary purple colour for my quiz images

class StartQuiz:
    def __init__(self, parent):
        self.quiz_frame = tk.Canvas(parent, bg="#290f42")
        self.quiz_frame.pack(expand=True, fill=tk.BOTH)
        bg_image = Image.open("enternamepage.png")
        bg_image = ImageTk.PhotoImage(bg_image)

        self.quiz_frame.create_image(0, 0, image=bg_image, anchor="nw")
        
        window.bind("<Configure>", self.on_resize)
    
    def on_resize(self, event):
        print("test")

        global bg_image
        bg_image = Image.open("enternamepage.png")

        ratio = self.quiz_frame.winfo_width() / 634
        print(ratio)
        if 469 * ratio > self.quiz_frame.winfo_height():
            ratio = self.quiz_frame.winfo_height() / 469
        print(ratio)

        if ratio <= 0:
            return

        print("resize")

        width = int(634 * ratio)
        height = int(469 * ratio)
        bg_image = bg_image.resize((width, height), 1)
        bg_image = ImageTk.PhotoImage(bg_image)
        self.quiz_frame.create_image((self.quiz_frame.winfo_width() - width)/2, (self.quiz_frame.winfo_height() - height)/2, image=bg_image, anchor="nw")

        
        

#Starting Point of Quiz
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Quiz of Vexatious Contemplation")
    window.geometry("634x469")
    window.minsize(634, 469)
    quizStarterObject = StartQuiz(window)
    window.mainloop()
    




