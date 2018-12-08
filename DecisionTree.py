# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:44:17 2018

@author: smsal
"""


"""" Based on some heuristics decides whtehter a given word that contains . is a Probable EOS Marker or not"""
def isProbableEOS(word):
    capitalNo = 0
    periodNo = 0
    for letter in word:
        if (letter.isupper()): capitalNo +=1
        if (letter is '.'): periodNo += 1
     
    if (len(word) < 5 and periodNo >= 1): return False
    if (capitalNo / len(word) >= 0.4): return False
    return True


""""Given a string, adds Starts of Sentence and End of Sentence markers accordingly """
def computeEOS(str):
    punct = ["?","!"]
    output = "<S> "
    SOS = "<S>"
    EOS = "</S>"
    tokens = str.split(sep=' ')
    
    for i in range(len(tokens)):
        token = tokens[i]
        if token[len(token)-1] in punct:
            output = output + token[:len(token)-1] + " " + EOS + " " + SOS + " "
        else:
            if i == len(tokens) - 1 and isProbableEOS(token): output = output + token[:len(token)-1] + " " + EOS
            elif token[len(token)-1] == '.'  and isProbableEOS(token):
                output = output + token[:len(token)-1] + " " + EOS + " " + SOS + " "
            
            else: output = output + token + " "
            
    return output


str = ""
for line in open("C:\\Users\\smsal\\OneDrive\\Documents\\input.txt","r").readlines():
    str = str + line
    
            
print(computeEOS(str))




        
    
    