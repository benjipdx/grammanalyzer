#! /usr/bin/env sh

#lang one
#accept
#S->aSb|#
echo "Language 1 ACCEPT"
./grammanalyzer.py templates/1.txt a#b
./grammanalyzer.py templates/1.txt aa#bb
./grammanalyzer.py templates/1.txt aaa#bbb
#reject
echo "Language 1 REJECT"
./grammanalyzer.py templates/1.txt aaa#bb
./grammanalyzer.py templates/1.txt aa#
./grammanalyzer.py templates/1.txt a#
./grammanalyzer.py templates/1.txt \#b
./grammanalyzer.py templates/1.txt b#
./grammanalyzer.py templates/1.txt aa##
./grammanalyzer.py templates/1.txt jaldfkjlajdsfljalsdfasdljfaljdflkja

#lang two
#S->0S0|1S1|#
#accept
echo "Language 2 ACCEPT"
./grammanalyzer.py templates/2.txt 0#0
./grammanalyzer.py templates/2.txt 1#1
./grammanalyzer.py templates/2.txt 00#00
./grammanalyzer.py templates/2.txt 11#11
./grammanalyzer.py templates/2.txt \#

#reject
echo "Language 2 REJECT"
./grammanalyzer.py templates/2.txt 11#10
./grammanalyzer.py templates/2.txt 10#11
./grammanalyzer.py templates/2.txt 1#0
./grammanalyzer.py templates/2.txt 0#1
./grammanalyzer.py templates/2.txt 10101010101010101010101010010101010010101001001010

#lang three
#S->aAb#cC
#A->aAb|#
#C->cC|#

echo "Language 3 ACCEPT"
./grammanalyzer.py templates/3.txt a#b#cc#
./grammanalyzer.py templates/3.txt aaa#bbb#cc#
./grammanalyzer.py templates/3.txt aaa#bbb#c#
./grammanalyzer.py templates/3.txt aaaaa#bbbbb#c#
./grammanalyzer.py templates/3.txt aaa#bbb#ccc#
./grammanalyzer.py templates/3.txt aa#bb#cc#

#reject
echo "Language 3 REJECT"
./grammanalyzer.py templates/3.txt abc
./grammanalyzer.py templates/3.txt aaa#ccc#
./grammanalyzer.py templates/3.txt a#bb#cc#
./grammanalyzer.py templates/3.txt aa#b#cc#
./grammanalyzer.py templates/3.txt aa#b#c#
./grammanalyzer.py templates/3.txt \#


#lang four
#S->1S1|0

echo "Language 4 ACCEPT"
./grammanalyzer.py templates/4.txt 101
./grammanalyzer.py templates/4.txt 11011
./grammanalyzer.py templates/4.txt 0
./grammanalyzer.py templates/4.txt 1110111


#reject
echo "Language 4 REJECT"
./grammanalyzer.py templates/4.txt 1
./grammanalyzer.py templates/4.txt 1101
./grammanalyzer.py templates/4.txt 1011
./grammanalyzer.py templates/4.txt 10
./grammanalyzer.py templates/4.txt 01
./grammanalyzer.py templates/4.txt 2323242424
