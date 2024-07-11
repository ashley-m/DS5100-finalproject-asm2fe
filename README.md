# Title: Monte Carlo Simulation
# Author: Ashley Miller

## Description:
This is a simulation that allows for customizable data randomization and 
analysis using three different classes of object in Python. The module 
is packaged for installation using pip. Once installed, you will be able 
to import the package in your code using `import montecarlo.montecarlo`. 
Each object created generates data which can be used by the next to simulate
or analyze the game. This class is dependent on the `pandas` and `numpy`
packages. The Die class is instantiated, taking an argument containing 
the faces of the die. These faces must be unique, though they must be 
all either letters or numbers. For example, a coin can be created with 
the following code `coin=Die(np.array(['H','T']))`. Each Die has a set 
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
- `Die` takes an array and raises errors if the argument passed is not a
NumPy array or if the faces are not unique.
- The returned `Die` object has faces with default weights of 1.

`adj_wt(self, face, wt)`
- Adjusts the weight of the selected face with the argument
passed. This will result in an error if the value passed is not a
floating point number. This returns `None`

`roll(self, n = 1)`
- Generates and returns a Python list of outcomes



# About the README file

The `README.md` file will be your the main source of documentation for
your users, in addition to your use of docstrings in your code. The file
should consist of the following sections:

-   **Metadata**: Specify your name and the project name (i.e. Monte
    Carlo Simulator).

-   **Synopsis:** Show brief demo code of how the classes are used, i.e.
    code snippets showing how to install, import, and use the code
    to (1) create dice, (2) play a game, and (3) analyze a game. You can
    use preformatted blocks for the code.

-   **API description**: A list of all classes with their public methods
    and attributes. Each item should show their docstrings. All
    parameters (with data types and defaults) should be described. All
    return values should be described. Do not describe private methods
    and attributes.

# DS5100-finalproject-asm2fe
This is a final project repository for Programming for Data Science
