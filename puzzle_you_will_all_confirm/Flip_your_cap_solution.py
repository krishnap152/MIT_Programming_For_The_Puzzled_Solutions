# -*- coding: utf-8 -*-

#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B','B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConfirm(caps):
    ## Initialization 
    start = 0
    forward = 0
    backward = 0
    interval = []
    
    for i in range(1, len(caps)):
        ## print("cap start", caps[start] + " cap i : "+caps[i])
        
        if caps[start] != caps[i]:
            ## Creating tuples start,end and type and appending it in interval
            interval.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward +=1
            
            start = i
    ## need to add last interval after the loop completes
    interval.append((start,len(caps)-1,caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    
    if backward < forward:
        flip = 'B'
    else :
        flip = 'F'
    
    for t in interval:
        if t[2] == flip:
            if t[0] == t[1]: ## solution to exercise 1
                print("people in position",t[0]," flip your caps")
            else :
                print("people in positions",t[0],"through ",t[1], " flip your caps")

 # print("intervals : ", interval)
 # print("forward : ", forward)
 # print("backward : ", backward)
pleaseConfirm(caps)    
pleaseConfirm(cap2)