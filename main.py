import tkinter as tk
from PIL import Image, ImageTk
import random
import time

#5D088E is the primary purple colour for my quiz images
names_store = []
asked_questions = []
player_score = 0

questions_and_answers = {
    1: ["What can't you do out of these?", "Sleep on 30th feb", "Fly", "Swim", "Drive", "Sleep on 30th feb", 1],
    2: ["What is the capital of France?", "Paris", "London", "Berlin", "Rome", "Paris", 1],
    3: ["What is the capital of Germany?", "Paris", "London", "Berlin", "Rome", "Berlin", 3],
    4: ["What is the capital of Italy?", "Paris", "London", "Berlin", "Rome", "Rome", 4],
    5: ["What is the capital of Spain?", "Paris", "Madrid", "Berlin", "Madrid", "Madrid", 2]
}

def question_randomiser():
    global qnum
    qnum = random.randint(1,5)
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
        
        self.question = tk.Label(self.quiz_canvas, fg="#5D088E", bg="#F3D915", text=questions_and_answers[qnum][0], font=("Arial Narrow", 24, "bold"))
        self.question.grid(row=1, padx=30, pady=40)

        self.var1 = tk.IntVar()

        self.answer1 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[qnum][1], value=1, variable=self.var1, font=("Arial Narrow", 18), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer1.grid(row=2)

        self.answer2 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[qnum][2], value=2, variable=self.var1, font=("Arial Narrow", 18), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer2.grid(row=3)

        self.answer3 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[qnum][3], value=3, variable=self.var1, font=("Arial Narrow", 18), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer3.grid(row=4)

        self.answer4 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[qnum][4], value=4, variable=self.var1, font=("Arial Narrow", 18), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer4.grid(row=5)

        self.confirm_button = tk.Button(self.quiz_canvas, bg="#5D088E", text="Confirm", command=self.test_progress, fg="#edd818", highlightthickness=0, font=("Arial Narrow", 18, "bold"))
        self.confirm_button.grid(row=6, pady=20)

        self.score_display = tk.Label(self.quiz_canvas, text="Score",  bg="#5D088E", fg="#edd818", font=("Arial Narrow", 18))
        self.score_display.grid(row=7, pady=5)
    
    def next_question(self):
        question_randomiser()
        self.var1.set(0)
        self.question.config(text=questions_and_answers[qnum][0])

        self.answer1.config(text=questions_and_answers[qnum][1])
        self.answer2.config(text=questions_and_answers[qnum][2])
        self.answer3.config(text=questions_and_answers[qnum][3])
        self.answer4.config(text=questions_and_answers[qnum][4])

    def test_progress(self):
        global player_score
        score_label = self.score_display
        selection = self.var1.get()
        if len(asked_questions) > 4:
            if selection == questions_and_answers[qnum][6]:
                player_score += 1
                score_label.config(text="Score: " + str(player_score))
                self.confirm_button.config(text="Confirm")
            elif selection == 0:
                self.confirm_button.config(text="Please select an answer")
                selection = self.var1.get()
            else:
                player_score += 0
                score_label.config(text="The correct answer was: " + questions_and_answers[qnum][5])
                self.confirm_button.config(text="Confirm")
        else:
            if selection == 0:
                self.confirm_button.config(text="Please select an answer")
                selection = self.var1.get()
            else:
                if selection == questions_and_answers[qnum][6]:
                    player_score += 1
                    score_label.config(text="Score: " + str(player_score))
                    self.next_question()
                    self.confirm_button.config(text="Confirm")
                else:
                    player_score += 0
                    score_label.config(text="The correct answer was: " + questions_and_answers[qnum][5])
                    self.confirm_button.config(text="Confirm")
                    self.next_question()
        

#Starting Point of Quiz
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Quiz of Vexatious Contemplation")
    window.geometry("634x469")
    window.minsize(634, 469)
    quizStarterObject = NameEnter(window)
    window.mainloop()
    




