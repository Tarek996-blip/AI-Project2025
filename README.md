# AI-Project2025

Short README for this workspace.

## Project Overview

This repository contains small demo projects related to AI and utilities used during development. Primary files in the workspace:

- `maze_solver.py` — Maze solving script (reads `maze.txt`).
- `maze.txt` — Example maze input used by the solver.
- `EELU_ML.ipynb` — Jupyter notebook with data analysis and ML experiments (references `education_career_success.csv`).

## Requirements

- Python 3.8 or newer
- Common Python packages used by the notebook and scripts:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

Install with:

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

Or create a `requirements.txt` with the above packages and run:

```
pip install -r requirements.txt
```

## Usage

1. Maze solver

   - Ensure `maze.txt` is present in the same folder as `maze_solver.py`.
   - Run the solver:

   ```
   python maze_solver.py
   ```

   (If `maze_solver.py` accepts command-line arguments, pass the path to the maze file accordingly.)

2. Jupyter Notebook

   - Open the notebook with:

   ```
   jupyter notebook EELU_ML.ipynb
   ```

   - The notebook expects `education_career_success.csv` in the same directory for full reproducibility.

## Notes

- This README is intentionally minimal. Update it with more details about `maze_solver.py` (usage flags, input format) and dataset provenance for the notebook if desired.

## License

MIT License — feel free to modify and reuse.
