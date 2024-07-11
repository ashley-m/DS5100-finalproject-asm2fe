# Title: Monte Carlo Simulation
## Version 1.1.2
# Author: Ashley Miller

## Description:
This is a simulation that allows for customizable data randomization and 
analysis using three different classes of object in Python. The module 
is packaged for installation using pip. Once installed, you will be able 
to import the package in your code using `import montecarlo.montecarlo`. 
Each object created generates data which can be used by the next to simulate
or analyze the game. This class is dependent on the `pandas` and `numpy`
packages. The Die class is instantiated and takes an argument containing 
the faces of the die. These faces must be unique, and they can be either 
letters or numbers. For example, a coin can be created with the
following code `coin=Die(np.array(['H','T']))`. Each Die has a set 
of weights assigned to each face with a default value of 1. You can modify
the weight of each face to create a bias. Dice can be rolled to produce 
outcomes for the Game class to store. Games are instantiated with a set
of similar Dice (same number and type of faces) - i.e. a game with 7 
six-sided dice with faces ranging from 1 to 6 would be played as follows:

```{python}
d6=Die(np.arange(1,7))
yahtzee = Game([d6, d6, d6, d6, d6, d6, d6])
yahtzee.play()
```
You can instruct the game to play any number of times, and it will throw
the dice as a group to generate each outcome. Games can access their
last play (and only their last play) using the class method `last_play`.
Analyzer objects are created with a Game argument to allow for analysis
of the game state data. The `face_roll` method returns the counts of each
face from each roll. The `jackpot` counts how many times the Dice roll
resulted in all matching faces. The `perm_count` and `combo_count` methods
return the number of permutation and combinations for the results,
respectively. The following code would generate the four types of analyses
of which `montecarlo` package is capable.

```{python}
yahtzee_analysis = Analyzer(yahtzee)
roll_data = yahtzee_analysis.face_roll()
jackpot_data = yahtzee_analysis.jackpot()
permutation_data = yahtzee_analysis.perm_count()
combination_data = yahtzee_analysis.combo_count()
```

# API description
## `Die`
`__init__(self, sides)`
- `Die` takes an array and raises errors if the argument passed is
not a NumPy array or if the faces are not unique.
- The returned `Die` object has faces with default weights of 1.

`adj_wt(self, face, wt)`
- Adjusts the weight of the selected face with the argument
passed. This will result in an error if the value passed is not a
floating point number. This returns `None`

`roll(self, n = 1)`
- Generates and returns a Python list of outcomes from the `Die`'s
faces biased using the weight values. May be passed an argument
to indicate the number of times the die is to be rolled, but the
default is to roll once.

`get_state(self)`
- Returns a pandas DataFrame containing the column of weights assigned to
the corresponding faces, which comprise the indices. Takes no arguments

## `Game`
`__init__(self, dice_list)`
- `Game` takes a Python list of similar dice - they should all have
the same faces, though the weight biases may be different.
- This returns a `Game` object

`play(self, i=1)`
- Takes an integer and instructs the `Game` object to generate results
the same number of times. This method only generates one roll if no
argument is passed.
- Returns a wide format DataFrame where each column corresponds to
the `Die` in the `Game`'s set and the roll numbers are the indices.
The cells contain the face result of each roll.

`last_play(self, width='WIDE')`
- Returns a copy of the DataFrame containing the results. Takes a string
argument which specifies narrow or wide (this is not case sensitive).
- Defaults to wide format as described above, but the narrow
version has a MultiIndex where the roll number is the first index
and the `Die` number is the second. The single column contains
the face results.

## `Analyzer`
`__init__(self, game_obj)`
- `Analyzer` takes a `Game` argument and returns an `Analyzer` object.

`jackpot(self)`
- Returns an integer count of how many rolls resulted in all `Die` in
the game landing on the same face. Takes no arguments

`face_roll(self)`
- Returns a DataFrame containing the results from the `Game`'s last play.
The index represents the roll number and the face values are the column
features. Each cell of the columns contain the result values for each roll.
Takes no arguments.

`combo_count(self)`
- Returns a DataFrame where the MultiIndex represents the distinct face
combinations found in the results - the order of faces is not considered.
The column has the associated counts for the combination represented in the
index. Takes no arguments.

`perm_count(self)`
- Returns a DataFrame where the MultiIndex represents the distinct face
permutations found in the results - the order is taken into consideration.
The column has the associated counts for the permutation represented in the
index. Takes no arguments.
