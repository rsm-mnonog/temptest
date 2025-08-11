import jupytext
import os

if os.path.isfile("tz-gaming-sol.ipynb"):
    notebook_name = "tz-gaming-sol.ipynb"
else:
    notebook_name = "tz-gaming.ipynb"

ntbk = jupytext.read(notebook_name)
file_name = notebook_name.replace("ipynb", "py")
jupytext.write(ntbk, file_name, fmt="py:percent")

with open(file_name) as f:
    exec(f.read())

with open("test/tests.py") as f:
    exec(f.read())
