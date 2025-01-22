import tkinter as tk
from tkinter import font as tkFont
import random
import time
import os

start = False
timeLimit = 5
mistakes = 0
rSol = 0
basedir = os.path.dirname(__file__)

def main():
    global start
    start = True

win = tk.Tk()
win.title("PyMathX")
win.attributes('-fullscreen', True)
win.iconbitmap(os.path.join(basedir, "pilight.ico"))
bimage = tk.PhotoImage(file=os.path.join(basedir, "ui-button.png"))
exitimage = tk.PhotoImage(file=os.path.join(basedir, "exitsmall.png"))

bg_image = tk.PhotoImage(file=os.path.join(basedir, "PyMathXbg.png"))
bg_label = tk.Label(win, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
button = tk.Button(win, text="Start", command=main, image=bimage, compound="center", font=("Helvetica", 50), highlightthickness=0, bd=0, bg="#6abe30", activebackground="#6abe30", activeforeground="black")
text = tk.Label(win, text="Welcome to PyMathX", font=("Helvetica", 50), bg="#6abe30")
mathProblem = tk.Label(win, text="", font=("Helvetica", 80), bg="#6abe30")
timer = tk.Label(win, text="", font=("Helvetica", 50), bg="#6abe30")
mistakesLabel = tk.Label(win, text=f"Mistakes: {mistakes}", font=("Helvetica", 50), bg="#6abe30")
solutionEntry = tk.Entry(win, font=("Helvetica", 50), highlightthickness=0, bd=0, bg="lightblue")
rightSolutionsLabel = tk.Label(win, text=f"Right Solutions: {rSol}", font=("Helvetica", 50), bg="#6abe30")
freeSpace = tk.Frame(win, height=200, width=50, bg="#6abe30")
exit_button = tk.Button(win, image=exitimage, height=35, width=35, command=win.destroy, highlightthickness=0, bd=0, bg="white", activebackground="white")

exit_button.place(relx=1.0, rely=0.0, anchor='ne')
freeSpace.pack()
text.pack()
button.pack()

# Main loop to wait for the start
def wait_for_start():
    global start
    if not start:
        win.after(100, wait_for_start)
    else:
        start_game()

def start_game():
    global mistakes, timeLimit, rSol
    text.pack_forget()
    button.pack_forget()
    rightSolutionsLabel.pack_forget()
    rightSolutionsLabel.config(text=f"Right Solutions: {rSol}")
    rightSolutionsLabel.update()
    mistakesLabel.config(text=f"Mistakes: {mistakes}")
    mistakesLabel.update()
    mathProblem.pack()
    timer.pack()
    solutionEntry.pack()
    mistakesLabel.pack()
    rightSolutionsLabel.pack()

    while mistakes < 3:
        rNum1 = random.randint(1, 10)
        rNum2 = random.randint(1, 10)
        solution = rNum1 * rNum2

        mathProblem.config(text=f"{rNum1} * {rNum2}")
        mathProblem.update()

        timeLimit = 5
        timer.config(text=timeLimit)
        timer.update()
        while True:
            for i in range(100):
                time.sleep(0.01)
                solutionEntry.update()
            timeLimit -= 1
            timer.config(text=timeLimit)
            timer.update()
            if solutionEntry.get() == str(solution):
                rSol += 1
                break
            if timeLimit == 0:
                mistakes += 1
                mistakesLabel.config(text=f"Mistakes: {mistakes}")
                mistakesLabel.update()
                mathProblem.config(text=f"Solution: {solution}")
                mathProblem.update()
                time.sleep(1)
                break
        rightSolutionsLabel.config(text=f"Right Solutions: {rSol}")
        rightSolutionsLabel.update()
        solutionEntry.delete(0, tk.END)
    text.config(text="Game Over")
    button.config(text="Retry", command=start_game)
    text.pack()
    button.pack()
    mistakes = 0
    rSol = 0
    mistakesLabel.update()
    timer.pack_forget()
    solutionEntry.pack_forget()
    mistakesLabel.pack_forget()
    mathProblem.pack_forget()
    

wait_for_start()
win.mainloop()
