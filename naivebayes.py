# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:51:47 2018

@author: smsal
"""

documents = [dict() for _ in range(4)]

c = 'Chinese'
j = 'Japan'
prior_c = 0
prior_j = 0
vocab_list = set()
word_ctr = 0
vocab_dict = dict()

# Training Data
documents[0] = {'words':'Chinese Bejing Chinese','class': c}
documents[1] = {'words':'Chinese Chinese Shanghai','class': c}
documents[2] = {'words':'Chinese Macao','class': c}
documents[3] = {'words':'Tokyo Japan Chinese','class': j}

for document in documents:
    dc = document['class']
    if  dc is c: prior_c += 1
    if  dc is j: prior_j += 1
    
    for word in document['words'].split(' '):
        vocab_list.add(word)
        word_ctr += 1

# Create Word Frequencies
for v in vocab_list:
    vocab_dict[v] = 0

for document in documents:
    for word in document['words'].split(' '):
        vocab_dict[word] += 1
        
        
        
print(prior_c)
print(prior_j)
print(vocab_list)
print(vocab_dict)

# Test Data
test = {'words':'Chinese Chinese Chinese Tokyo Japan','class': ''}

answer = {c:prior_c, j: prior_j}

# For Chinese
for word in test['words'].split(' '):
    countwc = 0
    classctr = 0
    for document in documents:
        if document['class'] == c:
            for word2 in document['words'].split(' '):
                if word == word2: countwc += 1
                classctr += 1
    p =  (countwc + 1)/(classctr + len(vocab_list))
    print(p)
    answer[c] = answer[c] * p
    

print(answer)
