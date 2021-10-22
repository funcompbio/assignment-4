import os.path
import sys
import pytest
import pandas
import src.dinuc

class color:
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_dinuc() :

    if not os.path.isfile("dinucgold1.csv") or not os.path.isfile("dinucgold2.csv") :
        errmsg = "ERROR: gold standard for comparison has not been created"
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        raise Exception("Autograding workflow problem")

    ## assumes dinucleotides are in the same order in both files
    golddat1 = pandas.read_csv("dinucgold1.csv")
    golddat2 = pandas.read_csv("dinucgold2.csv")
    if (golddat1.shape[0] != golddat2.shape[0]) :
        errmsg = "ERROR: dinucleotides in gold standard files do not match"
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        raise Exception("Autograding workflow problem")

    for i in range(0, golddat1.shape[0]-1) :
        if (golddat1.iloc[i, 1][0] != golddat2.iloc[i, 1][0] or
                golddat1.iloc[i, 1][1] != golddat2.iloc[i, 1][1]) :
            errmsg = "ERROR: dinucleotides in gold standard files do not match"
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            raise Exception("Autograding workflow problem")

        nt1 = golddat1.iloc[i, 1][0]
        nt2 = golddat1.iloc[i, 1][1]
        n = golddat1.iloc[i, 0] + golddat2.iloc[i, 0]
        d = src.dinuc.main("HBB.fa", nt1, nt2)
        
        if d != n :
            errmsg = "ERROR: your program wrongly outputs %d for %s dinucleotides in HBB.fa, while there are %d!!" %(d,golddat1.iloc[i, 1], n)
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            
        assert d == n
