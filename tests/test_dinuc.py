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

    if !os.path.isfile("dinucgold.csv") :
        errmsg = "ERROR: gold standard for comparison has not been created"
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        raise Exception("Autograding workflow problem")

    golddat = pandas.read_csv("dinucgold.csv")
    for i in range(0, golddat.shape[0]-1) :
        nt1 = golddat.iloc[i, 1][0]
        nt2 = golddat.iloc[i, 1][1]
        n = golddat.iloc[i, 0]
        d = src.dinuc.main("HBB.fa", nt1, nt2)
        
        if d != n :
            errmsg = "ERROR: your program wrongly outputs %d for %s dinucleotides in HBB.fa, while there are %d!!" %(d,golddat.iloc[i, 1], n)
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            
        assert d == n
