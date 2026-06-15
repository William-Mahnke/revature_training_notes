# Notebook Conversion Directions

Your job as an agent is to take python scripts and created a notebook file with the same code. Here are more specific directions and guidelines:

- for each python script, the name of the corresponding notebook file should be the same as script (e.g. te notebook for 001_lists.py should be "001_lists.ipynb"
- break up the code in each script into individual cells which can be run indepdently of each oterh (you shouldn't really need to run one cell for another one to work)
- if code is used for multiple processes (the same variable being used multiple times for different ideas), repeat any needed code in each of the cells it's used
- for each cell, use the titles present in the code to add a title above each cell. if a code cell doesn't have a clear title commented in the code, infer a title based on the code in the cell
- DO NOT import or use dependencies unless the code requires it
- make any necessary judgement calls regarding formatting the notebooks to make them more readable, just make sure to a list of those judgement calls and why they came up (not in the files, just in the chat)
- if a script relies on other files within a directory: DO NOT alter any non-python scripts NO MATTER WHAT; if there is an issue converting code into a notebook, include the issue in the chat and offer a possible alternative
