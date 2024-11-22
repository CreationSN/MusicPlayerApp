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

    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)

    solution = [row[:] for row in board]

    for _ in range(40):  # Adjust the number of cells to remove
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board, solution

def main(page: ft.Page):
    page.title = "Sudoku Game"
    page.padding = 20
    page.scroll = "adaptive"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    grid = [[None for _ in range(9)] for _ in range(9)]
    current_puzzle = [[0 for _ in range(9)] for _ in range(9)]
    solution = [[0 for _ in range(9)] for _ in range(9)]

    def load_puzzle():
        nonlocal current_puzzle, solution
        current_puzzle, solution = generate_sudoku()
        for row in range(9):
            for col in range(9):
                value = current_puzzle[row][col]
                grid[row][col].content.value = str(value) if value != 0 else ""
                grid[row][col].content.read_only = value != 0
                grid[row][col].content.bgcolor = "#d0e7ff" if value != 0 else "white"

        page.update()

    def check_cell():
        for row in range(9):
            for col in range(9):
                if not grid[row][col].content.read_only:
                    try:
                        user_value = int(grid[row][col].content.value)
                        if user_value == solution[row][col]:
                            grid[row][col].content.bgcolor = "lightgreen"
                        else:
                            grid[row][col].content.bgcolor = "red"
                    except ValueError:
                        grid[row][col].content.bgcolor = "red"
        page.update()

    def check_solution():
        for row in range(9):
            for col in range(9):
                try:
                    user_value = int(grid[row][col].content.value)
                    if user_value != solution[row][col]:
                        page.dialog = ft.AlertDialog(
                            title=ft.Text("You Lose!"),
                            on_dismiss=lambda e: None,
                        )
                        page.dialog.open = True
                        page.update()
                        return
                except ValueError:
                    page.dialog = ft.AlertDialog(
                        title=ft.Text("You Lose!"),
                        on_dismiss=lambda e: None,
                    )
                    page.dialog.open = True
                    page.update()
                    return
        page.dialog = ft.AlertDialog(
            title=ft.Text("Congratulations! You Win!"),
            on_dismiss=lambda e: None,
        )
        page.dialog.open = True
        page.update()

    def create_cell(row, col):
        # Add thicker borders for 3x3 sections
        top_border = 3 if row % 3 == 0 else 1
        left_border = 3 if col % 3 == 0 else 1
        bottom_border = 3 if row == 8 else 1
        right_border = 3 if col == 8 else 1

        field = ft.TextField(
            value="",
            text_align="center",
            height=50,
            width=50,
            border_radius=0,
            border_color="black",
            border_width=0,
            read_only=False,
            color="black",
            bgcolor="white",
        )
        grid[row][col] = ft.Container(
            content=field,
            border=ft.border.Border(
                top=ft.border.BorderSide(width=top_border, color="black"),
                left=ft.border.BorderSide(width=left_border, color="black"),
                bottom=ft.border.BorderSide(width=bottom_border, color="black"),
                right=ft.border.BorderSide(width=right_border, color="black"),
            ),
        )
        return grid[row][col]

    sudoku_grid = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [create_cell(row, col) for col in range(9)],
                    spacing=0,
                ) for row in range(9)
            ],
            spacing=0,
            alignment="center",
        ),
        border_radius=10,
        bgcolor="#f0f4ff",
        padding=10,
        margin=20,
    )

    new_game_button = ft.ElevatedButton(
        text="New Game",
        on_click=lambda e: load_puzzle(),
        width=150,
    )

    check_cell_button = ft.ElevatedButton(
        text="Check Cell",
        on_click=lambda e: check_cell(),
        width=150,
    )

    check_solution_button = ft.ElevatedButton(
        text="Check Solution",
        on_click=lambda e: check_solution(),
        width=150,
    )

    buttons_row = ft.Row(
        [new_game_button, check_cell_button, check_solution_button],
        alignment="center",
        spacing=20,
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text("Sudoku Game", size=30, weight=ft.FontWeight.BOLD, color="white"),
                    bgcolor="blue",
                    padding=10,
                    border_radius=10,
                ),
                sudoku_grid,
                buttons_row,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

    load_puzzle()

ft.app(main)
