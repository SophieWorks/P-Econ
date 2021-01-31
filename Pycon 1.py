# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:48:07 2021

This program is to assist in Engineering Econ Calculations;
specifacly for quiz 1, which includes the need for simple
and compound interest calculations, understanding 
effective and nomial rates for compounding,
continuous compounding, straight line depreciation, 
declining balance depreciation, and rate manipulation.

@author: sophi
"""
import numpy as np
import math
import time 

print('Assume 1 year annual interest',
      'if question does not state explicitly.')
print('Assume nominal annual rates.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def simpleInterest():

    print('\nInsert 1 if not used')
    time.sleep(1)    

    P = float(input('Input present amount P:'))
    i = float(input('Input interest rate (i):'))/100
    N = float(input('Input period:'))
    F = P*(1+i*N)
    
    print('\nFuture Amount is:',F)
    
    time.sleep(3)
    main()

def compoundInterest():
    
    print('\nInsert 1 if not used')
    time.sleep(1)
    
    P = float(input('Input present amount P:'))
    i = float(input('Input interest rate (i):'))/100
    N = float(input('Input period in years (n):'))
    F = float(input('Input Future Amount:'))
    
    if F==1:
        F = P*(1+i)**N
        print('\nFuture Amount is:',F)
    
    if P==1:
        P = F/((1+i)**N)
        print('\nNeeded money today is', P)    
    


    time.sleep(3)
    main()

def rateManipulation():
    
    print('\nInsert 1 if not used')
    time.sleep(1)
    
    ieff = float(input('Input effective interest (if q gives):'))/100
    
    oldPeriod = input('Changing from:'
                  ' \n(1-Daily, 2-Weekly, '
                  '3-Monthly, 4-Quarterly, 5-Semiannually'
                  ' 6-Annually)\nPlease Type: ')
    if oldPeriod =='1':
        x=float(365)
    if oldPeriod =='2':
        x=float(52)
    if oldPeriod =='3':
        x=float(12)
    if oldPeriod =='4':
        x=float(4)
    if oldPeriod =='5':
        x=float(2)
    if oldPeriod =='6':
        x=float(1)
        
    newPeriod = input('Changing from:'
                  ' \n(1-Daily, 2-Weekly, '
                  '3-Monthly, 4-Quarterly, 5-Semiannually'
                  ' 6-Annually)\nPlease Type: ')
    if newPeriod =='1':
        y=float(365)
    if newPeriod =='2':
        y=float(52)
    if newPeriod =='3':
        y=float(12)
    if newPeriod =='4':
        y=float(4)
    if newPeriod =='5':
        y=float(2)
    if newPeriod =='6':
        y=float(1)
        
    k = x/y

    # print(k)           
    # P = float(input('Input present amount P:'))
    r = float(input('Input nominal annual interest (r):'))/100
    m = float(input('Input compounding period (m):'))
    # k = float(input('Input how many {x} in thing:'.format(x=oldPeriod)))
    
    iek = ((1+r/m)**k)-1
    
    # if m==1:
    #     m = np.log(ieff+1)/np.log*()
    
    # print(iek)
    print('\nNew rate manipulation is: ',iek*100, '\N{PERCENT SIGN}')

    time.sleep(2)
    main()



def nomeffInterest():
    print('\nInsert 1 if not used')
    time.sleep(1)
    
    P = float(input('Input present amount (P):'))
    r = float(input('Input nominal annual interest (r):'))/100
    m = float(input('Input compounding period (m):'))
    n = float(input('Input time in years (n):'))
    F = float(input('Input future amount (F):'))
    
    isub = r/m 
    N = m*n 
    ieff = (((1+isub)**m)-1)
    
    if F==1:
        F = P*(1+isub)**N
        print('\nFuture amount is', F)
    if r==0.01:
        ieffNew = (F/P)**(1/n)
        r = ((ieffNew)**(1/2)-1)*2
        print('\nAnnual Nominal interest is', r)
    if P ==1:
        P = F/(((1+(ieff))**n)-1)
        print('\nNeeded money today is', P)

     
    
    # print('\nEffective interest rate is', ieff,'\N{PERCENT SIGN}')
    
    
    time.sleep(2)
    main()

def contInterest():
    
    print('\nInsert 1 if not used')
    time.sleep(1)
    
    P = float(input('Input present amount (P):'))
    r = float(input('Input nominal annual interest (r):'))/100
    n = float(input('Input time in years (n):'))
    
    
    F = P*(math.exp(r*n))
    ieff = (math.exp(r)-1)*100
    print('\nEffective interest rate is', ieff,'\N{PERCENT SIGN}')
    print('\nFuture amount is', F)

    time.sleep(2)
    main()


def SLDepreciation():
    N = int(input('Input useful life in years (N):'))
    P = float(input('Input purchase price (P):'))
    S = float(input('Input salvage value (S):'))
    
    dep = float((P-S)/N)
    print('\nDepreciation is: ', dep)

    i = np.arange(1,N+1,1)
    
    print('\n')
    for n in i:
        bv = P-(n*(dep))
        ad = n*(dep)
        print('Year {i}'.format(i=n))
        print('Book Value: ',bv)
        print('Accumulated Depreciation: ',ad)
        print('\n')
    
    time.sleep(2)
    main()
    

def DBDepreciation():

    print('\nInsert 1 if not used')
    time.sleep(1)

    P = float(input('Input purchase price (P):'))
    S = float(input('Input salvage value (S):'))
    d = float(input('Input depreciation rate (d):'))/100 
    N = int(input('Input useful life in years (N):'))
    
    
    if d == 0.01:
        d = 1- (S/P)**(1/N)
        print('\nDep Rate is', d*100,'\N{PERCENT SIGN}')
    
    i = np.arange(1,N+1,1)
    
    print('\n')
    for n in i:
        bv = P*(1-d)**n
        bv_1 = P*(1-d)**(n-1)
        dep = (bv_1)*d

        print('\nYear {i}'.format(i=n))
        print('Book Value is: ', bv)
        print('Depreciation charge is: ', dep)

    
    
    
    
"""~~~~~~~~~MAIN FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def main():
   
    try:
        running = True
        while running:
            fnc = int(input('Enter to call a function:\n'
                        '1 - Rate Manipulation\n' 
                        '2 - Simple Interest\n'
                        '3 - Compound Interest\n'
                        '4 - Nominal Compound Interest\n'
                        '5 - Continuous Interest\n'
                        '6 - SL Dep\n'
                        '7 - DB Dep\n'
                        '9 - Exit\n'))
            if fnc ==1:
                print('\nCalled Rate Manipulator!\n')
                rateManipulation()
                running = False
            if fnc ==2:
                print('\nCalled Simple Interest!\n')
                simpleInterest()
                running = False
            if fnc ==3:
                print('\nCalled Compound Interest!\n') 
                compoundInterest()
                running = False
            if fnc ==4:
                print('\nCalled Nominal Effective Comppound Interest!\n')
                nomeffInterest()
                running = False
            if fnc ==5:
                print('\nCalled Continuous Interest!\n')
                contInterest()
                running = False
            if fnc ==6:
                print('\nCalled SL Dep!\n')
                SLDepreciation()
                running = False
            if fnc ==7:
                print('\nCalled DB Dep!\n')
                DBDepreciation()
                running = False
                
                
    
            if fnc ==9:
                print('\nExiting Function!')
                running = False
    except ValueError:
        print('\nInput a valid number! Try again...')
        main()
            
"""~~~~~~~~~MAIN FUNCTION~end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

main()



    
    

