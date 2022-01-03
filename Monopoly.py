#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:07:56 2019

@author: leon
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
    

# =============================================================================
# The starting state is assumed to be a start on the Go field, as Monopoly is usually started.
# After a large number of moves (here N = 1000) an equilibrium is reached, which corresponds to the probabilities of staying on the individual fields. 
# =============================================================================


datei = 'Monopoly_with_double'   # Input file can be adjusted 

N = 1000                         # Number of iterations



v = np.zeros((40,1))

v[0,0]=1     

df = pd.read_excel('input/' + datei + '.xlsx')

a=np.array(df)

a=np.copy(a[0:40,1:41])
a.astype(int)


for i in range(N):
    
    v = a @ v     
    
    
prop = pd.DataFrame({'Feld': df['Feld'], 'Wahrscheinlichkeit': v[:,0]})
    
print(prop)
print('\nNorm of vector must be = 1 \nnorm(v) = :', sum(v))  


prop.to_excel('result/' + datei + '_result.xlsx', index=False)


plt.figure(figsize=(7,10))
plt.barh(np.arange(len(prop['Feld'])), np.transpose(prop['Wahrscheinlichkeit']))
plt.axvline(x = 0.025, color="red")
plt.yticks(np.arange(len(prop['Feld'])), np.transpose(prop['Feld']))

plt.title('Aufenthaltswahrscheinlichkeiten : ' + datei)
plt.xlabel("Wahrscheinlichkeit")
plt.ylabel("Feld")

plt.tight_layout()

plt.show
plt.savefig('result/' + datei + '_hist.pdf')
