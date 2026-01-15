import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black")
        self.canvas.pack()

        self.score = 0
        self.speed = 100  # initial speed (lower number = faster speed)
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake coordinates
        self.snake_direction = "Right"
        self.food = None
        self.game_running = True

        self.create_food()
        self.update_snake()

        self.label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14), fg="white", bg="black")
        self.label.pack()

        self.replay_button = tk.Button(self.root, text="Replay", font=("Arial", 14), command=self.restart_game)
        self.replay_button.pack()
        self.replay_button.config(state=tk.DISABLED)

        self.root.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def run_game(self):
        if self.game_running:
            self.move_snake()
            self.check_collision()
            self.check_food_collision()
            self.update_snake()

            self.root.after(self.speed, self.run_game)  # Set speed based on the `speed` variable
        else:
            self.canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 30))
            self.replay_button.config(state=tk.NORMAL)

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.snake_direction == "Up":
            head_y -= 10
        elif self.snake_direction == "Down":
            head_y += 10
        elif self.snake_direction == "Left":
            head_x -= 10
        elif self.snake_direction == "Right":
            head_x += 10

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def change_direction(self, event):
        if event.keysym == "Up" and self.snake_direction != "Down":
            self.snake_direction = "Up"
        elif event.keysym == "Down" and self.snake_direction != "Up":
            self.snake_direction = "Down"
        elif event.keysym == "Left" and self.snake_direction != "Right":
            self.snake_direction = "Left"
        elif event.keysym == "Right" and self.snake_direction != "Left":
            self.snake_direction = "Right"

    def check_collision(self):
        head_x, head_y = self.snake[0]

        # Check wall collision
        if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
            self.game_running = False

        # Check self-collision
        if (head_x, head_y) in self.snake[1:]:
            self.game_running = False

    def check_food_collision(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food

        if head_x == food_x and head_y == food_y:
            self.snake.append(self.snake[-1])  # Add a new segment to the snake
            self.create_food()
            self.score += 10  # Increment score
            self.speed = max(50, self.speed - 5)  # Speed up, but keep a minimum speed

            self.label.config(text=f"Score: {self.score}")

    def create_food(self):
        food_x = random.randint(0, 59) * 10
        food_y = random.randint(0, 39) * 10
        self.food = (food_x, food_y)

    def update_snake(self):
        self.canvas.delete("all")

        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")

        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red")

    def restart_game(self):
        # Reset all game variables and restart the game
        self.score = 0
        self.speed = 100
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = "Right"
        self.game_running = True
        self.create_food()
        self.update_snake()
        self.label.config(text=f"Score: {self.score}")
        self.replay_button.config(state=tk.DISABLED)
        self.run_game()


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
