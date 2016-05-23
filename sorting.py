"""
    Sorting a million of signed 32-bit integers using 3 MB of memory.
"""
import array
import heapq
import random
import struct
import tempfile

# Create a million signed 32-bit integers into input file input.txt
with open('input.txt', 'wb') as inputdata:
    for x in xrange(1000000):
        integer = random.randint(0, 999999)
        b = struct.pack('i', integer)
        inputdata.write(b)


def get_integers(tf):
    while True:
        arr = array.array('i')
        arr.fromstring(tf.read(400000))  # 100,000 integers of 4 bytes each = 400,000 bytes
        if not arr:
            break
        for i in arr:
            yield i

iters = []
inp = open('input.txt', 'rb')

# This repeatedly reads a chunk of 100,000 integers from the input file, sorts them in memory, 
#and writes them to a temporary file
while True:
    a = array.array('i')
    a.fromstring(inp.read(400000))
    if not a:
        break
    f = tempfile.TemporaryFile()
    array.array('i', sorted(a)).tofile(f)
    f.seek(0)  
    iters.append(get_integers(f))

a = array.array('i')
out = open('output.txt', 'wb')

# Merge all these files (each of which is sorted) together using heapq.merge() function
for x in heapq.merge(*iters):
    a.append(x)

# Write the result into output.txt file    
out.write(str(a))
out.close()