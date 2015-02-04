#!/usr/bin/python
# -*- coding: utf-8 -*-

import BigInt as lib
import sys
import random
import getopt

class usage(Exception):
    def __init__(self, msg):
        self.msg = msg
        print self.msg

def xgcd(a, b):
	"""Расширенный алгоритм Евклида

	"""

	if a == lib.BigInt(0):
		return 0, 1, b

	if b == lib.BigInt(0):
		return 1, 0, a

	px = lib.BigInt(0)
	ppx = lib.BigInt(1)
	py = lib.BigInt(1)
	ppy = lib.BigInt(0)



	while b > lib.BigInt(0):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y
	
	return ppx, ppy, a


def generate_d(a, b):
	"""Генерирует число d

	"""
	while True:
		x, y, g = xgcd(a, b)
		

		if g != lib.BigInt(1):
			raise ValueError("Невозможно подобрать такое d, чтобы выполнялось условие d * e mod fi = 1.")
		else:
			z=lib.BigInt();
			z = x % b
			
			break
		
		
	return z

def rsa(p,q,e,msg):
	n = p * q
	fi=lib.BigInt()
	fi = (p - lib.BigInt(1)) * (q - lib.BigInt(1))
	
	
	 
	
	if msg > n:
		raise ValueError("Неверная длина сообщения")
	d = generate_d(e, fi)
	
	print ("fi: ") 
	fi.writeNumber(fi)
	print ("\nd: ") 
	fi.writeNumber(d)
	print("\n")
	c=lib.BigInt();
	c=c.powm(msg,e,n)
	#c.writeNumberToFilE("ofile.txt", c, 's');
	print("\nShifrotekst: \n")
	c.writeNumber(c)
	desh=lib.BigInt()
	desh=desh.powm(c,d,n)
	#desh.writeNumberToFilE("ofile.txt", desh, 's');
	print("\nDeshifrotekst: ")
	desh.writeNumber(desh)
	#print("\n")
	#print ("Открытый ключ {",d,n,"} ","Закрытый ключ {",e,n,"}")

#def shifr(msg,e,n):
#	result = lib.BigInt();
#	result=result.Pow(msg,e,n)
#	return result;
#def deshifr(c,d,n):
#	result = lib.BigInt();
	#result=result.Pow(c,d,n)
#	return result;

def main():
	p = lib.BigInt()
	tmp=lib.BigInt()
	q = lib.BigInt()
	e = lib.BigInt()
	msg = lib.BigInt()
	
	
	
	if len(sys.argv) != 5:
		err_num_of_arguments = "Use python rsa.py p q e msg attributes"
		usage(err_num_of_arguments)
	try:
		tmp_num = "";
		tmp_num = tmp.readNumberFromFile(sys.argv[1], 's');
		
		p = lib.BigInt(tmp_num)
		tmp_num = tmp.readNumberFromFile(sys.argv[2], 's');
		q = lib.BigInt(tmp_num)
		#print(tmp_num)
		tmp_num = tmp.readNumberFromFile(sys.argv[3], 's');
		e = lib.BigInt(tmp_num)
		tmp_num = tmp.readNumberFromFile(sys.argv[4], 's');
		msg = lib.BigInt(tmp_num)
	except :
		usage("Something wrong with read files")
	finally:
   		pass
   	tmp = lib.BigInt();
   	
   	rsa(p,q,e,msg)
   	

   	#tmp.writeNumberToFilE("ofile.txt", itog, 's');
   	#tmp.writeNumberToFilE("ofile.txt", q, 's');
   	#tmp.writeNumberToFilE("ofile.txt", e, 's');
   	#tmp.writeNumberToFilE("ofile.txt", msg, 's');




if __name__ == "__main__":
   sys.exit(main())