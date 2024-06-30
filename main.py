import tkinter as tk
from PIL import Image, ImageTk
import random

#5D088E is the primary purple colour for my quiz images
names_store = []
asked_questions = []

questions_and_answers = {
    1: ["What can't you do out of these?", "Sleep on 30th feb", "Fly", "Swim", "Drive", "Sleep on 30th feb", 1],
    2: ["What is the capital of France?", "Paris", "London", "Berlin", "Rome", "Paris", 1]
}

def question_randomiser():
    global qnum
    qnum = random.randint(1,2)
    if qnum not in asked_questions:
        asked_questions.append(qnum)
    elif qnum in asked_questions:
        question_randomiser()

class NameEnter:
    def __init__(self, parent):
        
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(expand=True, fill=tk.BOTH)

        self.enter_name = tk.Entry(self.quiz_canvas, bg="#5D088E", highlightthickness=0, foreground="#edd818", font=("Arial Narrow", 18, "bold"))
        self.enter_name.pack(anchor=tk.CENTER)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("enternamepage.png"))
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()
        self.on_resize()

        
        self.quiz_canvas.bind("<Configure>", self.on_resize)
        self.enter_name.bind("<Return>", self.name_storage)
    
    def on_resize(self, event=None):
        self.bg_image = Image.open("enternamepage.png")

        ratio = self.quiz_canvas.winfo_width() / 634
        print(ratio)
        if 469 * ratio > self.quiz_canvas.winfo_height():
            ratio = self.quiz_canvas.winfo_height() / 469
        print(ratio)

        if ratio <= 0:
            return

        #finding entry box place relative to size of window
        width = int(634 * ratio)
        height = int(469 * ratio)

        if width == 0 or height == 0:
            return

        vertical_gap = (self.quiz_canvas.winfo_height() - height)/2
        horizontal_gap = (self.quiz_canvas.winfo_width() - width)/2
        button_ratio = int(height * 0.644 + vertical_gap)
        self.enter_name.pack_configure(pady=(button_ratio, 0))
        
        self.bg_image = self.bg_image.resize((width, height), 1)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.quiz_canvas.create_image(horizontal_gap, vertical_gap, image=self.bg_image, anchor="nw")

        ratio2 = 250/634
        entry_size = width * ratio2
        self.enter_name.place_configure(x=width/2 - int(entry_size)/2, y=button_ratio, width=int(entry_size))
    
    def name_storage(self, event):
        print("here")
        name = self.enter_name.get()
        if name != "":
            self.quiz_canvas.pack_forget()
            self.quiz_canvas.destroy()
            names_store.append(name)
            print(names_store)
            self.start_page = StartPage(window)
            
class StartPage:
    def __init__(self, parent):
        print("StartPage works")
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(side="top", expand=True, fill=tk.BOTH)
        self.bg_image = ImageTk.PhotoImage(Image.open("resizedstarterpagev2.png"))

        
        self.start_button = tk.Button(self.quiz_canvas, bg="#5D088E", text="Play", command=self.play_button_clicked, font=("Arial Narrow", 9, "bold"), activebackground="#69248f", highlightthickness=0, foreground="#edd818", width=20)
        self.start_button.pack()

        self.howtoplay_button = tk.Button(self.quiz_canvas, command=self.tutorial_button_click, bg="#5D088E", text="How To Play", font=("Arial Narrow", 9, "bold"), activebackground="#69248f", highlightthickness=0, foreground="#edd818", width=20)
        self.howtoplay_button.pack()
        
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()
        self.on_resize()

        self.quiz_canvas.bind("<Configure>", self.on_resize)

        
        window.update()
        print("done")

    #function for "how to play" button clicked
    def tutorial_button_click(self):
        print("clicked")
        self.quiz_canvas.destroy()
        self.start_page = HowToPlayPage(window)

    def play_button_clicked(self):
        print("clicked")
        question_randomiser()
        self.quiz_canvas.destroy()
        self.start_page = QuestionPage(window, qnum)

    #resize components relative to resize of window
    def on_resize(self, event=None):
        self.bg_image = Image.open("resizedstarterpagev2.png")
        
        ratio = self.quiz_canvas.winfo_width() / 634
        print(ratio)
        if 469 * ratio > self.quiz_canvas.winfo_height():
            ratio = self.quiz_canvas.winfo_height() / 469
        print(ratio)

        if ratio <= 0:
            return
    
        #finding entry box place relative to size of window
        width = int(634 * ratio)
        height = int(469 * ratio)

        if width == 0 or height == 0:
            return

        vertical_gap = (self.quiz_canvas.winfo_height() - height)/2
        horizontal_gap = (self.quiz_canvas.winfo_width() - width)/2

        self.bg_image = self.bg_image.resize((width, height), 1)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.quiz_canvas.create_image(horizontal_gap, vertical_gap, image=self.bg_image, anchor="nw")

        #placing buttons relative to size of window
        ratio2 = 290/469
        button_location = int(height * ratio2)
        self.start_button.place_configure(x=width/2 - self.start_button.winfo_width()/2, y=button_location)

        ratio3 = 380/469
        button_location2 = int(height * ratio3)
        self.howtoplay_button.place_configure(x=width/2 - self.start_button.winfo_width()/2, y=button_location2)

class HowToPlayPage:
    def __init__(self, parent):
        print("DONE WOW")
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(expand=True, fill=tk.BOTH)

        self.bg_image = ImageTk.PhotoImage(Image.open("howtoplaypagev2.png"))
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()

        self.instruction_label = tk.Label(self.quiz_canvas, bg="#5D088E", text= "- Click on one of the multichoice answers to", fg="#edd818", font=("Arial Narrow", 13, "bold"))
        self.instruction_label2 = tk.Label(self.quiz_canvas, bg="#5D088E", text= "proceed to the next question", fg="#edd818", font=("Arial Narrow", 13, "bold"))
        self.instruction_label3 = tk.Label(self.quiz_canvas, bg="#5D088E", text= "- You have to think outside the box", fg="#edd818", font=("Arial Narrow", 13, "bold"))
        self.instruction_label4 = tk.Label(self.quiz_canvas, bg="#5D088E", text= "- There's no time limit. Take your time", fg="#edd818", font=("Arial Narrow", 13, "bold"))
        self.instruction_label5 = tk.Label(self.quiz_canvas, bg="#5D088E", text= "- Good luck and have fun!", fg="#edd818", font=("Arial Narrow", 13, "bold"))
        
        self.instruction_label.place(x=100, y=180)
        self.instruction_label2.place(x=100, y=210)
        self.instruction_label3.place(x=100, y=250)
        self.instruction_label4.place(x=100, y=290)
        self.instruction_label5.place(x=100, y=330)
        self.back_button = tk.Button(self.quiz_canvas, command=self.back_button_function, bg="#5D088E", text="Go Back", font=("Arial Narrow", 18, "bold"), fg="#edd818",activebackground="#69248f", highlightthickness=0)

        self.back_button.pack()
        self.back_button.place_configure(x=15, y=415)

    def back_button_function(self):
        print("clicked")
        self.quiz_canvas.destroy()
        self.start_page = StartPage(window)

class QuestionPage:
    def __init__(self, parent, qnum):
        print("Works")
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(expand=True, fill=tk.BOTH)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("questionsbackground.png"))
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()

        
        


#Starting Point of Quiz
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Quiz of Vexatious Contemplation")
    window.geometry("634x469")
    window.minsize(634, 469)
    quizStarterObject = NameEnter(window)
    window.mainloop()
    




