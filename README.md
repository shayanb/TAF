TAF
===

Trace Analysis Framework (Version 0.2)

* Parser and tools to extract system call sequences from strace trace of an application.

* exports CSV of system calls: (Process ID, System Call Name/Number, Arguments, Return Values)

* windows the system call sequence to W sized windows (default=6)

* Use STIDE technique to check two databases (Normal, Malicious) to flag the anomaly system call sequence windows in the final file

* outputs flagged system call sequence windows and converts the anomalies to system call name sequences

(Support for default switches with following the forks: strace -o trace.txt -C -f file)

![TAF](/docs/TAF.png)

for more information see the readme in /docs/

TODO
-----
* Add support for adding fields in the trace (time, relative time, ...)

* Automate the whole process (not sure if this is needed, cause personally I needed every output of each python file so that would be one run for all the outputs.)



STIDE technique Readings:
------------------------
Forrest et al. employed a methodology motivated by immune systems. 
This characterizes the problem as distinguishing ‘self’ from ‘non-self’ (normal and abnormal behaviors respectively). An event horizon is built from a sliding window applied to the sequence of system calls made by an application during normal use. The sequences formed by the sliding window are stored in a table that establishes the normal behavior model. During the deployment (detection) phase, if the pattern from the sliding window is not in the normal behavior database it is considered a mismatch.
Input to the Stide detector takes the form of system call traces of an application for which the detector is trained. Specifically, Stide builds a “normal database” by segmenting the training data (of system call traces) into fixed length sequences . To do so, a sliding window of N is employed over the training dataset and the resulting system call patterns are stored in the “normal database”. During testing, the same sliding window size is employed on the data. Resulting patterns are compared against the “normal database” and if there is no match, a mismatch is recorded. Given a window size of N and system call trace length M, anomaly rate for the trace is calculated by dividing the number of mismatches by the number of sliding window patterns (i.e. M – N + 1).
[4]


1- S. Forrest, S. Hofmeyr, A. SoMayaji, and T. Longstaff, “A sense of self for Unix processes,” in Security and Privacy, 1996. Proceedings., 1996 IEEE Symposium on, May. 1996, pp. 120–128.

2- S. Forrest, S. A. Hofmeyr, and A. SoMayaji, “Computer immunology,” Commun. ACM, vol. 40, no. 10, pp. 88–96, Oct. 1997.[Online]. Available: http://doi.acm.org/10.1145/262793.262811 

3- S. A. Hofmeyr, S. Forrest, and A. SoMayaji, “Intrusion detection using sequences of system calls.” Journal of Computer Security, vol. 6, no. 3, p. 151, 1998. [Online]. Available: http://search.ebscohost.com/login.aspx?
direct=true&db=tsh&AN=1531432&site=ehost- live

4- Kayacık, H. G., & Zincir-Heywood, A. N. (2008). Mimicry Attacks Demystified: What Can Attackers Do To Evade Detection? (A. N. Zincir-Heywood, Ed.), 1–11.



The MIT License (MIT)
----------------------

Copyright (c) [2013] [Shayan Eskandari] [Shayan [ a t ] theshayan.com]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
