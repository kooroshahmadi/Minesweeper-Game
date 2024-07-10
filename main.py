from tkinter import *
import setting
import utils
from cell import Cell

# Initialize the main window
root = Tk()

# Set the size of the main window
root.geometry(f"{setting.width}x{setting.height}")
root.resizable(False, False)  # Disable window resizing

# Set the title of the main window
root.title("MineSweeperGame")

# Set the background color of the main window
root.configure(bg="black")

# Create frames
# Top frame: occupies 25% of the window height
top_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(100),
    height=utils.height_prct(25),
)
top_frame.place(x=0, y=0)

# Add the game title to the top frame
game_title = Label(
    top_frame,
    text="Minesweeper",
    bg="black",
    fg="white",
    font=("Arial", 30, "bold"),
)
game_title.place(x=utils.width_prct(25), y=0)

# Left frame: occupies 25% of the window width and 75% of the window height
left_frame = Frame(
    root, bg="black", width=utils.width_prct(25), height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

# Center frame: occupies 75% of the window width and 75% of the window height
center_frame = Frame(
    root, bg="black", width=utils.width_prct(75), height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# Create cells in the center frame
for x in range(setting.grid_size):
    for y in range(setting.grid_size):
        c = Cell(root, x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(row=y, column=x)

# Create and place the cell count label in the left frame
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

# Randomly assign mines to cells
Cell.randomize_mines()

# Run the main event loop
root.mainloop()
