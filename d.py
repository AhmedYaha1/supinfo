import tkinter as tk

class Case:
    def __init__(self, tokens, player):
        self.tokens = tokens
        self.player = player

class Jeu:
    def __init__(self, num_rows, num_cols, num_players):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_players = num_players
        self.board = [[Case(0, 0) for j in range(num_cols)] for i in range(num_rows)]
        self.root = tk.Tk()
        self.root.title("My Game")
        self.grid = []
        self.canvas = tk.Canvas(self.root, width=num_cols*50, height=num_rows*50)
        self.canvas.pack()
        self.current_player = 1
        self.colors = ["blue", "red", "green", "yellow", "purple", "orange", "pink", "brown"]
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                x1 = j * 50
                y1 = i * 50
                x2 = x1 + 50
                y2 = y1 + 50
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                self.canvas.tag_bind(rect, '<Button-1>', lambda event, row=i, col=j: self.on_rectangle_click(event, row, col))
                row.append(rect)
            self.grid.append(row)

    def on_rectangle_click(self, event, row, col):
        self.board[row][col].tokens += 1
        self.board[row][col].player = self.current_player
        x1, y1, x2, y2 = self.canvas.coords(self.grid[row][col])
        x1 += 20
        y1 += 20
        x2 -= 20
        y2 -= 20
        self.circle = self.canvas.create_oval(x1, y1, x2, y2, fill=self.colors[self.current_player-1])
        self.current_player = (self.current_player % self.num_players) + 1

def on_submit():
    num_rows = int(row_entry.get())
    num_cols = int(col_entry.get())
    num_players = int(players_entry.get())
    if num_rows < 3 or num_rows > 10:
        raise ValueError("Number of rows must be between 3 and 10.")
    if num_cols < 3 or num_cols > 12:
        raise ValueError("Number of columns must be between 3 and 12.")
    if num_players < 2 or num_players > 8:
        raise ValueError("Number of players must be between 2 and 8.")
    game = Jeu(num_rows, num_cols, num_players)

root = tk.Tk()
root.title("My Game")

row_label = tk.Label(root, text="Enter the number of rows:")
row_label.grid(row=0, column=0)
row_entry = tk.Entry(root)
row_entry.grid(row=0, column=1)

col_label = tk.Label(root, text="Enter the number of columns:")
col_label.grid(row=1, column=0)
col_entry = tk.Entry(root)
col_entry.grid(row=1, column=1)

players_label = tk.Label(root, text="Enter the number of players:")
players_label.grid(row=2, column=0)
players_entry = tk.Entry(root)
players_entry.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=1)

root.mainloop()


