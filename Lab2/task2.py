#!/usr/bin/python
from threading import Lock, Thread
from time import sleep
from random import choice, randint
import sys
lista = [1,2,3,4,5,6,7,8,9,10]
lista2= []
global_var = 0
thread_list = []

def functie(l1,l2,lock):
	fac_append=(choice(l1))
	global global_var
	lock.acquire()
	global_var+=fac_append
	lock.release()
	l2.append(fac_append)
	

for i in xrange(int(sys.argv[1])):
	sleep(randint(1, 4))
	thread = Thread(target = functie, args = (lista,lista2,Lock()))
	thread.start()
	print thread.getName()
	print lista2
	print global_var
	thread_list.append(thread)

for i in xrange(len(thread_list)):
	thread_list[i].join()

# Scrieti un program in care mai multe threaduri (numarul lor este dat ca
# argument in linia de comanda) aleg random un element dintr-o lista comuna si
# le adauga intr-o lista rezultat (tot comuna).
# a) in fiecare thread, afisati numele threadului si varianta din acel moment 
#    a listei rezultat
# b) in fiecare thread adunati elementul la o variabila globala. Protejati 
#    accesul la aceasta
# c) faceti thread-urile sa astepte un numar random de secunde pana sa inceapa
#    executia. Hint: modulul time
#   
