import sqlite3

# Read and save data from penguins.sqlite

with sqlite3.connect("data/penguins.sqlite") as co:
    penguins = co.execute(
            "SELECT * FROM penguins"
        ).fetchall()
