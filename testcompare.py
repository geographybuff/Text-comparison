# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:48:20 2019

@author: Owner
"""

import textcompare
import numpy as np
n9841 = open('1984Chapter1.txt', 'r').read()
n9842 = open('1984Chapter2.txt', 'r').read()
hobbit1 = open('TheHobbitChapter1.txt', 'r').read()
hobbit2 = open('TheHobbitChapter2.txt', 'r').read()
ge1 = open('GreatExpectationsChapter1.txt', 'r').read()
ge2 = open('GreatExpectationsChapter2.txt', 'r').read()
pp12 = open('PrideandPrejudiceChapter1-2.txt', 'r').read()
pp3 = open('PrideandPrejudiceChapter3.txt', 'r').read()
hs1 = open('HindSwarajChapter1.txt', 'r').read()
hs24 = open('HindSwarajChapter2-4.txt', 'r').read()
ts1 = open('TomSawyerChapter1.txt', 'r').read()
ts2 = open('TomSawyerChapter2.txt', 'r').read()
passages = [n9841, n9842, hobbit1, hobbit2, ge1, ge2, pp12, pp3, hs1, hs24, ts1, ts2]
comparisonarray = [[textcompare.compare(i, j) if passages.index(i) < passages.index(j) < len(passages) else 0 for j in passages[1::]] for i in passages[:-1]]

print(comparisonarray)        