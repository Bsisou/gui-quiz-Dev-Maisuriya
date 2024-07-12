import tkinter as tk
from PIL import Image, ImageTk
import random

#5D088E is the primary purple colour for my quiz images
names_store = []
asked_questions = []

questions_and_answers = {
    1: ["What can't you do out of these?", "Sleep on 30th feb", "Fly", "Swim", "Drive", "Sleep on 30th feb", 1],
    2: ["What has an eye but can't see?", "Needle", "Hurricane", "Blind Man", "Owl", "Needle", 1],
    3: ["What belongs to you but others use it more than you do?", "Your Money", "Your Ideas", "Your Time", "Your Name", "Your Name", 4],
    4: ["What travels around the world while staying in a corner?", "Globe", "Stamp", "Postage", "Airplane", "Stamp", 2],
    5: ["Forward I am heavy, but backward I am not. What am I?", "Stone", "Weight", "Ton", "Not", "Ton", 3],
    6: ["What has cities but no houses, forests but no trees?", "Map", "Book", "Atlas", "Globe", "Map", 1],
    7: ["What can you hold without ever using your hands?", "Breath", "Thought", "Air", "Sight", "Air", 3],
    8: ["What gets wetter as it dries?", "Sponge", "Towel", "Soap", "Cloth", "Towel", 2],
    9: ["What has a neck but no head?", "Bottle", "Shirt", "Cup", "Shoe", "Bottle", 1],
    10: ["What has one head, one foot, and four legs?", "Bed", "Chair", "Table", "Clock", "Table", 3]
}

class NameEnter:
    #initializes all the objects inside of the NameEnter class
    def __init__(self, parent):
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(expand=True, fill=tk.BOTH)

        self.enter_name = tk.Entry(self.quiz_canvas, bg="#5D088E", highlightthickness=0, foreground="#edd818", font=("Arial Narrow", 18, "bold"))
        self.enter_name.pack(anchor=tk.CENTER)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("enternamepage.png"))
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()
        self.on_resize()

        self.next_button = tk.Button(self.quiz_canvas, command=self.to_start_page, bg="#5D088E", text="Next", font=("Arial Narrow", 18, "bold"), fg="#edd818",activebackground="#69248f", highlightthickness=0)
        self.next_button.place(x=530, y=390)
        
        self.quiz_canvas.bind("<Configure>", self.on_resize)
        self.enter_name.bind("<Return>", self.name_storage)

    #function for resizing the canvas
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

    #function for storing the name and intialising the next class
    def name_storage(self, event):
        print("here")
        name = self.enter_name.get()
        if name != "":
            self.quiz_canvas.pack_forget()
            self.quiz_canvas.destroy()
            names_store.append(name)
            print(names_store)
            self.start_page = StartPage(window)

    def to_start_page(self):
        name = self.enter_name.get()
        if name != "":
            self.quiz_canvas.destroy()
            self.start_page = StartPage(window)
        
class StartPage:
    #initializes all the objects inside of the StartPage class
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

    #function for "play" button clicked
    def play_button_clicked(self):
        print("clicked")
        self.quiz_canvas.destroy()
        self.start_page = QuestionPage(window)

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
    #initializes all the objects inside of the HowToPlay class
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

    #function for "go back" button clicked leading back to start page
    def back_button_function(self):
        print("clicked")
        self.quiz_canvas.destroy()
        self.start_page = StartPage(window)

class QuestionPage:
    #initializes all the objects inside of the QuestionPage class
    def __init__(self, parent):

        self.question_randomiser()
        
        print("Works")
        player_score = 0
        self.player_score = player_score
        self.quiz_canvas = tk.Canvas(parent, bg="#290f42")
        self.quiz_canvas.pack(expand=True, fill=tk.BOTH)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("questionsbackground.png"))
        self.quiz_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        window.update()
        
        self.question = tk.Label(self.quiz_canvas, fg="#5D088E", bg="#F3D915", text=questions_and_answers[self.qnum][0], font=("Arial Narrow", 14, "bold"))
        self.question.pack(pady=(30, 80))

        self.var1 = tk.IntVar()

        self.answer1 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[self.qnum][1], value=1, variable=self.var1, font=("Arial Narrow", 15), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer1.pack()

        self.answer2 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[self.qnum][2], value=2, variable=self.var1, font=("Arial Narrow", 15), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer2.pack()

        self.answer3 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[self.qnum][3], value=3, variable=self.var1, font=("Arial Narrow", 15), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer3.pack()

        self.answer4 = tk.Radiobutton(self.quiz_canvas, text=questions_and_answers[self.qnum][4], value=4, variable=self.var1, font=("Arial Narrow", 15), bg="#5D088E", fg="#F3D915", highlightthickness=0, pady=10)
        self.answer4.pack()

        self.confirm_button = tk.Button(self.quiz_canvas, bg="#5D088E", text="Confirm", command=self.quiz_progress, fg="#edd818", highlightthickness=0, font=("Arial Narrow", 15, "bold"))
        self.confirm_button.pack(pady=(10,0))

        self.warning_label = tk.Label(self.quiz_canvas, bg="#5D088E", fg="#edd818", highlightthickness=0, font=("Arial Narrow", 15, "bold"))
        self.warning_label.pack(pady=(10,0))
        
        self.score_display = tk.Label(self.quiz_canvas, text="Score",  bg="#5D088E", fg="#edd818", font=("Arial Narrow", 15))
        self.score_display.pack(pady=(10,0))

    #function for randomising questions from the dictionary
    def question_randomiser(self):
        self.qnum = random.randint(1,10)
        if self.qnum not in asked_questions:
            asked_questions.append(self.qnum)
        elif self.qnum in asked_questions:
            self.question_randomiser()
    
    #function for "confirm" button clicked setting up the next question
    def next_question(self):
        self.question_randomiser()
        self.var1.set(0)
        self.question.config(text=questions_and_answers[self.qnum][0])

        self.answer1.config(text=questions_and_answers[self.qnum][1])
        self.answer2.config(text=questions_and_answers[self.qnum][2])
        self.answer3.config(text=questions_and_answers[self.qnum][3])
        self.answer4.config(text=questions_and_answers[self.qnum][4])

    #function for "quit" button clicked, closing the window
    def end_program(self):
        window.withdraw()

    #function to handle right answers and wrong answers, and when to end the quiz
    def quiz_progress(self):
        score_label = self.score_display
        selection = self.var1.get()
        if len(asked_questions) > 9:
            if selection == questions_and_answers[self.qnum][6]:
                self.player_score += 1
                score_label.config(text="Score: " + str(self.player_score))
                self.confirm_button.config(text="Quit", command=self.end_program)
            elif selection == 0:
                self.warning_label.config(text="Please select an answer")
                selection = self.var1.get()
            else:
                self.player_score += 0
                score_label.config(text="Score: " + str(self.player_score))
                self.confirm_button.config(text="Quit", command=self.end_program)
        else:
            if selection == 0:
                self.warning_label.config(text="Please select an answer")
                selection = self.var1.get()
            else:
                if selection == questions_and_answers[self.qnum][6]:
                    self.player_score += 1
                    score_label.config(text="Score: " + str(self.player_score))
                    self.next_question()
                    self.confirm_button.config(text="Confirm")
                else:
                    self.player_score += 0
                    self.warning_label.config(text="The correct answer was: " + questions_and_answers[self.qnum][5])
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
    




