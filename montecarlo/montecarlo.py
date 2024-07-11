import numpy as np
import pandas as pd
from numbers import Number
# import random as rn

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
    def __init__(self, sides):
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
        try:
            if not isinstance(sides, np.ndarray):
                raise TypeError('not an array')
            if len(set(sides)) != len(sides):
                raise ValueError('faces must be unique')
            
            self.weight = np.ones(len(sides))
            self._data = pd.DataFrame(data= self.weight, index= sides)
            self._data.rename_axis('face', axis='columns', inplace=True)
        except (TypeError, ValueError) as e:
            print('error: ', e) 

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
        try:
            if face not in self._data.index:
                raise IndexError('invalid face')
            elif (not isinstance(float(wt), float)) or wt<0:
                raise TypeError('invalid reassignment weight')
            else:
                self._data.loc[face] = wt

        except (IndexError, TypeError) as e:
            print('error: ', e)

    def roll(self, n = 1):
        '''
    -   Takes a parameter of how many times the die is to be rolled;
        defaults to 1.

    -   This is essentially a random sample with replacement, from the
        private die data frame, that applies the weights.

    -   Returns a Python list of outcomes.

    -   Does not store internally these results.
        '''
        roll = self._data.sample(weights=self._data[0], n=n, replace= True).index.to_list()
        return roll

    def get_state(self):
        '''
    -   Returns a copy of the private die data frame.
        '''
        return self._data

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
        '''
        self._dice_set = dice_list

    def play(self, i = 1):
        '''
    -   Takes an integer parameter to specify how many times the dice should
        be rolled.

    -   Saves the result of the play to a private data frame.

    -   The data frame is in wide format, it has the roll number
        as a named index, columns for each die number (using its list index
        as the column name), and the face rolled in that instance in each
        cell.
        '''
        if not isinstance(i, int):
            raise TypeError('invalid number of plays')
        ls = []
        for d in self._dice_set:
            ls.append(d.roll(i))
        self._result_frame = pd.DataFrame(ls)
        self._result_frame = self._result_frame.T
        self._result_frame.index = [i for i in range(1, len(self._result_frame.index)+1)]
        self._result_frame.columns = [j for j in range(1, len(self._result_frame.columns)+1)]
        self._result_frame.index.name = 'roll #'
        self._result_frame.rename_axis('die #', axis='columns', inplace=True)
        return self._result_frame

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
        if width.upper() == 'WIDE':
            return self._result_frame
        elif width.upper() == 'NARROW':
            return self._result_frame.stack().to_frame('outcome')
        else:
            raise ValueError('Invalid width selection. Must be "narrow" or "wide"')

class Analyzer:
    '''
-   An Analyzer object takes the results of a single game and computes
    various descriptive statistical properties about it.'''

    def __init__(self, game_obj):
        '''
    -   Takes a game object as its input parameter. Throw a `ValueError` if
        the passed value is not a Game object.
        '''
        if not isinstance(game_obj, Game):
            raise ValueError('Argument passed was not a Game obj.')
        else:
            self._game = game_obj

    def jackpot(self):
        '''
    -   A jackpot is a result in which all faces are the same, e.g. all ones
        for a six-sided die.

    -   Computes how many times the game resulted in a jackpot.

    -   Returns an integer for the number of jackpots.
        '''
        wins = 0
        multi_fr = self._game.last_play('wide')
        
        # iterrows returns list of tuples so next()[1][1] 
        # returns first row of subframe corresponding to iteration
        # ie next(is a tuple)[accessing index of tuple][accessing row of subframe]
        
        if isinstance(multi_fr.index, pd.MultiIndex):
            for i in multi_fr.index.get_level_values(0).unique():
                outcomes = multi_fr.loc[i,'outcome']
                if outcomes.value_counts().iloc[0]==len(outcomes):
                    wins+=1
        else:
            for ind, row in multi_fr.iterrows():
                if row.value_counts().iloc[0] == len(row):
                    wins+=1

            
        return wins

    def face_roll(self):
        '''
    -   Computes how many times a given face is rolled in each event. For example, 
        if a roll of five dice has all sixes, then the counts for this roll 
        would be $5$ for the face value `6` and $0$ for the other faces.

    -   Returns a data frame of results.

    -   The data frame has an index of the roll number, face values as
        columns, and count values in the cells (i.e. it is in wide format).
        '''
        df = self._game.last_play('narrow')
        catf = pd.DataFrame()
        for i in df.index.get_level_values(0).unique():
                fs = df.loc[i]
                ff = fs.value_counts().to_frame().T
                ff.index = [i]
                catf = pd.concat([catf, ff])
        catf.rename_axis('roll #', inplace=True)
        catf.fillna(0, inplace=True)
        return catf

    def combo_count(self):
        '''
    -   Computes the distinct combinations of faces rolled, along with their
        counts.

    -   Combinations are order-independent and may contain repetitions.

    -   Returns a data frame of results.

    -   The data frame will have a MultiIndex of distinct combinations
        and a column for the associated counts.
        '''
        pf = self._game.last_play()
        # df = {
        #     1:['a','b','b'],
        #     2:['a','b','b'],
        #     3:['a','b','b']
        # }
        # pf = pd.DataFrame(df)
        count = pf.apply(lambda x: tuple(sorted(x)), axis=1).value_counts()
        com_df = pd.DataFrame(count)
        com_df.index = pd.MultiIndex.from_tuples(com_df.index)
        return com_df

    def perm_count(self):
        '''
    -   Computes the distinct permutations of faces rolled, along with their
        counts.

    -   Permutations are order-dependent and may contain repetitions.

    -   Returns a data frame of results.

    -   The data frame will have a MultiIndex of distinct permutations
        and a column for the associated counts.
        '''

        pf = self._game.last_play()
        # df = {
        #     1:['a','b','a'],
        #     2:['a','a','b'],
        #     3:['b','a','b']
        # }
        # pf = pd.DataFrame(df)
        # print('\n', pf)
        count = pf.apply(lambda x: tuple(x), axis=1).value_counts()
        perm_df = pd.DataFrame(count)
        perm_df.index = pd.MultiIndex.from_tuples(perm_df.index)
        return perm_df

