## Problem
Write a program in any programming language of your preference to sort 1
million of signed 32-bit integers using 3 MB of memory.

## Approach
* Challenge: 1 million signed 32-bit integers = 4,000,000 bytes of memory which 
is larger than 3 MB of memory (3,000,000 bytes in decimal)

* Solution: Using external merge sort algorithm, which sorts chunks 
that each fit in RAM, then merges the sorted chunks together
    
1. Read 400,000 bytes of the data in main memory and sort by mergesort 
on the list in Python - sorted() built-in function that builds a new 
sorted list from an iterable.

2. Write the sorted data to temporary disk.

3. Repeat steps 1 and 2 until all of the data is in sorted 400,000 bytes chunks 
(there are 400,0000 bytes / 400,000 bytes = 10 chunks), which now need to be 
merged into one single output file - heapq.merge() function.

## Environment
- OS: Ubuntu
- Python: Python 2.7.6 version

## How to run
$ python sorting.py

## Output
1 million sorted signed 32-bit integers in output.txt file

## References
1. Sorting a Million 32-bit integers in 2MB of RAM using Python:
https://gist.github.com/arunenigma/8177109
http://neopythonic.blogspot.com/2008/10/sorting-million-32-bit-integers-in-2mb.html

2. Sorting Mini-HOW TO in Python
https://wiki.python.org/moin/HowTo/Sorting

3. External sorting
https://en.wikipedia.org/wiki/External_sorting
