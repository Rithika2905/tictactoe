import tkinter

playerx ="X"
playero ="O"
currentplay = playerx
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

turns =0
over = False

def title(row, column):
    global currentplay
    if board[row][column]["text"] != "":
        return
    if over==True:
        return

    board[row][column]["text"] = currentplay
    if currentplay == playero:
        currentplay =playerx
    else:
        currentplay =playero
    
    label["text"] = currentplay+ " turn"
    return winner()

def winner():
    global turns, over
    turns +=1
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][1]["text"] != ""):
            label.config(text = board[row][0]["text"]+ " is winner!")
            over = True

    for column in range (3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] !=""):
            label.config(text = board[0][column]["text"]+ " is winner!")
            over = True

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] !=""):
            label.config(text = board[0][0]["text"]+ " is winner!")
            over = True

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] !=""):
            label.config(text = board[0][2]["text"]+ " is winner!")
            over = True

    if (turns==9):
            label.config(text="Tie")


def newgame():
    global turns,over
    turns = 0
    over = False
    label.config(text= currentplay+" turn")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="")

window = tkinter.Tk()
window.name="TTT game"
window.resizable(False,False)

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text= currentplay +" turn", font=("Aldhabi", 18))
label.grid(row=0 , column=0, columnspan=3)

for row in range(3):
    for column in range(3):
        board[row][column] =tkinter.Button(frame, text="", font=("Aldhabi", 14), background="#CCCCCC", foreground="black",
                                        width=4, height=1, command= lambda row=row, column=column: title(row, column) )
        board[row][column].grid(row=row+1, column=column)
        

button = tkinter.Button(frame, text=" Go ", font=("Aldhabi", 18), command= newgame )
button.grid(row=4, column=0, columnspan=3)



window.mainloop()