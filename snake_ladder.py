import tkinter as tk
from tkinter import messagebox
import random

# Snake and ladder positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
          64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
           36: 44, 51: 67, 71: 91, 80: 100}


class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake & Ladder Game 🐍🎲")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.positions = {1: 0, 2: 0}
        self.current_player = 1
        self.cell_size = 60

        self.draw_board()
        self.draw_snakes_ladders()

        # Tokens (drawn as colored ovals)
        self.tokens = {
            1: self.canvas.create_oval(10, 560, 30, 580, fill="red"),
            2: self.canvas.create_oval(30, 560, 50, 580, fill="blue")
        }

        self.roll_btn = tk.Button(root, text="🎲 Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.roll_btn.grid(row=1, column=0, pady=10)

        self.dice_label = tk.Label(root, text="", font=("Arial", 20))
        self.dice_label.grid(row=1, column=1)

        self.status_label = tk.Label(root, text="Player 1's Turn", font=("Arial", 14, "bold"))
        self.status_label.grid(row=1, column=2)

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                board_row = 9 - row
                board_col = col if board_row % 2 == 0 else 9 - col
                number = board_row * 10 + board_col + 1
                fill = "#f0f8ff" if number % 2 == 0 else "#e0ffff"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="gray")
                self.canvas.create_text(x1 + 30, y1 + 30, text=str(number), font=("Arial", 10, "bold"))

    def draw_snakes_ladders(self):
        for start, end in snakes.items():
            self.draw_line(start, end, "darkred", True)
        for start, end in ladders.items():
            self.draw_line(start, end, "green", False)

    def draw_line(self, start, end, color, curve=False):
        x1, y1 = self.get_coords(start)
        x2, y2 = self.get_coords(end)
        if curve:
            self.canvas.create_line(x1, y1, (x1 + x2) // 2, (y1 + y2) // 2 - 30, x2, y2,
                                    fill=color, width=4, smooth=True)
        else:
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=4)

    def get_coords(self, pos):
        if pos == 0:
            return 30, 570
        row = (pos - 1) // 10
        col = (pos - 1) % 10 if row % 2 == 0 else 9 - (pos - 1) % 10
        x = col * self.cell_size + 10
        y = (9 - row) * self.cell_size + 10
        return x, y

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.dice_label.config(text=f"🎲 {roll}")
        self.root.after(500, lambda: self.move_player(roll))

    def move_player(self, roll):
        current = self.positions[self.current_player]
        next_pos = current + roll

        if next_pos > 100:
            next_pos = current

        if next_pos in snakes:
            self.status_label.config(text=f"🐍 Snake! Down to {snakes[next_pos]}")
            next_pos = snakes[next_pos]
        elif next_pos in ladders:
            self.status_label.config(text=f"🪜 Ladder! Up to {ladders[next_pos]}")
            next_pos = ladders[next_pos]
        else:
            self.status_label.config(text=f"Player {self.current_player} to {next_pos}")

        self.positions[self.current_player] = next_pos
        x, y = self.get_coords(next_pos)
        self.canvas.coords(self.tokens[self.current_player], x, y, x + 20, y + 20)

        if next_pos == 100:
            messagebox.showinfo("🎉 Game Over", f"Player {self.current_player} wins!")
            self.root.quit()
        else:
            if roll != 6:
                self.current_player = 2 if self.current_player == 1 else 1
            self.status_label.config(text=f"Player {self.current_player}'s Turn")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
