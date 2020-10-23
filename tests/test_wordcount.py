import pytest
import src.wordcount

def test_wordcount() :

    src.wordcount.input = "This is a test."
    wc = src.wordcount.main()

    assert wc == 4
