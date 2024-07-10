# Minesweeper-Game
This is a simple implementation of the classic Minesweeper game using Python's Tkinter library. The game features a grid of cells, some of which are randomly assigned as mines. The player must click on cells to reveal them, trying to avoid clicking on mines. The game is won when all non-mine cells are revealed. 
Here's a comprehensive documentation for your Minesweeper game project, suitable for your GitHub page:

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Files](#files)
   - [main.py](#mainpy)
   - [cell.py](#cellpy)
   - [utils.py](#utilspy)
   - [setting.py](#settingpy)
4. [running on windows](#windows)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/minesweeper-game.git
   cd minesweeper-game
   ```

2. Ensure you have Python installed (preferably Python 3.8 or higher).

3. Install Tkinter if it is not already installed. On Debian-based systems:
   ```sh
   sudo apt-get install python3-tk
   ```

## Usage

Run the game by executing the `main.py` file:
```sh
python main.py
```

## Files

### main.py

This is the entry point of the game. It sets up the main window, creates frames for layout, and initializes the grid of cells.

### cell.py

Handles the behavior and properties of each cell in the Minesweeper game. This includes revealing cells, marking cells as mines, and displaying the result when a mine is clicked.

### utils.py

Provides utility functions for calculating dimensions based on percentages of the total width and height.

### setting.py

Holds configuration

 values for the game.
## Running on windows

To run the Minesweeper game fully on Windows, you'll need to adjust the code to handle Windows-specific message boxes using ctypes. This change is necessary for displaying a native message box with "Abort", "Retry", and "Ignore" options when a mine is clicked. Ensure you have Python and Tkinter installed. Modify the show_mine method in cell.py to use ctypes.windll.user32.MessageBoxW. Here's a snippet to get you started:

   ```python
   
   import ctypes
   
   def show_mine(self):
       self.cell_btn_object.configure(bg="red")
       response = ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine!", "Game Over", 3)
       if response == 4:  # Retry
           self.root.destroy()
           main()  # Restart the game; ensure `main` function wraps the game's start logic
       elif response == 3:  # Abort
           self.root.destroy()
       # Ignore option will do nothing
   ```
Integrating this code will provide a familiar dialog interface on Windows. Ensure thorough testing on both Linux and Windows for compatibility.



---

This documentation provides an overview of the project, installation instructions, and detailed explanations of each file. Feel free to modify it to better fit your project's needs.
