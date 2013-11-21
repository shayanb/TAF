#!/usr/bin/env python

#The MIT License (MIT)
#
#Copyright (c) [2013 [Shayan Eskandari]
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import fileinput
import os
import sys

W=6		#window size
K=1	#shift size

def window(seqfile, normFlag):
    ''' to extract windows of size W with the shift size of K from the sequence files (-seq) '''
    seqfilename = os.path.splitext(seqfile)[0]
    norm = open(seqfilename + "_" + str(W) + "W.txt", "w")
    with open(seqfile) as seqfile:
        for line in seqfile:
            sequence=line.split(",")
            end=len(sequence)-W
            for i in xrange(0,end,K):
                for j in xrange(i,W+i):
                    norm.write(sequence[j])
                    norm.write(",")
                if normFlag == True: #checks if -N is indicated adds a 0 flag as normal in the end of the sequence
                    norm.write('0')
                norm.write("\n")
                print "Number of Sequences added: " + str(i)



def unique(file):
    ''' Removes duplicate lines'''
    filename = os.path.splitext(file)[0]
    lines_seen = set() # holds lines already seen
    outfile = open(filename + "_uniq.txt", "w")
    for line in open(file, "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    print "Number of unique sequences: " + str(len(lines_seen))
    outfile.close()



# SHOULD REWRITE THIS TO SOMETHING NICER!
if len(sys.argv) == 2:
    file = sys.argv[1]
    window(file, False)
    filename = os.path.splitext(file)[0]
    unique(filename + "_" + str(W) + "W.txt")
elif len(sys.argv) == 3:
    file = sys.argv[1]
    if sys.argv[2] == '-N': #checks for -N switch
        window(file, True)
    elif sys.argv[2].isdigit():
        file = sys.argv[1]
        W = int(sys.argv[2])
        window(file, False)
    else:
        print "You did not chose to have a normal database"
        window(file, False)
    filename = os.path.splitext(file)[0]
    unique(filename + "_" + str(W) + "W.txt")
else:
    print 'Extract the W sized windows from a systemcall sequence file'
    print 'Input needed: Systemcall sequence file, comma seperated'
    print '              Window size [Default=6]'
    print 'e.g ./SysCallExtract.py trace_seq.txt 6'
    print 'If the input is the Normal trace file (No Anomaly) Add -N (Normal) switch the second for the file to add 0 flag to end of all of the lines'
