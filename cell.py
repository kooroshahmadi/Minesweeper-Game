from tkinter import Button, Label
from tkinter import messagebox
import tkinter as tk
import random
import setting

class Cell:
    all = []
    cell_count = setting.cell_count
    cell_count_label_object = None

    def __init__(self, root, x, y, is_mine=False):
        self.root = root
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        """Creates a button for the cell and binds left and right click events."""
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind("<Button-1>", self.left_click_action)  # Left click
        btn.bind("<Button-3>", self.right_click_action)  # Right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        """Creates a label to display the number of cells left."""
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            bg="black",
            fg="white",
            font=("Arial", 30, "bold"),
        )
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        """Action to perform on left-click: reveal cell or show mine."""
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == setting.mines_count:
                messagebox.showinfo("Game Over", "You Win!")

        # Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def get_cell_by_axis(self, x, y):
        """Retrieve a cell object by its (x, y) coordinates."""
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        """Get all the cells surrounding the current cell."""
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        """Count the number of mines in the surrounding cells."""
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        """Reveal the cell and update the cell count."""
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
            self.cell_btn_object.configure(bg="light grey")
        self.is_opened = True

    def show_mine(self):
        """Show a mine and end the game."""
        self.cell_btn_object.configure(bg="red")
        messagebox.showinfo("Game Over", "You clicked on a mine! The game will close.")
        self.root.destroy()

    def right_click_action(self, event):
        """Action to perform on right-click: mark or unmark the cell as a mine candidate."""
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="light grey")
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        """Randomly assign mines to a specified number of cells."""
        picked_cells = random.sample(Cell.all, setting.mines_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        """Return a string representation of the cell."""
        return f"Cell({self.x}, {self.y})"
