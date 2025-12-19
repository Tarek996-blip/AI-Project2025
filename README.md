# Maze Solver

Simple maze solver project containing a solver script and a text-format maze input.

## Files
- `maze_solver.py` — main Python script that solves a maze.
- `maze.txt` — example maze input (text grid).

## Requirements
- Python 3.8 or newer

## Usage
Run the solver from the command line. Examples:

```
python maze_solver.py maze.txt
```

or, if the script reads a default file:

```
python maze_solver.py
```

## Input format
The maze is provided as a plain text grid (each line is a row). Common conventions:

- `#` — wall
- space (` `) — open path
- `S` — start (optional)
- `E` — end (optional)

If `S`/`E` are not present, the script may assume a default start/end (check `maze_solver.py`).

## Output
The solver typically prints the solved maze or the path found to the console. Check `maze_solver.py` for exact behavior.

## Notes
- Update the input-format section above if your implementation uses different characters.
- If your script requires extra dependencies, add them to a `requirements.txt` file.

## License
This repository is provided without an explicit license. Add a license file if you want to set one.
