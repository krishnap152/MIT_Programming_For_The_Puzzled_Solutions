# -*- coding: utf-8 -*-

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B','B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
cap=[]

def pleaseConfirmOpt(caps):
    
    if len(cap)<0: ## code for ensuring that it would not crash on empty list
        caps = caps + [caps[0]]
    
    #print(caps)
    for i in range(1,len(caps)):
       
        if caps[i] != caps[i-1]:
            
            if caps[i] != caps[0]:
                begin = i ## Soution to exercise 2, print like natural commands
            elif i-1 == begin:
                print ('Person at position ', begin, 'flip your cap!')
            else:
                print ('People in positions', begin, 'through', i-1, 'flip your caps!')
                
    
pleaseConfirmOpt(caps)