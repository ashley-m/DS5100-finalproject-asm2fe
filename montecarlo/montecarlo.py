class Die:
    '''
-   A die has N sides, or “faces”, and W weights, and can be rolled
    to select a face.

-   For example, a “die” with N = 2 is a coin, and a one with
    N = 6 is a standard die.

-   Normally, dice and coins are “fair,” meaning that the each side
    has an equal weight. An unfair die is one where the weights are
    unequal.

-   Each side contains a unique symbol. Symbols may be all alphabetic or
    all numeric.

-   W defaults to 1.0 for each face but can be changed after the
    object is created.

-   The weights are just positive numbers (integers or floats, including 0),
    not a normalized probability distribution.

-   The die has one behavior, which is to be rolled one or more times.
    '''
    def __init__(self, sides, weights):
        '''
    -   Takes a NumPy array of faces as an argument. Throws a `TypeError` if
        not a NumPy array.

    -   The array’s data type `dtype` may be strings or numbers.

    -   The array’s values must be distinct. Tests to see if the values are
        distinct and raises a `ValueError` if not.

    -   Internally initializes the weights to 1.0 for each face.

    -   Saves both faces and weights in a private data frame with faces in
        the index.
        '''
         
        pass

    def adj_wt(self, face, wt):
        '''
    -   Takes two arguments: the face value to be changed and the new
        weight.

    -   Checks to see if the face passed is valid value, i.e. if it is in
        the die array. If not, raises an `IndexError`.

    -   Checks to see if the weight is a valid type, i.e. if it is numeric
        (integer or float) or castable as numeric. If not, raises a
        `TypeError`.
        '''

        pass

    def roll(self, n):
        '''
    -   Takes a parameter of how many times the die is to be rolled;
        defaults to $1$.

    -   This is essentially a random sample with replacement, from the
        private die data frame, that applies the weights.

    -   Returns a Python list of outcomes.

    -   Does not store internally these results.
        '''
        pass

    def get_state(self):
        '''
    -   Returns a copy of the private die data frame.
        '''
        pass

class Game:
    '''
-   A game consists of rolling of one or more similar dice (Die objects)
    one or more times. 

-   By similar dice, we mean that each die in a given game has the same
    number of sides and associated faces, but each die object may have
    its own weights. 

-   Each game is initialized with a Python list that contains one or
    more dice.

-   Game objects have a behavior to play a game, i.e. to roll all of the
    dice a given number of times.

-   Game objects only keep the results of their most recent play.
    '''

    def __init__(self, dice_list):
        '''
    -   Takes a single parameter, a list of already instantiated similar
        dice.

    -   Ideally this would check if the list actually contains Die objects
        and that they all have the same faces, but this is not required for
        this project.
        '''

        pass

    def play(self, i):
        '''
    -   Takes an integer parameter to specify how many times the dice should
        be rolled.

    -   Saves the result of the play to a private data frame.

    -   The data frame should be in wide format, i.e. have the roll number
        as a named index, columns for each die number (using its list index
        as the column name), and the face rolled in that instance in each
        cell.
        '''

        pass

    def last_play(self, width = 'WIDE'):
        '''
    -   This method just returns a copy of the private play data frame to
        the user.

    -   Takes a parameter to return the data frame in narrow or wide form
        which defaults to wide form.

    -   The narrow form will have a `MultiIndex`, comprising the roll number
        and the die number (in that order), and a single column with the
        outcomes (i.e. the face rolled).

    -   This method should raise a `ValueError` if the user passes an
        invalid option for narrow or wide.
        '''

        pass

class Analyzer:
    '''
-   An Analyzer object takes the results of a single game and computes
    various descriptive statistical properties about it.'''

    def __init__(self, game_state):
        '''
    -   Takes a game object as its input parameter. Throw a `ValueError` if
        the passed value is not a Game object.
        '''

        pass

    def jackpot(self):
        '''
    -   A jackpot is a result in which all faces are the same, e.g. all ones
        for a six-sided die.

    -   Computes how many times the game resulted in a jackpot.

    -   Returns an integer for the number of jackpots.
        '''

        pass

    def face_roll(self):
        '''
    -   Computes how many times a given face is rolled in each event. For example, if a roll of five dice has all sixes, then the counts for this roll would be $5$ for the face value `6` and $0$ for the other faces.

    -   Returns a data frame of results.

    -   The data frame has an index of the roll number, face values as
        columns, and count values in the cells (i.e. it is in wide format).
        '''

        pass

    def combo_count(self):
        '''
    -   Computes the distinct combinations of faces rolled, along with their
        counts.

    -   Combinations are order-independent and may contain repetitions.

    -   Returns a data frame of results.

    -   The data frame should have an MultiIndex of distinct combinations
        and a column for the associated counts.
        '''

        pass

    def perm_count(self):
        '''
    -   Computes the distinct permutations of faces rolled, along with their
        counts.

    -   Permutations are order-dependent and may contain repetitions.

    -   Returns a data frame of results.

    -   The data frame should have an MultiIndex of distinct permutations
        and a column for the associated counts.
        '''

        pass

