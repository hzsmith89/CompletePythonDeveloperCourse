from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

# Global Variables
active_player = 1
player1 = []  # What Player 1 Selected
player2 = []  # What Player 2 Selected

root = Tk()
root.title("Tic Tac Toe: Player 1")

# This was lame
# style = ttk.Style()
# style.theme_use('classic')

button1 = ttk.Button(root, text=" ")
button1.grid(row=0, column=0, sticky="nsew", ipadx=40, ipady=40)
button1.config(command=lambda: button_click(1))

button2 = ttk.Button(root, text=" ")
button2.grid(row=0, column=1, sticky="nsew", ipadx=40, ipady=40)
button2.config(command=lambda: button_click(2))

button3 = ttk.Button(root, text=" ")
button3.grid(row=0, column=2, sticky="nsew", ipadx=40, ipady=40)
button3.config(command=lambda: button_click(3))

button4 = ttk.Button(root, text=" ")
button4.grid(row=1, column=0, sticky="nsew", ipadx=40, ipady=40)
button4.config(command=lambda: button_click(4))

button5 = ttk.Button(root, text=" ")
button5.grid(row=1, column=1, sticky="nsew", ipadx=40, ipady=40)
button5.config(command=lambda: button_click(5))

button6 = ttk.Button(root, text=" ")
button6.grid(row=1, column=2, sticky="nsew", ipadx=40, ipady=40)
button6.config(command=lambda: button_click(6))

button7 = ttk.Button(root, text=" ")
button7.grid(row=2, column=0, sticky="nsew", ipadx=40, ipady=40)
button7.config(command=lambda: button_click(7))

button8 = ttk.Button(root, text=" ")
button8.grid(row=2, column=1, sticky="nsew", ipadx=40, ipady=40)
button8.config(command=lambda: button_click(8))

button9 = ttk.Button(root, text=" ")
button9.grid(row=2, column=2, sticky="nsew", ipadx=40, ipady=40)
button9.config(command=lambda: button_click(9))


def button_click(button_id):
    global active_player
    global player1
    global player2

    if active_player == 1:
        set_layout(button_id, "X")
        player1.append(button_id)
        print("Player1: {}".format(player1))
        winner = check_winner(player1)

        if winner:
            root.title("Winner Player 1!!!")
            messagebox.showinfo("Congrats!!", "Player 1 Wins!!!")
        else:
            root.title("Tic Tac Toe: Player 2")
            active_player = 2
            auto_play()

    elif active_player == 2:
        set_layout(button_id, "O")
        player2.append(button_id)
        print("Player2: {}".format(player2))
        winner = check_winner(player2)

        if winner:
            root.title("Winner Player 2!!!")
            messagebox.showinfo("Congrats!!", "Player 2 Wins!!!")
        else:
            root.title("Tic Tac Toe: Player 1")
            active_player = 1


def set_layout(button_id, player_symbol):
    if button_id == 1:
        button1.config(text=player_symbol)
        button1.state(['disabled'])

    elif button_id == 2:
        button2.config(text=player_symbol)
        button2.state(['disabled'])

    elif button_id == 3:
        button3.config(text=player_symbol)
        button3.state(['disabled'])

    elif button_id == 4:
        button4.config(text=player_symbol)
        button4.state(['disabled'])

    elif button_id == 5:
        button5.config(text=player_symbol)
        button5.state(['disabled'])

    elif button_id == 6:
        button6.config(text=player_symbol)
        button6.state(['disabled'])

    elif button_id == 7:
        button7.config(text=player_symbol)
        button7.state(['disabled'])

    elif button_id == 8:
        button8.config(text=player_symbol)
        button8.state(['disabled'])

    else:
        button9.config(text=player_symbol)
        button9.state(['disabled'])


def check_winner(player):
    winner = False

    # Checks first row
    if 1 in player and 2 in player and 3 in player:
        winner = True
    # Checks second row
    elif 4 in player and 5 in player and 6 in player:
        winner = True
    # Checks third row
    elif 7 in player and 8 in player and 9 in player:
        winner = True
    # Checks first column
    elif 1 in player and 4 in player and 7 in player:
        winner = True
    # Checks second column
    elif 2 in player and 5 in player and 8 in player:
        winner = True
    # Checks third column
    elif 3 in player and 6 in player and 9 in player:
        winner = True
    # Checks top-left to bottom-right diagonal
    elif 1 in player and 5 in player and 9 in player:
        winner = True
    # Checks bottom-left to top-right diagonal
    elif 3 in player and 5 in player and 7 in player:
        winner = True
    else:
        print("Keep Going")

    if winner:
        print("Winner!!")
        disable_buttons()

    return winner


def disable_buttons():

    button1.state(['disabled'])
    button2.state(['disabled'])
    button3.state(['disabled'])
    button4.state(['disabled'])
    button5.state(['disabled'])
    button6.state(['disabled'])
    button7.state(['disabled'])
    button8.state(['disabled'])
    button9.state(['disabled'])


def auto_play():

    empty_cells = []

    for cell in range(1, 10):
        if not (cell in player1 or cell in player2):
            empty_cells.append(cell)

    print(empty_cells)

    if len(empty_cells) > 0:
        rand_index = randint(0, len(empty_cells) - 1)
        button_click(empty_cells[rand_index])
    else:
        messagebox.showinfo("Congrats??", "It's a draw!!")


root.mainloop()
