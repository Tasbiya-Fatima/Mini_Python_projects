import tkinter as tk
import random

class FallingObjectsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Falling Objects")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="lightblue")
        self.canvas.pack()

        self.basket_width = 60
        self.basket = self.canvas.create_rectangle(270, 350, 330, 370, fill="green")
        self.basket_speed = 20

        self.objects = []
        self.score = 0
        self.lives = 3
        self.game_running = True
        self.fall_speed = 15  # Increased fall speed to slow down falling objects

        # Score and Lives Labels
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.lives_label = tk.Label(self.root, text=f"Lives: {self.lives}", font=("Arial", 14))
        self.lives_label.pack()

        # Replay Button
        self.replay_button = tk.Button(self.root, text="Replay", font=("Arial", 14), command=self.restart_game)
        self.replay_button.pack()
        self.replay_button.config(state=tk.DISABLED)

        # Controls for moving the basket
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.create_object()
        self.run_game()

    def run_game(self):
        if self.game_running:
            self.move_objects()
            self.check_collisions()
            self.update_objects()

            self.root.after(self.fall_speed, self.run_game)  # Falling speed controlled by `fall_speed`
        else:
            self.canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 30))
            self.replay_button.config(state=tk.NORMAL)

    def create_object(self):
        object_x = random.randint(0, 580)
        object_type = random.choice(["fruit", "bomb"])
        object_color = "red" if object_type == "fruit" else "black"
        object = self.canvas.create_oval(object_x, 0, object_x + 20, 20, fill=object_color)
        self.objects.append((object, object_type))

    def move_objects(self):
        for obj, obj_type in self.objects:
            self.canvas.move(obj, 0, 3)  # Reduced speed (fall slower)

        # Remove objects that have fallen out of the screen
        for obj, _ in self.objects[:]:
            _, y1, _, y2 = self.canvas.coords(obj)
            if y2 >= 400:
                self.objects.remove((obj, _))
                self.canvas.delete(obj)
                self.create_object()

    def check_collisions(self):
        basket_coords = self.canvas.coords(self.basket)
        basket_x1, basket_y1, basket_x2, basket_y2 = basket_coords

        for obj, obj_type in self.objects[:]:
            object_coords = self.canvas.coords(obj)
            object_x1, object_y1, object_x2, object_y2 = object_coords

            if object_y2 >= basket_y1 and object_x1 >= basket_x1 and object_x2 <= basket_x2:
                # Catch fruit
                if obj_type == "fruit":
                    self.score += 10
                    self.canvas.delete(obj)
                    self.objects.remove((obj, obj_type))
                    self.create_object()
                # Catch bomb
                elif obj_type == "bomb":
                    self.lives -= 1
                    self.canvas.delete(obj)
                    self.objects.remove((obj, obj_type))
                    self.create_object()

        # Update score and lives display
        self.score_label.config(text=f"Score: {self.score}")
        self.lives_label.config(text=f"Lives: {self.lives}")

        # Check for game over
        if self.lives <= 0:
            self.game_running = False

    def update_objects(self):
        # Update all falling objects
        for obj, obj_type in self.objects:
            if self.canvas.coords(obj)[3] > 400:
                self.canvas.delete(obj)
                self.objects.remove((obj, obj_type))

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.basket)
        if x1 > 0:
            self.canvas.move(self.basket, -self.basket_speed, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.basket)
        if x2 < 600:
            self.canvas.move(self.basket, self.basket_speed, 0)

    def restart_game(self):
        # Reset all game variables and restart the game
        self.score = 0
        self.lives = 3
        self.fall_speed = 15  # Reset falling speed to the original slower value
        self.game_running = True
        self.objects = []
        self.create_object()
        self.update_objects()
        self.score_label.config(text=f"Score: {self.score}")
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.replay_button.config(state=tk.DISABLED)
        self.run_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = FallingObjectsGame(root)
    root.mainloop()
