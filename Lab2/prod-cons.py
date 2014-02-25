from threading import Thread, Lock, Semaphore
import time
import random
import sys

queue = []
lock = Lock()

def producator(nr,sem):
	number = range(1000)
	global queue
	while True:
		num = random.choice(number)
		sem.acquire()
		print "Thread-ul", nr, " acceseaza"
    		time.sleep(random.randint(1, 4))
    		print "Thread-ul", nr, " a terminat"
		queue.append(num)
		print "Produced", num
		sem.release()
		time.sleep(random.random())

def consumator(nr,sem):
	global queue
	while True:
		sem.acquire()
		print "Thread-ul", nr, " acceseaza"
    		time.sleep(random.randint(1, 4))
    		print "Thread-ul", nr, " a terminat"
		if not queue:
			print "Nothing in the queue"
		num = queue.pop(0)
		print "Consumed", num
		sem.release()
		time.sleep(random.random())

thread_list = []
semafor = Semaphore(value = 1)

random.seed()

for i in xrange(int(sys.argv[1])):
	thread_prod = Thread(target=producator, args = (i,semafor));
	thread_cons = Thread(target=consumator, args = (i,semafor));
	thread_prod.start()
	thread_cons.start()
	thread_list.append(thread_prod)
	
for i in xrange(len(thread_list)):
	thread_list[i].join()
				
