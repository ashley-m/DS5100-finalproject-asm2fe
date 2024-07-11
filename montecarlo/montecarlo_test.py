import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):

    def test_01_init_die(self):
        # d6a = Die(np.array(['a', 'b', 'c', 'd', 'e', 'f']))
        d6 = Die(np.array([1,2,3,4,5,6]))
        self.assertTrue(isinstance(d6, Die), 'Die dataframe initialized incorrectly')
    
    def test_02_adj_wt(self):
        d4 = Die(np.array([1,2,3,4]))
        d4.adj_wt(1, 5)
        # print(d4.get_state().loc[1, 0])
        self.assertTrue(d4.get_state().loc[1, 0] == 5)
    
    def test_03_roll(self):
        d2 = Die(np.array(['a','b']))
        d2.adj_wt('a', 2)
        rolls = d2.roll(3)
        # print('\n', rolls)
        self.assertTrue(isinstance(rolls, list))
    
    def test_04_state(self):
        d1 = Die(np.array([1]))
        self.assertTrue(isinstance(d1.get_state(), pd.DataFrame))

    def test_05_init_game(self):
        d_list = [Die(np.array(['a','b'])), Die(np.array(['a','b']))]
        g2 = Game(d_list)
        self.assertTrue(isinstance(g2, Game))
    
    def test_06_play(self):
        let = Die(np.array(['a','b','c']))
        d_list = [let, let, let, let]
        g3 = Game(d_list)  
        res_fr = g3.play(3)
        # print('\n', type(res_fr))
        self.assertTrue(isinstance(res_fr, pd.DataFrame))

    def test_07_last_play(self):
        let = Die(np.array(['a','b','c']))
        d_list = [let, let, let, let]
        g2 = Game(d_list)  
        g2.play(3)
        res_fr = g2.last_play('narrow')
        # print('\n', res_fr)
        # print(type(res_fr))

        self.assertTrue(isinstance(res_fr, pd.DataFrame))

    def test_08_anal_init(self):
        let = Die(np.array(['a','b','c']))
        d_list = [let, let, let, let]
        g3 = Game(d_list)  
        g3.play(3)
        # st = 's'
        ana = Analyzer(g3)
        self.assertTrue(isinstance(ana, Analyzer))

    def test_09_jack(self):
        let = Die(np.array(['a','b','c']))
        let.adj_wt('a', 10)
        d_list = [let, let, let, let]
        g3 = Game(d_list)  
        g3.play(3)
        # st = 's'
        ana = Analyzer(g3)
        jack = ana.jackpot()
        # print('\n', g3.last_play('wide'))
        # print(jack)
        self.assertTrue(isinstance(jack, int))

    def test_10_face(self):
        let = Die(np.array(['a','b','c']))
        let.adj_wt('a', 10)
        d_list = [let, let, let, let]
        g3 = Game(d_list)  
        g3.play(3)
        # st = 's'
        ana = Analyzer(g3)
        # print('\n', g3.last_play('narrow'), '\n')
        # print(ana.face_roll())
        self.assertTrue(isinstance(ana.face_roll(), pd.DataFrame))

    def test_11_comb(self):
        let = Die(np.array(['a','b','c']))
        let.adj_wt('a', 10)
        d_list = [let, let, let]
        g3 = Game(d_list)  
        g3.play(20)
        ana = Analyzer(g3)
        cc = ana.combo_count()
        # print('\n', g3.last_play('wide'), '\n')
        # print('\n', cc)
        self.assertTrue(isinstance(cc, pd.DataFrame))

    def test_12_perm(self):
        let = Die(np.array(['a','b','c']))
        let.adj_wt('a', 10)
        d_list = [let, let, let]
        g3 = Game(d_list)  
        g3.play(20)
        ana = Analyzer(g3)
        cc = ana.perm_count()
        # print('\n', g3.last_play('wide'), '\n')
        # print('\n', cc)
        self.assertTrue(isinstance(cc, pd.DataFrame))

if __name__ == '__main__':
    unittest.main(verbosity=3)
    