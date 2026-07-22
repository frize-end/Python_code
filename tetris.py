import tkinter as tk
from tkinter import messagebox
import random

ROWS = 20
COLS = 10
CELL_SIZE = 30

SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

COLORS = {
    'I': '#00f5ff',
    'O': '#ffd700',
    'T': '#a855f7',
    'S': '#22c55e',
    'Z': '#ef4444',
    'J': '#3b82f6',
    'L': '#f97316'
}


class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("俄罗斯方块")

        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg='#1a1a2e')
        self.canvas.pack()

        self.info_frame = tk.Frame(root)
        self.info_frame.pack(side=tk.LEFT, padx=20)

        self.score_label = tk.Label(self.info_frame, text="分数: 0", font=('Arial', 16))
        self.score_label.pack(pady=10)

        self.level_label = tk.Label(self.info_frame, text="等级: 1", font=('Arial', 16))
        self.level_label.pack(pady=10)

        self.next_frame = tk.Frame(self.info_frame, bg='#16213e', width=4 * CELL_SIZE, height=4 * CELL_SIZE)
        self.next_frame.pack(pady=10)
        self.next_canvas = tk.Canvas(self.next_frame, width=4 * CELL_SIZE, height=4 * CELL_SIZE, bg='#16213e')
        self.next_canvas.pack()

        self.start_btn = tk.Button(self.info_frame, text="开始游戏", command=self.start_game, font=('Arial', 14))
        self.start_btn.pack(pady=10)

        self.reset_btn = tk.Button(self.info_frame, text="重新开始", command=self.reset_game, font=('Arial', 14))
        self.reset_btn.pack(pady=10)

        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
        self.level = 1
        self.game_over = True
        self.current_piece = None
        self.next_piece = None
        self.current_x = 0
        self.current_y = 0
        self.drop_speed = 1000

        self.root.bind('<Left>', lambda e: self.move(-1, 0))
        self.root.bind('<Right>', lambda e: self.move(1, 0))
        self.root.bind('<Down>', lambda e: self.move(0, 1))
        self.root.bind('<Up>', lambda e: self.rotate())
        self.root.bind('<space>', lambda e: self.hard_drop())

        self.draw_board()

    def draw_board(self):
        self.canvas.delete('all')
        for row in range(ROWS):
            for col in range(COLS):
                color = self.board[row][col]
                if color:
                    x1 = col * CELL_SIZE
                    y1 = row * CELL_SIZE
                    x2 = x1 + CELL_SIZE
                    y2 = y1 + CELL_SIZE
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#0f0f23', width=2)

    def draw_piece(self, piece, x, y, canvas):
        shape = SHAPES[piece]
        color = COLORS[piece]
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    x1 = (x + col) * CELL_SIZE
                    y1 = (y + row) * CELL_SIZE
                    x2 = x1 + CELL_SIZE
                    y2 = y1 + CELL_SIZE
                    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#0f0f23', width=2)

    def draw_current_piece(self):
        if self.current_piece:
            self.draw_piece(self.current_piece, self.current_x, self.current_y, self.canvas)

    def draw_next_piece(self):
        self.next_canvas.delete('all')
        if self.next_piece:
            self.draw_piece(self.next_piece, 0, 0, self.next_canvas)

    def spawn_piece(self):
        self.current_piece = self.next_piece if self.next_piece else random.choice(list(SHAPES.keys()))
        self.next_piece = random.choice(list(SHAPES.keys()))
        self.current_x = COLS // 2 - len(SHAPES[self.current_piece][0]) // 2
        self.current_y = 0

        if not self.is_valid_move(0, 0):
            self.game_over = True
            messagebox.showinfo("游戏结束", f"最终得分: {self.score}")

    def is_valid_move(self, dx, dy, piece=None, x=None, y=None):
        piece = piece if piece else self.current_piece
        x = x if x is not None else self.current_x
        y = y if y is not None else self.current_y

        shape = SHAPES[piece]
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    new_x = x + col + dx
                    new_y = y + row + dy
                    if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return False
        return True

    def rotate(self):
        if self.game_over or not self.current_piece:
            return

        rotated = self.get_rotated_piece()
        if self.is_valid_move(0, 0, rotated, self.current_x, self.current_y):
            self.current_piece = rotated

    def get_rotated_piece(self):
        shape = SHAPES[self.current_piece]
        rows = len(shape)
        cols = len(shape[0])
        rotated = []
        for col in range(cols):
            new_row = []
            for row in range(rows - 1, -1, -1):
                new_row.append(shape[row][col])
            rotated.append(new_row)

        for name, s in SHAPES.items():
            if s == rotated:
                return name
        return self.current_piece

    def move(self, dx, dy):
        if self.game_over or not self.current_piece:
            return

        if self.is_valid_move(dx, dy):
            self.current_x += dx
            self.current_y += dy
        elif dy == 1:
            self.lock_piece()

    def hard_drop(self):
        if self.game_over or not self.current_piece:
            return

        while self.is_valid_move(0, 1):
            self.current_y += 1
            self.score += 2
        self.lock_piece()

    def lock_piece(self):
        shape = SHAPES[self.current_piece]
        color = COLORS[self.current_piece]
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    self.board[self.current_y + row][self.current_x + col] = color

        self.clear_lines()
        self.spawn_piece()
        self.update_score()

    def clear_lines(self):
        lines_cleared = 0
        new_board = []
        for row in range(ROWS):
            if all(self.board[row]):
                lines_cleared += 1
            else:
                new_board.append(self.board[row])

        for _ in range(lines_cleared):
            new_board.insert(0, [0 for _ in range(COLS)])

        self.board = new_board

        if lines_cleared > 0:
            self.score += lines_cleared * 100 * self.level
            self.level = min(10, self.score // 1000 + 1)
            self.drop_speed = max(100, 1000 - (self.level - 1) * 100)

    def update_score(self):
        self.score_label.config(text=f"分数: {self.score}")
        self.level_label.config(text=f"等级: {self.level}")

    def game_loop(self):
        if not self.game_over:
            self.move(0, 1)
            self.draw_board()
            self.draw_current_piece()
            self.draw_next_piece()
            self.root.after(self.drop_speed, self.game_loop)

    def start_game(self):
        if not self.game_over:
            return
        self.game_over = False
        self.spawn_piece()
        self.game_loop()

    def reset_game(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
        self.level = 1
        self.drop_speed = 1000
        self.game_over = True
        self.current_piece = None
        self.next_piece = None
        self.update_score()
        self.draw_board()
        self.next_canvas.delete('all')


if __name__ == "__main__":
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()