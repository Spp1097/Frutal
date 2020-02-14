# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:25:43 2020

@author: santi
"""

#import pandas as pd
import os
from functions import *

#inventario = pd.read_csv('inventario_peq.csv',index_col='Fruta')

'''
ns = {'Fruta':'Frutos Rojos','Cantidad':6}

inventario = inventario.append(ns,ignore_index = True)

print(inventario)

inventario.to_csv('inventario_peq.csv')
'''

active  = True 


while active:
	do = menu()
	active = validate(do,lista = ['i','v','a'])
	
	if do == 'i':
		load_inv()
			
	if do == 'a':
		validate_add()
		
	if do == 'v':
		ventas()
		
	os.system("clc")
		
	
	
	

	
		
	

	



