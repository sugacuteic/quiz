import pgzrun, random, time

TITLE = "quiz"
WIDTH = 900
HEIGHT = 700

marquebox = Rect(0,0, 900, 80)
skipbox = Rect(0,0, 150, 330)
timerbox = Rect(0,0, 150, 150)
questionbox = Rect(0,0, 650, 150)
option1 = Rect(0,0, 300, 150)
option2 = Rect(0,0, 300, 150)
option3 = Rect(0,0, 300, 150)
option4 = Rect(0,0, 300, 150)
marquebox.move_ip(0,0)
questionbox.move_ip(20, 100)
skipbox.move_ip(700,270)
timerbox.move_ip(700,100)
option1.move_ip(20,270)
option3.move_ip(20,450)
option2.move_ip(370,270)
option4.move_ip(370,450)
options = [option1, option2, option3, option4]
score = 0
timeleft = 10
mmessage = ""
gameover = False
qbank = "questions.txt"
questions = []
qindex = 0
questioncount = 0

def draw():
    screen.fill("teal")
    screen.draw.filled_rect(marquebox, "black")
    screen.draw.filled_rect(questionbox, "grey")
    screen.draw.filled_rect(skipbox, "blue")
    screen.draw.filled_rect(timerbox, "red")
    for i in options:
        screen.draw.filled_rect(i, "orange")
    mmessage = "Welcome to Quizmaster!"
    mmessage += f"Q: {qindex} of {questioncount}"
    screen.draw.textbox(mmessage, marquebox, color = "white")
    
    
pgzrun.go()


