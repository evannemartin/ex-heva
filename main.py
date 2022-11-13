import sqlite3
import numpy as np
from description import definition

# Read and save data from penguins.sqlite
with sqlite3.connect("data/penguins.sqlite") as co:
    penguins = co.execute(
            "SELECT * FROM penguins"
        ).fetchall()

nb_mod = len(penguins[0])
pen_array = np.array(penguins)

# Check all the modalities
for i in range (nb_mod) :
    print("Frequencies for modality ", i)
    print(definition.freq_mod(pen_array[:,i]))

# Check the histogram creation
definition.create_hist(pen_array[:,0])
definition.create_hist(pen_array[:,2])
