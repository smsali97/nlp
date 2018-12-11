# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:17:37 2018

@author: mmaaz
"""

import collections
doc1= "I did enact Julius Caesar I was killed i' the Capitol Brutus killed me"
doc2 ="So let it be with Caesar The noble Brutus hath told you Caesar was ambitious"

my_doc1= (doc1, 1)
my_doc2= (doc2, 2)

doclist= [my_doc1, my_doc2]

defDict= collections.defaultdict(list)
for document in doclist:
    doc=document[0]
    index= document[1]
    for word in doc.split():
        defDict[word.lower()].append(index)
        
for key, value in sorted(defDict.items()):
    print(str(key) + ' ' + str(value) + '\n')