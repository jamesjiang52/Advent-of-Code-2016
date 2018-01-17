# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:16:17 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_triples = []
for line in all_lines:
    numbers_string = line.split(' ')
    while '' in numbers_string:
        numbers_string.remove('')
    numbers = [int(i) for i in numbers_string]
    all_triples.append(numbers)

total = 0    
for triple in all_triples:
    max_index = triple.index(max(triple))
    if max_index == 0:
        if triple[1] + triple[2] > triple[0]:
            total += 1
    elif max_index == 1:
        if triple[0] + triple[2] > triple[1]:
            total += 1
    elif max_index == 2:
        if triple[0] + triple[1] > triple[2]:
            total += 1

print(total)
