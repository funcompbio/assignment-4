[![FCB-Python-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)](../../actions?query=workflow%3AFCB-Python-autograding)

# Assignment 4 - FCB 2024
### Deadline: 22/10/2024 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2024-25 at
[https://github.com/FCB-2024](https://github.com/FCB-2024)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-4` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the latest version available will be retrieved. If that latest
version available is posterior to the deadline, then the mark of the assignment
will have a penalty.

To complete your submission (see rubric below) please **agree to the following
academic integrity statement** by editing this README file and placing the
letter `X` between the squared brackets preceding the statement:

- [] The work here submitted has been entirely developed by myself and is the
  result of my own work.

## Description

The goal of this assignment is to implement a program in Python that
**takes a positive integer number as argument in the command line and
decides whether this number is highly-composite, also known as anti-prime,
or not, printing the message 'antiprime' when the number is anti-prime, and
'not anti-prime' when it is not**.

According to the Wikipedia
[page](https://en.wikipedia.org/wiki/Highly_composite_number) a positive
integer number is called highly composite, or anti-prime, if it has more
divisors than all smaller positive integers. For instance, number 6 **is
anti-prime** because has 4 divisors (1, 2, 3, and 6) and none of its smaller
positive integers (1, 2, 3, 4, 5) has more divisors than this number 6.
Number 10 **is not anti-prime** because it has 4 divisors (1, 2, 5, and 10),
while some of the smaller numbers, such as 4, but also 6 or 8, have also 4
divisors.

This assignment incorporates an autograding feature using a so-called
[GitHub Actions Worflow](https://github.com/features/actions), which will
help you to automatically test whether your Python program is
correctly working after every _push_. More concretely, a few minutes after
you _pushed_ your changes to your remote GitHub repo, the badge labeled
`FCB-Python-autograding` on top of this README file will be red and display
the message `failing` if the autograding has not been successful, and
green with the message `passing` otherwise. You may click on badge to
look at output of the autograding tests to understand why it has failed,
if that was the case. This feature provides you with
[formative assessment](https://en.wikipedia.org/wiki/Formative_assessment)
and to work with it you need to edit your program in the existing file
`src/antiprime.py` and leave the rest of the files and directory structure
intact. Within the file `src/antiprime.py` please follow the instructions
written in comments and put your code exactly in the indicated lines. You
can test your program on your own computer by changing your current working
directory into the `src` directory of this GitHub repo and typing:

```
$ python antiprime.py 6
```

to test, for instance, whether the number 6 is anti-prime. Note that the
`main()` function in the `src/antiprime.py` file should take the number
your want to test as argument from the Unix command line to enable the
autograding tool to correctly evaluate your program. Your assignment repo
should have the following files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `tests` directory with the initial files of the assignment repo.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/antiprime.py`, and `README.md` to agree
to the academic integrity statement**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Did you use the GitHub user profile you provided in the first assignment?
  * Did you properly agree to the academic integrity statement?
  * Does the assignment contain the required files?
  * Does the Python program `src/antiprime.py` runs without errors?
  * Does the Python program `src/antiprime.py` identifies anti-prime and non-anti-prime numbers correctly?
  * Does the Python program `src/antiprime.py` passes all autograding tests?
