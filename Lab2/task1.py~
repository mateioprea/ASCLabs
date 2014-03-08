from threading import Thread
import threading
import time
#a) Folosind clasa Thread, creati 10 threaduri care afiseaza un mesaj de forma:
#    Hello, I'm thread id_thread

#definim o functie ajutatoare
#def my_concurrent_code(nr, msg, id_t):
#	print "Thread", nr, "says:", msg, id_t

#functie smechera



#lista in care punem threadurile ce au pornit
#thread_list = []

#start() de threaduri
#for i in xrange(10):
#	thread = Thread(target = my_concurrent_code, args = (i, "Hello, I'm thread",i))
#	thread.start()
#	thread_list.append(thread)

#join() de threaduri ( asteptam ca fiecare thread sa termine de muncit )
#for i in xrange(10):
#	thread_list[i].join()


def afisare_concurrent_code(**threads):
	for i in threads.keys():
		print i, ':', threads[i], ':' , str(threading.current_thread().getName())
		time.sleep(1)

thread_list = []

for i in xrange (10):
	bla= { "number": i, "msg": "Hello" }
	thread = Thread(target = afisare_concurrent_code, kwargs=bla, name=str(i))
	thread.start()
	thread_list.append(thread)

for i in xrange(10):
	thread_list[i].join()

#b) Modificati codul anterior astfel incat thread-urile sa primeasca un 
#   index si un mesaj date ca parametru sub forma de dictionar
#   *hint: exemplu in lab1 http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#functii

#c) Modificati codul anterior astfel incat thread-urile sa afiseze si numele
#   thread-ului (campul 'name')

#d) Modificati codul anterior astfel incat thread-urile sa primeasca index-ul
#   drept nume al thread-ului, afisati-l ca la punctul b)

