import subprocess
import os.path
import sys
import pytest
import src.antiprime

class color:
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_antiprime() :

    antiprimes = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840]
    nonantiprimes = [3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 25, 50, 100, 200, 300]

    for i in range(0, len(antiprimes)) :

        n = antiprimes[i]
        ## call from the command line to verify whether the program correctly
        ## transfers command-line arguments to the main() function
        cmd = ['python3', 'src/antiprime.py', str(n)]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()

        if (proc.returncode == 0) :
            r = o.decode('ascii').rstrip()
            if r != "anti-prime" :
                errmsg = "ERROR: your program wrongly outputs '%s' for %d, while it should output 'anti-prime'" %(r, n)
                print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        else :
            errmsg = "ERROR: your program did not run correctly. Please see below:"
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            errmsg = e.decode('ascii')
            errmsg = errmsg.split('\n')
            for e in errmsg :
                print(color.ERROR+color.BOLD+e+color.END, file=sys.stderr)
            r = "x"
            
        assert r == "anti-prime"

        n = nonantiprimes[i]
        ## call from the command line to verify whether the program correctly
        ## transfers command-line arguments to the main() function
        cmd = ['python3', 'src/antiprime.py', str(n)]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()

        if (proc.returncode == 0) :
            r = o.decode('ascii').rstrip()
            if r != "not anti-prime" :
                errmsg = "ERROR: your program wrongly outputs '%s' for %d, while it should output 'not anti-prime'" %(r, n)
                print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        else :
            errmsg = "ERROR: your program did not run correctly. Please see below:"
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            errmsg = e.decode('ascii')
            errmsg = errmsg.split('\n')
            for e in errmsg :
                print(color.ERROR+color.BOLD+e+color.END, file=sys.stderr)
            r = "x"
            
        assert r == "not anti-prime"
