TAF
===

Trace Analysis Framework (Version 0.2)


* Parser and tools to extract system call sequences from strace trace of an application.

* exports CSV of system calls: (Process ID, System Call Name/Number, Arguments, Return Values)

* windows the system call sequence to W sized windows (default=6)

* Use STIDE technique to check two databases (Normal, Malicious) to flag the anomaly system call sequence windows in the final file

* outputs flagged system call sequence windows and converts the anomalies to system call name sequences


![TAF](/docs/TAF.png)


The MIT License (MIT)

Copyright (c) [2013 [Shayan Eskandari]

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
