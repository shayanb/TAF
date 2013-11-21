#!/usr/bin/env python


# Trace Analysis System with Strace
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
import re
import sys
import csv
import pandas as pd
from syscall_table import SystemCallNumbersi386 as SystemCallNumbers #import the desired architecture as SystemCallNumbers
from syscall_table import Name2Number



def SysCallExtract(Tracefile):

    ''' Matches different parts of the unix strace trace file with their functionalities and outputs two different files
    outputs:
            (inputfilename).csv     parsed version of the trace file in csv format
            (inputfilename)_syscall_seq.txt     only the system call (numbers) sequence with ',' as the seperator

    You can output any of the attributes with testmatch.group("AttributeName")

    AttributeName:
                    PID
                    SysCallName
                    Arguments
                    Returns
    '''

    TracefileName = os.path.splitext(Tracefile)[0]
    outfile = csv.writer(open(TracefileName +'.csv', 'w'))
    outfile.writerow(['PID', 'SysCallName', 'Arguments', 'Returns'])
    syscallfile = open(TracefileName + '_syscall_seq.txt', 'w')
    for line in open(Tracefile):
        testmatch = re.match("(?P<PID>[0-9]*)[ ](?P<SysCallName>[_a-zA-Z0-9]*)\((?P<Arguments>.*)\) *= (?P<Returns>.*)", line)
        if testmatch:
            outfile.writerow([testmatch.group("PID"), testmatch.group("SysCallName"), testmatch.group("Arguments"), testmatch.group("Returns")])
            syscallfile.write(Name2Number(testmatch.group("SysCallName"), SystemCallNumbers))
            syscallfile.write(",")
        elif line.startswith('%'):
            break
    syscallfile.close()
    print "DONE - ", TracefileName , "_syscall_seq.txt and" , TracefileName , ".csv saved!"




if len(sys.argv) > 1:
    Tracefile = sys.argv[1]
    SysCallExtract(Tracefile)
else:
    print 'Input needed: Strace trace file'
    print "e.g ./TAS.py ./trace.txt"
    print 'Support for : strace -o trace.txt -C -f file'
    print 'Output: parsed .csv and systemcall sequence text file'