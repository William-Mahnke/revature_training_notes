# Jupyter Notebook — Installation and Usage Guide

---

## What is Jupyter Notebook?

Jupyter Notebook is an open-source, browser-based interactive environment that allows you to write and run Python code in individual blocks called **cells**. It is widely used for data science, education, and rapid prototyping because it lets you mix code, output, and notes all in one document.

---

## Prerequisites

Before installing Jupyter Notebook, make sure you have the following:

- **Python 3.x** installed — verify by running `python --version` in your terminal
- **pip** installed — verify by running `pip --version` in your terminal
- A **virtual environment** (recommended — see Step 1)

---

## Step 1 — Create and Activate a Virtual Environment (Recommended)

It is best practice to install Jupyter inside a virtual environment to keep your project dependencies isolated.

```bash
# Create a virtual environment
python -m venv venv

# Activate — Mac/Linux
source venv/bin/activate

# Activate — Windows (Command Prompt)
venv\Scripts\activate

# Activate — Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Your terminal prompt should now show `(venv)` to indicate the environment is active.

---

## Step 2 — Install Jupyter Notebook

With your virtual environment active, install Jupyter using pip:

```bash
pip install notebook
```

To verify the installation was successful:

```bash
jupyter --version
```

You should see output listing the Jupyter component versions.

---

## Step 3 — Launch Jupyter Notebook

To start Jupyter Notebook, run the following command in your terminal from the directory you want to work in:

```bash
jupyter notebook
```

This will:

1. Start a local server (typically at `http://localhost:8888`)
2. Automatically open the Jupyter interface in your default web browser

> **Note:** Do not close the terminal window while Jupyter is running — the terminal is the server. Closing it will shut down Jupyter.

---

## Step 4 — Create a New Notebook

Once the Jupyter interface opens in your browser:

1. Click the **"New"** button in the top-right corner
2. Select **"Python 3 (ipykernel)"** from the dropdown
3. A new notebook will open in a new browser tab

---

## Step 5 — Understanding the Interface

```
┌─────────────────────────────────────────────────────┐
│  File  Edit  View  Insert  Cell  Kernel  Help        │  ← Menu bar
├─────────────────────────────────────────────────────┤
│  + | Cut | Copy | Paste | ▶ Run | ■ | ⟳ | Code  ▼  │  ← Toolbar
├─────────────────────────────────────────────────────┤
│                                                       │
│  In [ ]:  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │  ← Cell
│                                                       │
└─────────────────────────────────────────────────────┘
```

| Element | Description |
|---|---|
| **Cell** | The individual block where you write code or text |
| **In [ ]:** | Indicates a code cell. The number inside shows the order it was run |
| **Toolbar** | Buttons for running cells, adding cells, and changing cell type |
| **Kernel** | The Python engine running your code — shown in the top-right corner |

---

## Step 6 — Working with Cells

### Running a Cell

Type code into a cell and run it using one of these methods:

| Action | Shortcut |
|---|---|
| Run cell and move to next | `Shift + Enter` |
| Run cell and stay on same cell | `Ctrl + Enter` |
| Run cell and insert new cell below | `Alt + Enter` |

### Example — Your First Cell

Click inside a cell, type the following, and press `Shift + Enter`:

```python
print("Hello, Jupyter!")
```

The output will appear directly below the cell:

```
Hello, Jupyter!
```

---

## Step 7 — Cell Types

Jupyter supports different cell types, selectable from the dropdown in the toolbar:

| Type | Purpose |
|---|---|
| **Code** | Write and run Python code |
| **Markdown** | Write formatted notes, headings, and documentation |
| **Raw** | Plain text — not executed or rendered |

### Switching Cell Type

1. Click on a cell to select it
2. Use the dropdown in the toolbar (defaults to **"Code"**) to change the type
3. For Markdown cells, press `Shift + Enter` to render the formatted text

### Markdown Example

Change a cell to **Markdown**, type the following, and press `Shift + Enter`:

```markdown
# My First Notebook
This is a **Markdown** cell. I can write notes alongside my code.
```

---

## Step 8 — Common Keyboard Shortcuts

Jupyter has two modes:

- **Edit Mode** — you are typing inside a cell (green border)
- **Command Mode** — you are navigating between cells (blue border). Press `Esc` to enter Command Mode.

| Shortcut | Mode | Action |
|---|---|---|
| `Shift + Enter` | Either | Run cell and move to next |
| `Ctrl + Enter` | Either | Run cell, stay in place |
| `Esc` | Edit | Enter Command Mode |
| `Enter` | Command | Enter Edit Mode |
| `A` | Command | Insert cell **above** |
| `B` | Command | Insert cell **below** |
| `D + D` | Command | Delete selected cell |
| `M` | Command | Change cell to Markdown |
| `Y` | Command | Change cell to Code |
| `Z` | Command | Undo cell deletion |
| `Ctrl + S` | Either | Save notebook |

---

## Step 9 — Saving Your Notebook

Jupyter autosaves periodically, but you should save manually often:

- Press **`Ctrl + S`**
- Or go to **File → Save and Checkpoint**

Notebooks are saved as **`.ipynb`** files in the directory Jupyter was launched from.

---

## Step 10 — Shutting Down Jupyter

### Close a Notebook

Go to **File → Close and Halt** to shut down the notebook's kernel and close the tab.

### Stop the Jupyter Server

In the terminal where Jupyter is running, press:

```
Ctrl + C
```

Then confirm with `y` when prompted. This shuts down the local server completely.

---

## Using Jupyter in VS Code

If you prefer to stay in VS Code, you can run Jupyter Notebooks directly without a browser:

1. Install the **Jupyter extension** in VS Code:
   - Press `Ctrl + Shift + X` to open Extensions
   - Search for **"Jupyter"** and click **Install**

2. Create or open a `.ipynb` file in VS Code

3. VS Code will render the notebook interface directly in the editor

4. Select your Python interpreter/virtual environment using:
   - `Ctrl + Shift + P` → **"Python: Select Interpreter"**

---

## Quick Reference

| Task | Command |
|---|---|
| Install Jupyter | `pip install notebook` |
| Launch Jupyter | `jupyter notebook` |
| Run a cell | `Shift + Enter` |
| Insert cell below | `B` (Command Mode) |
| Delete a cell | `D + D` (Command Mode) |
| Save notebook | `Ctrl + S` |
| Stop the server | `Ctrl + C` in terminal |
