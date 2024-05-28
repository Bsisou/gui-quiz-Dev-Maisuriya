import tkinter as tk
from PIL import Image, ImageTk

#5D088E is the primary purple colour for my quiz images
namesList = []
asked = []

class StartQuiz:
    def __init__(self, parent):
        self.quiz_frame = tk.Canvas(parent, bg="#290f42")
        self.quiz_frame.pack(expand=True, fill=tk.BOTH)
        bg_image = Image.open("enternamepage.png")
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_entry_colour = "#5D088E"
        self.enter_name = tk.Entry(self.quiz_frame, bg=bg_entry_colour, highlightthickness=0, foreground="#edd818", font=("Arial Narrow", 18, "bold"))
        self.enter_name.pack(anchor=tk.CENTER)
        
        self.quiz_frame.create_image(0, 0, image=bg_image, anchor="nw")
        
        window.bind("<Configure>", self.on_resize)
        window.bind('<Return>', self.name_storage)
    
    def on_resize(self, event):

        global bg_image
        bg_image = Image.open("enternamepage.png")

        ratio = self.quiz_frame.winfo_width() / 634
        print(ratio)
        if 469 * ratio > self.quiz_frame.winfo_height():
            ratio = self.quiz_frame.winfo_height() / 469
        print(ratio)

        if ratio <= 0:
            return

        #finding entry box place relative to size of window
        width = int(634 * ratio)
        height = int(469 * ratio)

        vertical_gap = (self.quiz_frame.winfo_height() - height)/2
        horizontal_gap = (self.quiz_frame.winfo_width() - width)/2
        button_ratio = int(height * 0.644 + vertical_gap)
        self.enter_name.pack_configure(pady=(button_ratio, 0))
        
        bg_image = bg_image.resize((width, height), 1)
        bg_image = ImageTk.PhotoImage(bg_image)
        self.quiz_frame.create_image(horizontal_gap, vertical_gap, image=bg_image, anchor="nw")

        ratio2 = 250/634
        entry_size = width * ratio2
        self.enter_name.place_configure(x=width/2 - int(entry_size)/2, y=button_ratio, width=int(entry_size))
    def name_storage(self, event):
      name = self.enter_name.get()
      if name != "":
        self.quiz_frame.destroy()
        namesList.append(name)
        print(namesList)
        StartQuiz(window)

#Starting Point of Quiz
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Quiz of Vexatious Contemplation")
    window.geometry("634x469")
    window.minsize(634, 469)
    quizStarterObject = StartQuiz(window)
    window.mainloop()
    




