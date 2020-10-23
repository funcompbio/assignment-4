import pytest
import src.wordcount

def test_wordcount1() :

    def mock_input(s) :
        return "This is a test."

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount2() :

    def mock_input(s) :
        return "This  is a test."

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount3() :

    def mock_input(s) :
        return "  This is a test."

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount4() :

    def mock_input(s) :
        return "This is a test.  "

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount5() :

    def mock_input(s) :
        return "  This is a test.  "

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount6() :

    def mock_input(s) :
        return "  This   is   a   test.  "

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 4

def test_wordcount7() :

    def mock_input(s) :
        return "    "

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 0

def test_wordcount8() :

    def mock_input(s) :
        return ""

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 0

def test_wordcount9() :

    def mock_input(s) :
        return "  a  "

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 1

def test_wordcount10() :

    def mock_input(s) :
        return "a"

    src.wordcount.input = mock_input
    wc = src.wordcount.main()

    assert wc == 1
