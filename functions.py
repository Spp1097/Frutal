# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:51:06 2020

@author: santi
"""

import pandas as pd

def open_csv_file(name):
	temp = pd.read_csv(name,index_col=0)
	return temp

def menu():
	print('******************************************')
	print('*          MENU PRINCIPAL                *')
	print("*   Presione [I] para ver inventario     *")
	print("*   Presione [A] para añadir inventario  *")
	print("*   Presione [S] para salir              *")
	print("*   Presione [V] para venta              *")
	print('******************************************')
	a = (input('Que desea hacer: '))
	
	return a


def validate(num,lista):
	
	if num in lista or num == '\n':
		
		return True
	if num == 's':
		print("\n\n******Te esperamos de nuevo...******")
		return False
	if num not in lista:
		print ("\n\n*****Ingrese opcion valida*****\n\n")
		return True
	
	
def load_inv():
	#inventario = pd.read_csv('inventario_peq.csv',index_col=0)
	
	inventario  = open_csv_file('inventario_peq.csv')
	print('\n\n','*'*50)
	print(inventario)
	
	print('*'*50,'\n\n')

def validate_sabor(sabor,dict_sabores):
	l = [0,1]
	if sabor not in dict_sabores:
		print('\n\n','*'*50,'\n{} no esta en la lista de frutas'.format(sabor),
	'\n¿Desea Agegar sabor ?','\n\n')
		print ('Presione [1] para agregar')
		print( 'Presione [0] para regresar')
		ans = int(input('Agregar/Regresar: '))
		
		if ans not in l :
			print('\n\n******Ingrese una opcion válida*****')
				
		else :
			return ans
		
	
	
	
def validate_add():
	print('Presione[1] para ingresar sabor al inventario')
	print('Presione[0] para regresar')
	temp = int(input())
	
	if temp==1:		
		sabor = input("Ingrese sabor: ")
		cantidad =int( input("Ingrese cantidad: "))
		
		add(sabor,cantidad)
	
	
def add(sabor,cantidad):
	exist = True
	inventario = open_csv_file('inventario_peq.csv')
	
	frutas = inventario.Fruta
	cant = inventario.Cantidad
			
	d = dict(zip(frutas,cant))
	
	val_sab = validate_sabor(sabor,d)
	
	
	if val_sab == 1:
		d[sabor] = 0
	
	if val_sab == 0:
		exist = False
		
	if exist == True:		
		d[sabor]+=cantidad
		#print(d[sabor])
		inv = {'Fruta': list(d.keys()),'Cantidad':list(d.values())}
		df = pd.DataFrame(inv)			
		df.to_csv('inventario_peq.csv')
		
		print('*'*50)
		print(df)
		print('*'*50)
	
def ventas():
	
	print('Presione[1] para ingresar venta')
	print('Presione[0] para regresar')
	decision = int(input())
	
	
	if decision == 1:
		inventario = open_csv_file('inventario_peq.csv')
		dic_vendidas ={}
		frutas = inventario.Fruta
		cant = inventario.Cantidad				
		inv = dict(zip(frutas,cant))
		
		
		
		
		
		vendidas = input('Ingrese pulpas vendidas: ')
		vendidas = vendidas.split(',')
		
		cont = 0
		while len(vendidas)>0:
			dic_vendidas[vendidas[0]]=vendidas[cont+1]
			vendidas.pop(cont)
			vendidas.pop(cont)
			
		
		for fruta in dic_vendidas:
			inv[fruta]-=int(dic_vendidas[fruta])
			
		inv_updated = {'Fruta':list(inv.keys()),'Cantidad':list(inv.values())}
		df_inv = pd.DataFrame(inv_updated)
		df_inv.to_csv('inventario_peq.csv')