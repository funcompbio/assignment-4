[![FCB-Python-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)](../../actions?query=workflow%3AFCB-Python-autograding)

# Assignment 4 - FCB 2020
### Deadline: 29/10/2020 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2021-22 at
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
**counts the ocurrences of a dinucleotide from the DNA sequence of a gene
stored in a FASTA file giving the FASTA filename and the two nucleotides
that form the dinucleotide as arguments from the command line**.


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
`src/dinuc.py` and leave the rest of the files and directory structure
intact. Within the file `src/dinuc.py` please follow the instructions
written in comments and put your code exactly in the indicated lines. The
template repo and autograding feature will test your program with the DNA
sequence of the [_HBB_](https://www.ncbi.nlm.nih.gov/gene/3043) gene stored
in a FASTA file as an example, assuming that the FASTA filename is the first
argument and the two nucleotides forming the sought dinucleotide in the second
and third arguments. To perform such a test in your own computer, you should
change your current working directory to the top directory of this GitHub
repo and type:

```
$ python src/dinuc.py HBB.fa A A
```

for the `AA` dinucleotide. Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `tests` directory with the initial files of the assignment repo.
  4. The `HBB.fa` FASTA file storing the DNA of the _HBB_ gene.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/dinuc.py`**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Does the assignment contain the required files?
  * Does the Python program `src/dinuc.py` runs without errors?
  * Does the Python program `src/dinuc.py` counts ocurrences of a dinucleotide
    in the DNA of a gene stored in a FASTA file correctly?
  * Does the Python program `src/dinuc.py` passes all autograding tests?
