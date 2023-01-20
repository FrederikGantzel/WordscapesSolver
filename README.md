# WordscapesSolver
Small program that can be used to easily solve levels of the mobile game "Wordscapes"

## Installation
Download the "WordscapesSolver" folder and put it on your desktop or wherever

## Usage
Provides an algorithm that determines what words can be made with the given input letters.
To run the program, run the command "python3 WordscapesSolver.py" in the command line (make sure the command line path is set to the WordscapesSolver folder you downloaded. Also make sure that you have python installed)
The program will promt the user to input the available letters, one letter at a time. The program will then promt the user to input whether or not to search for three letter words (as some Wordscapes levels do not allow for three letter words). The program will then calculate all words that can be made with the given inputs, and display them on the screen. The program will not search for one or two letter words, as words of this length are not allowed in Wordscapes.
Some example input:


\>python3 WordscapesSolver.py

Input letters, one letter at a time, for a maximum of 8 letters.

Input "cancel" to remove last input letter.

Input "end" to signal that you have finished inputting:

\>e

\>e

\>r

\>d

\>h

\>a

\>end

Inputted letters are:

E

E

R

D

H

A

Are three letter words allowed? (y/n)

\>n


REED

READ

RHEA

DEER

DEAR

DARE

HEED

HERE

HERD

HEAR

HEAD

HARE

HARD

EARED

HEARD

HARED

HEADER

ADHERE


## Word List
I have downloaded the list of all English words from http://www.mieliestronk.com/wordlist.html

## Issues
Wordscapes I believe use English words from Wiktionary, while I use another list of words to search for real words. Thus, sometimes the program will find words that are not counted as real words by Wordscapes, and sometimes the program will fail to find a word in a Wordscapes level.
I have not been able to find a list of all words used by Wordscapes as of yet, and thus these issues persist.
Finding a word that wordscapes doesn't count as a word is not a huge issue however, and the program failing to find a word is a rare occurrence, so the program still woks reasonably well.

