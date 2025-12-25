import tkinter as tk
from tkinter import ttk, messagebox
import heapq
import random

# ====== PFS Algorithm ======
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


def generate_random_maze(rows, cols, wall_prob=0.3):
    maze = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                row.append(1)
            else:
                row.append(1 if random.random() < wall_prob else 0)
        maze.append(row)

    while True:
        sx, sy = random.randint(1, rows-2), random.randint(1, cols-2)
        if maze[sx][sy] == 0:
            maze[sx][sy] = 'S'
            break

    while True:
        gx, gy = random.randint(1, rows-2), random.randint(1, cols-2)
        if maze[gx][gy] == 0:
            maze[gx][gy] = 'G'
            break

    return maze


# ====== Splash Screen ======
class SplashScreen:
    def __init__(self, root):
        self.root = root

        self.splash = tk.Toplevel()
        self.splash.title("Loading...")
        self.splash.geometry("500x300")
        self.splash.configure(bg="#0F172A")
        self.splash.overrideredirect(True)
        x = (self.splash.winfo_screenwidth() // 2) - 250
        y = (self.splash.winfo_screenheight() // 2) - 150
        self.splash.geometry(f"+{x}+{y}")

        tk.Label(
            self.splash,
            text="Maze Solver",
            font=("Arial", 26, "bold"),
            fg="#38BDF8",
            bg="#0F172A"
        ).pack(pady=40)

        tk.Label(
            self.splash,
            text="Loading AI Engine...",
            font=("Arial", 12),
            fg="white",
            bg="#0F172A"
        ).pack(pady=10)

        self.progress = ttk.Progressbar(
            self.splash,
            orient="horizontal",
            length=300,
            mode="determinate"
        )
        self.progress.pack(pady=20)

        self.value = 0
        self.animate()

    def animate(self):
        if self.value < 100:
            self.value += 2
            self.progress["value"] = self.value
            self.splash.after(40, self.animate)
        else:
            self.splash.destroy()
            self.root.deiconify()
            WelcomeScreen(self.root)



# ====== Welcome Screen ======
class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver - Welcome")
        self.root.geometry("400x320")
        self.root.configure(bg="#111827")

        tk.Label(
            root,
            text="Maze Solver",
            font=("Arial", 28, "bold"),
            fg="#22C55E",
            bg="#111827"
        ).pack(pady=30)

        tk.Label(
            root,
            text="Get ready to solve mazes ",
            font=("Arial", 14),
            fg="white",
            bg="#111827"
        ).pack(pady=10)

        tk.Button(
            root,
            text="Start Game",
            font=("Arial", 14, "bold"),
            bg="#3B82F6",
            fg="white",
            width=15,
            command=self.start_game
        ).pack(pady=40)

        tk.Button(
            root,
            text="Exit",
            font=("Arial", 12),
            bg="#EF4444",
            fg="white",
            width=10,
            command=root.quit
        ).pack()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MazeGUI(self.root)


# ====== Maze GUI ======
class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver - PFS (AI Project)")

        self.rows = 7
        self.cols = 9
        self.cell_size = 70

        self.maze = generate_random_maze(self.rows, self.cols)

        self.start = None
        self.goal = None

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.draw_maze()
        self.create_buttons()

        self.canvas.bind("<Configure>", self.on_canvas_resize)

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

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

                if self.maze[i][j] == 'S':
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2,
                                            text="START", fill="white", font=("Arial", 8, "bold"))
                elif self.maze[i][j] == 'G':
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2,
                                            text="GOAL", fill="white", font=("Arial", 8, "bold"))

    def create_buttons(self):
        tk.Button(self.root, text="Solve", bg="#3B82F6", fg="white",
                    command=self.solve).grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Button(self.root, text="Reset Maze", bg="#EF4444", fg="white",
                    command=self.reset_maze).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(self.root, text="New Random Maze", bg="#22C55E", fg="white",
                    command=self.new_random_maze).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

    def solve(self):
        path, cost = pfs_maze_solver(self.maze, self.start, self.goal)
        if not path:
            messagebox.showerror("Result", "No Path Found")
            return
        self.animate_path(path, 0, cost)

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
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                        fill="#38BDF8", outline="gray")

        self.root.after(200, lambda: self.animate_path(path, index + 1, cost))

    def reset_maze(self):
        self.draw_maze()

    def new_random_maze(self):
        self.maze = generate_random_maze(self.rows, self.cols)
        self.draw_maze()

    def on_canvas_resize(self, event):
        self.cell_size = min(event.width / self.cols, event.height / self.rows)
        self.draw_maze()


# ====== Run Program ======
root = tk.Tk()
root.withdraw()
SplashScreen(root)
root.mainloop()

