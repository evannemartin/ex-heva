import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def freq_mod(array1mod) :

    """ This function allows to get the frequency for each value from an array containing one specific modality.
        It returns an array containing at the first line the values and at the seond line the frequencies associated.

        Args :
            array1mod : the numpy array containing one specific modality to study

        Returns :
            nparray containing the unique values of the modality (and 'None' if exist) and the frequencies associated (and frequency of 'None' if the case)

        Example :
            >>> int(sum(freq_mod(mod_test)[1,:]))
            1
    """
    nb_peng = len(array1mod)
    nb_nonzero = np.count_nonzero(array1mod)

    # Save the array without 'None' values
    array1mod = array1mod[array1mod != np.array(None)]

    # Count appearance for each unique value
    unique, counts = np.unique(array1mod, return_counts=True)
    nb_unique = len(unique)

    # Compute frequency for each value
    freq = counts/nb_peng

    # If 'None' values exist, put the frequency in another column
    if nb_peng-nb_nonzero != 0 :

        freq_tab = np.empty((2, (nb_unique+1)), dtype = object)

        freq_tab[0, :nb_unique] = unique
        freq_tab[0, nb_unique] = 'None'
        freq_tab[1, :nb_unique] = freq
        freq_tab[1, nb_unique] = (nb_peng-nb_nonzero)/nb_peng

    # If there are no 'None' values, simply add frequency for each value
    else :
        freq_tab = np.empty((2, nb_unique), dtype = object)

        freq_tab[0] = unique
        freq_tab[1] = freq

    return freq_tab

def create_hist(array1mod) :

    """ This function allows to create a colored histogram from an array of values.

        Args :
            array1mod : the numpy array containing one specific modality to study

        Returns :
            None
    """

    # Save the array without 'None' values
    array1mod = array1mod[array1mod != np.array(None)]

    # Count appearance for each unique value
    unique, counts = np.unique(array1mod, return_counts=True)
    nb_unique = len(unique)

    # To set a right number of bins
    if nb_unique > 20 :
        nb_unique = 20

    # Create histogram
    fig, axs = plt.subplots(1, 1, figsize =(10, 7), tight_layout = True)
    N, bins, patches = axs.hist(array1mod, bins=nb_unique)

    # Set color
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # Add labels
    plt.xlabel("Values of the modality")
    plt.ylabel("Appearance")
    plt.title('Distribution of the modality')

    # Show plot
    plt.show()



if __name__=="__main__":

    import sqlite3
    import numpy as np
    import doctest

    # Read and save data from penguins.sqlite
    with sqlite3.connect("../data/penguins.sqlite") as co:
        penguins = co.execute(
                "SELECT * FROM penguins"
            ).fetchall()

    pen = np.array(penguins)
    mod_test = pen[:,2]

    # Unitary test
    doctest.testmod(verbose=True)
