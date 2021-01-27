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
import math as mt
import time 

print('Assume 1 year annual interest',
      'if question does not state explicitly.')
print('Assume nominal annual rates.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def simpleInterest():
    
    P = float(input('Input present amount P:'))
    i = float(input('Input interest rate i:'))
    F = P*(1+i)
    
    print('\nFuture Amount is:',F)
    
    time.sleep(3)
    main()

def compoundInterest():
    P = float(input('Input present amount P:'))
    i = float(input('Input interest rate i:'))
    N = float(input('Input period:'))
    F = P*(1+i)**N
    
    print('\nFuture Amount is:',F)

    time.sleep(3)
    main()

def rateManipulation():
    
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

    print(k)           
    # P = float(input('Input present amount P:'))
    r = float(input('Input nominal annual interest as decimal (r):'))
    m = float(input('Input compounding period (m):'))
    # k = float(input('Input how many {x} in thing:'.format(x=oldPeriod)))
    
    iek = ((1+r/m)**k)-1
    
    # print(iek)
    print('\nNew rate manipulation is: ',iek)

    time.sleep(3)
    main()


"""~~~~~~~~~MAIN FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def main():
    fnc = input('Enter to call a function:\n'
                '1 - Rate Manipulation\n' 
                '2 - Simple Interest\n'
                '3 - Compound Interest ')
    if fnc =='1':
        rateManipulation()
    if fnc =='3':
        compoundInterest()
    if fnc =='2':
        simpleInterest()
        
"""~~~~~~~~~MAIN FUNCTION~end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

main()
    # r = input('Input Nominal Annual Interest r:')
    # m = input('Commounding Period m:')
    # P = input('Input present amount of money')
    # isub = r/m
    # F = ('Future Amount = ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

