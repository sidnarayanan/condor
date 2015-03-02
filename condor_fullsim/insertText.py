#!/usr/bin/env python

# inserts contents of argv[1] into argv[2] starting at line argv[3]
# outputs to stdout

from sys import argv,stdout

f1 = open(argv[1],'r')
f2 = open(argv[2],'r')
nLines = int(argv[3])

i=0
write=stdout.write
for l2 in f2.readlines():
    write(l2)
    if i==nLines:
        for l1 in f1.readlines():
            write(l1)
    i+=1
