# Assignment 4 - FCB 2020
### Deadline: 30/10/2020 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2020-21 at
[https://github.com/funcompbio2020](https://github.com/funcompbio2020)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-4` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the version available at the deadline will be retrieved. If the
first version available is posterior to the deadline, then the mark of the
assignment will have a penalty.

## Description

The goal of this assignment is to implement a program in Python that
**counts the words of a sentence, where words are separated by one or more
spaces and the sentence may start or end with spaces**.

This assignment incorporates [GitHub Classroom Autograding](https://mspoweruser.com/github-classroom-autograding-feature),
which will help you to automatically test whether your Python program is
correctly working after every _push_. To work with this feature you
need to edit your program in the existing file `src/wordcount.py` and
leave the rest of the files and directory structure intact. The file
`src/wordcount.py` has the following template: 

```
def main() :
    ## do not remove these two lines!!
    textstr = input("Write a sentence: ")
    v = list(textstr)
    wc = 0 ## 'wc' (word count) should store the number of words

    ## your code should start here


    ## your code should end here

    ## this must be the last line of this function, do not remove it!!
    return wc

if __name__ == "__main__" :
    print(main())
```

Please do not remove any line of this template and add your code between
the two comment lines indicating the place where your should put it. This
code will be part of the `main()` function, and therefore, it should start
with the proper space identation that makes it part of that function. The
code includes the first instructions that ask the user to write a sentence,
calls the function `input()` to read that sentence and stores it into a
variable called `textstr`, which is then coerced into a vector (actually a
Python `list`) called `v`, where every typed letter takes a position in that
vector. Finally, a word counting variable called `wc` is initialitzed to 0.
Your program should use the vector variable `v` to examine the characters of the sentence
one by one, and the integer variable `wc` to count the number of words of the
sentence. The last line of the `main()` function returns the value of `wc`,
which will be printed on the screen if you call this Python script from the
command line by typing

```
$ python wordcount.py
```

This code is written using Python version 3, if you use version 2, you will
probably be getting errors.

Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `test` directory with the initial files of the assignment repo.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/wordcount.py`**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Does the assignment contain the required files?
  * Does the Python program `src/wordcount.py` runs without errors?
  * Does the Python program `src/wordcount.py` counts words in a sentence correctly?
  * Does the Python program `src/wordcount.py` passes all autograding tests?

