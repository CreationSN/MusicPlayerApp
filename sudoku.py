import flet as ft
import random


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
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Sudoku Game"
    page.padding = 20
    page.scroll = "adaptive"
    

    grid = [[None for _ in range(9)] for _ in range(9)]
    current_puzzle = [[0 for _ in range(9)] for _ in range(9)]

    def load_puzzle():
        nonlocal current_puzzle
        current_puzzle = generate_sudoku()
        for row in range(9):
            for col in range(9):
                value = current_puzzle[row][col]
                cell = grid[row][col]
                if value != 0:
                    cell.content = ft.Text(
                        value, size=20, weight="bold", color="black"
                    )
                    cell.bgcolor = "lightgray"
                else:
                    cell.content = ft.TextField(
                        value="",
                        text_align="center",
                        border_color="transparent",
                        bgcolor="white",
                    )
        page.update()

    def create_cell(row, col):
        container = ft.Container(
            width=50,
            height=50,
            border=ft.border.all(1, "black"),
            alignment=ft.alignment.center,
        )
        grid[row][col] = container
        return container

    sudoku_grid = ft.Column(
        [
            ft.Row(
                [
                    create_cell(row, col) for col in range(9)
                ],
                alignment="center",
            )
            for row in range(9)
        ],
        alignment="center",
    )

    new_game_button = ft.ElevatedButton(
        text="New Game",
        on_click=lambda e: load_puzzle(),
        width=150,
    )

    page.add(
        ft.Column(
            [
                ft.Text("Sudoku Game", size=24, weight="bold"),
                ft.Container(content=sudoku_grid, padding=5),
                new_game_button,
            ],
            horizontal_alignment="center",
            spacing=20,
        )
    )

    load_puzzle()


ft.app(main)

