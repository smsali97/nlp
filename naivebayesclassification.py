# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:44:51 2018

@author: smsal
"""

"""
Given a list of documents with their corresponding classes as tuples, tells the class of 
an unkown test document
"""
def naiveBayes(megaDocument=list(),testDocument=list()):
    vocab = len(set([word for d in megaDocument for word in d[0]]))
    classList = [d[1] for d in megaDocument]
    classes = set(classList)
    
    classTotal = {c: 0 for c in classes}
    for c in classes:
        for d in megaDocument:
            for word in d[0]:
                if d[1] == c: classTotal[c] = classTotal[c] + 1
    
    # prior probabilities
    prior_prob = {c: 0 for c in classes}
    for c in classList: 
        prior_prob[c] = prior_prob[c] + 1

    answer = {}
    # give initial probabiility to answer i.e P(c)
    for c in classes:
        answer[c] = prior_prob[c]/ len(classList)
    
    # for each class
    for c in classes:
        # for each word in test doc i.e P(d|c) = P(w1|c) * P(w2|c) ..
        for word in testDocument:
            # numerator count(w, c) + 1 i.e P (w and c)
            num = len([w for d in megaDocument for w in d[0] 
                       if w == word and d[1] == c]) + 1
            # denominator count(c) + V i.e  P (c)
            den =  classTotal[c] + vocab
            
            answer[c] = answer[c] * num/den
    
    print(answer)       
    return max(answer,key= lambda k: answer[k])


megaDocument = list() 
megaDocument.append(tuple(['Chinese Bejing Chinese'.split(),'c']))
megaDocument.append(tuple(['Chinese Chinese Shanghai'.split(),'c']))
megaDocument.append(tuple(['Chinese Macao'.split(),'c']))
megaDocument.append(tuple(['Tokyo Japan Chinese'.split(),'j']))

testDocument = 'Chinese Chinese Chinese Tokyo Japan'.split()

output = naiveBayes(megaDocument,testDocument)
print(output)
