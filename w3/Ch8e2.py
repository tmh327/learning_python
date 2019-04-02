#!/usr/bin/env python3
prefix = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefix:
    if letter in "OQ":
        print (letter + 'u' + suffix)
    print(letter + suffix)

