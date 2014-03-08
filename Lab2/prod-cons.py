from threading import Thread, Lock, Semaphore
import time
import random
import sys

queue = []
lock = Lock()
def producator(nr,sem,sem2):
	number = range(1000)
	global queue
	while True:
		num = random.choice(number)
		sem.acquire()
		print "Thread-ul", nr, " acceseaza"
    		time.sleep(random.randint(1, 4))
		queue.append(num)
		print "Produced", num
		sem2.release()
		print "Thread-ul", nr, " a terminat"
		time.sleep(random.random())

def consumator(nr,sem,sem2):
	global queue
	while True:
		sem2.acquire()
		print "Thread-ul", nr, " acceseaza"
    		time.sleep(random.randint(1, 4))
		if not queue:
			print "Nothing in the queue"
		else:		
			num = queue.pop(0)
			print "Consumed", num
			sem.release()
			print "Thread-ul", nr, " a terminat"
		time.sleep(random.random())

thread_list = []
semafor = Semaphore(value = 5)
semafor2 = Semaphore(value = 0)

random.seed()

for i in xrange(int(sys.argv[1])):
	thread_prod = Thread(target=producator, args = (i,semafor,semafor2));
	thread_cons = Thread(target=consumator, args = (i,semafor,semafor2));
	thread_prod.start()
	thread_cons.start()
	thread_list.append(thread_prod)
	
for i in xrange(len(thread_list)):
	thread_list[i].join()
				
