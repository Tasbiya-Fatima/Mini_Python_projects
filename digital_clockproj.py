import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the window size
root.geometry("400x200")

# Set the font and color for the clock
clock_label = tk.Label(root, font=("Helvetica", 50), bg="black", fg="white")
clock_label.pack(expand=True)

# Function to update the time on the clock
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every second

# Start the time update function
update_time()

# Run the Tkinter event loop
root.mainloop()
