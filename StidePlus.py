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
from syscall_table import Number2Name
from syscall_table import SystemCallNumbersi386 as SystemCallNumbers


def compare(norm,malware, window):
    #normfilename = os.path.basename(norm)
    normfilename = os.path.splitext(norm)[0]
    malwarefilename = os.path.basename(malware)
    malwarefilename = os.path.splitext(malwarefilename)[0]
    OUTPUT = normfilename + "_" + malwarefilename + "_flagged.csv"
    MalicousSeqfilename = normfilename + "_" + malwarefilename + "_anamoly.csv"
    MalicousSeq = open(MalicousSeqfilename, "w")
    seq = open(OUTPUT , "w")
    Header = 'S1' #header for the csv file
    for i in xrange(1,window):
        Header = Header + ",S" + str(i+1)
    Header = Header + ",flag\n"
    seq.write(Header)
    with open(malware) as malfile:
        for line in malfile:
            if line in open(norm).read():
                print line
                seq.write(line.rstrip('\n'))
                seq.write("0")
                seq.write("\n")
                print line
            else:
                MalicousSeq.write(Number2Name(line.rstrip('\n'), SystemCallNumbers))
                MalicousSeq.write("\n")
                seq.write(line.rstrip('\n'))
                seq.write("1")
                seq.write("\n")
    MalicousSeq.close()
    seq.close()


if len(sys.argv) > 3:
    norm = sys.argv[1]
    secondfile = sys.argv[2]
    window = int(sys.argv[3])
    compare(norm, secondfile, window)

else:
    print 'Input needed: "Normal Database" "Sequence of the anomaly included" "windowsize" '
    print "e.g ./compare_STIDE.py Normal_seq_6W.txt trace_seq_6W.txt 6"
    # print 'Regex for : strace -o trace.txt -C -f file'
    print 'Output: flags the second file (the 0 as normal and 1 as anomaly)'

