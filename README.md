TAF
===

Trace Analysis Framework (Version 0.2)


*Parser and tools to extract system call sequences from strace trace of an application.

*exports CSV of system calls: (Process ID, System Call Name/Number, Arguments, Return Values)

*windows the system call sequence to W sized windows (default=6)

*Use STIDE technique to check two databases (Normal, Malicious) to flag the anomaly system call sequence windows in the final file

*outputs flagged system call sequence windows and converts the anomalies to system call name sequences

