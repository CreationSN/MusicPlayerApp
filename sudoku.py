import flet as ft
import random

# Sudoku puzzle generator
def generate_sudoku():
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def fill_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    # Start with an empty board
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)

    # Remove random cells to create a puzzle
    for _ in range(40):  # Adjust the number of cells to remove
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def main(page: ft.Page):
    page.title = "Sudoku Game"
    page.padding = 20
    page.scroll = "adaptive"

    # Create a 9x9 grid for Sudoku
    grid = [[None for _ in range(9)] for _ in range(9)]
    current_puzzle = [[0 for _ in range(9)] for _ in range(9)]

    def load_puzzle():
        nonlocal current_puzzle
        current_puzzle = generate_sudoku()
        for row in range(9):
            for col in range(9):
                value = current_puzzle[row][col]
                grid[row][col].content.value = str(value) if value != 0 else ""
                grid[row][col].content.read_only = value != 0
                grid[row][col].content.bgcolor = "lightgray" if value != 0 else "white"
        page.update()

    def create_cell(row, col):
        field = ft.TextField(
            value="",
            text_align="center",
            height=50,
            width=50,
            border_color="black",
            content_padding=10,
            read_only=False,
        )
        grid[row][col] = ft.Container(content=field)
        return grid[row][col]

    # Build the Sudoku UI
    sudoku_grid = ft.Column(
        [
            ft.Row(
                [
                    create_cell(row, col) for col in range(9)
                ]
            ) for row in range(9)
        ],
        alignment="center",
        horizontal_alignment="center",
    )

    # Add New Game Button
    new_game_button = ft.ElevatedButton(
        text="New Game",
        on_click=lambda e: load_puzzle(),
        width=150,
    )

    # Add everything to the page
    page.add(
        ft.Column(
            [
                ft.Text("Sudoku Game", size=24, weight="bold"),
                sudoku_grid,
                new_game_button,
            ],
            horizontal_alignment="center",
        )
    )

    # Load the initial puzzle
    load_puzzle()

ft.app(main)
