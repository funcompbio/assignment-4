import pytest
import src.wordcount

def test_wordcount() :

    def mock_input(s) :
        return "This is a test."

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4
