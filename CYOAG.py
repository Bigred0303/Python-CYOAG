import random
import time, sys, string
import tkinter as tk
from tkinter import *
#from playsound import playsound
# add other imports like sound here



def hackChallenge(numberOfCharacters, duration):
    timeGiven = duration
    startLine = "The code is ready, you will have to enter " + str(numberOfCharacters) +" characters, you only have " + str(timeGiven) +" seconds, you only have one shot!\n The code will appear below:"
    challenge = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(numberOfCharacters))
    global startedHack
    startedHack = False
    global finishedHack
    finishedHack = False

    def quitHack():
        root.quit()

    def hackChallengeStart():
        if finishedHack == False:
            win = False
            global startedHack
            startedHack = True
            challengeText = tk.Label(root, text=challenge)
            challengeText.config(font=("helvetica", 12, "bold"))
            global startTime
            startTime = time.time()
            canvas.create_window(200, 120, window=challengeText)

    def hackChallengeFinish():
        global finishedHack
        global win
        if finishedHack == False:
            submission = answer.get()
            global startedHack
            if submission != "" and startedHack == True:
                endTime = time.time()
                global startTime
                elapsedTime = endTime - startTime
                timeLeft = int(timeGiven - elapsedTime)
                if submission == challenge and elapsedTime < timeGiven:
                    winMessage = "You did it, wonderful! With " + str(timeLeft) + " seconds to spare!"
                    winText = tk.Label(root, text=winMessage)
                    winText.config(fg="green" , font =('helvetica', 12, "italic"))
                    canvas.create_window(200, 250, window=winText)
                    finishedHack = True
                    win = True
                else:
                    loseMessage = "You failed, that was it, it's all over now..."
                    loseText = tk.Label(root, text=loseMessage)
                    loseText.config(fg="red", font =('helvetica', 12, "italic"))
                    canvas.create_window(200, 250, window=loseText)
                    win = False
                    finishedHack = True
                quitButton = Button(root, text="Leave hacking terminal", command=quitHack, bg="pink",font =('helvetica', 10))
                canvas.create_window(200, 280, window=quitButton)

    root = tk.Tk()
    canvas = tk.Canvas(root, width = 400, height = 300)
    canvas.pack()
    answer = tk.Entry(root)
    startText = Label(root, text=startLine)
    startText.config(font =('helvetica', 12))
    startButton = Button(root, text ="Click to start hacking", command= hackChallengeStart, bg="lightyellow", font =('helvetica', 10))
    submitButton = Button(root, text ="Submit", command= hackChallengeFinish, bg="lightblue", font =('helvetica', 10))
    canvas.create_window(200, 220, window=startButton)
    canvas.create_window(200, 80, window=startText)
    canvas.create_window(200, 180, window=submitButton)
    canvas.create_window(200, 150, window=answer)
    root.mainloop()
    return win

print(hackChallenge(10, 20))
