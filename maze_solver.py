import tkinter as tk
from tkinter import messagebox
import heapq
import random

# ====== PFS Algorithm (Uniform Cost Search) ======
def pfs_maze_solver(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return path, cost

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] != 1:
                    heapq.heappush(
                        pq,
                        (cost + 1, (nx, ny), path + [(nx, ny)])
                    )

    return None, None


# ====== Random Maze Generator ======
def generate_random_maze(rows, cols, wall_prob=0.3):
    maze = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                row.append(1)  # حدود
            else:
                row.append(1 if random.random() < wall_prob else 0)
        maze.append(row)

    # تحديد Start
    while True:
        sx, sy = random.randint(1, rows-2), random.randint(1, cols-2)
        if maze[sx][sy] == 0:
            maze[sx][sy] = 'S'
            break

    # تحديد Goal
    while True:
        gx, gy = random.randint(1, rows-2), random.randint(1, cols-2)
        if maze[gx][gy] == 0:
            maze[gx][gy] = 'G'
            break

    return maze


# ====== GUI Class ======
class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver - PFS (AI Project)")

        self.rows = 7
        self.cols = 9
        self.cell_size = 60

        self.maze = generate_random_maze(self.rows, self.cols)

        self.start = None
        self.goal = None
        self.path_cells = []

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.draw_maze()
        self.create_buttons()

        self.canvas.bind("<Configure>", self.on_canvas_resize)

    # ===== Draw Maze =====
    def draw_maze(self):
        self.canvas.delete("all")
        self.start = None
        self.goal = None

        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if self.maze[i][j] == 1:
                    color = "black"
                elif self.maze[i][j] == 'S':
                    color = "red"
                    self.start = (i, j)
                elif self.maze[i][j] == 'G':
                    color = "green"
                    self.goal = (i, j)
                else:
                    color = "white"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )

                if self.maze[i][j] == 'S':
                    self.canvas.create_text(
                        (x1 + x2)/2,
                        (y1 + y2)/2,
                        text="START",
                        fill="white",
                        font=("Arial", 8, "bold")
                    )

                elif self.maze[i][j] == 'G':
                    self.canvas.create_text(
                        (x1 + x2)/2,
                        (y1 + y2)/2,
                        text="GOAL",
                        fill="white",
                        font=("Arial", 8, "bold")
                    )

        self.path_cells.clear()

    # ===== Buttons =====
    def create_buttons(self):
        tk.Button(
            self.root, text="Solve",
            command=self.solve,
            bg="#2196F3", fg="white"
        ).grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Button(
            self.root, text="Reset Maze",
            command=self.reset_maze,
            bg="#f44336", fg="white"
        ).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(
            self.root, text="New Random Maze",
            command=self.new_random_maze,
            bg="#4CAF50", fg="white"
        ).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

    # ===== Solve =====
    def solve(self):
        path, cost = pfs_maze_solver(self.maze, self.start, self.goal)

        if not path:
            messagebox.showerror("Result", "No Path Found")
            return

        self.animate_path(path, 0, cost)

    # ===== Animate Path =====
    def animate_path(self, path, index, cost):
        if index >= len(path):
            messagebox.showinfo("Result", f"Path Cost = {cost}")
            return

        x, y = path[index]
        if (x, y) != self.start and (x, y) != self.goal:
            x1 = y * self.cell_size
            y1 = x * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size

            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#03A9F4", outline="gray"
            )

        self.root.after(200, lambda: self.animate_path(path, index + 1, cost))

    # ===== Reset =====
    def reset_maze(self):
        self.draw_maze()

    # ===== New Maze =====
    def new_random_maze(self):
        self.maze = generate_random_maze(self.rows, self.cols)
        self.draw_maze()

    # ===== Resize =====
    def on_canvas_resize(self, event):
        self.cell_size = min(
            event.width / self.cols,
            event.height / self.rows
        )
        self.draw_maze()


# ===== Run App =====
root = tk.Tk()
app = MazeGUI(root)
root.mainloop()
