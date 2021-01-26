import os
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import pandas



os.chdir(r'C:\Users\gregb\Downloads')
listdir = os.listdir()
# must be a global function    

# timer = time.time()
# for _ in range(500):
# 	for o in listdir:
# 		print(o)
# time1 = time.time()-timer


# time.sleep(2)




def my_function():
	name = [i for i in listdir]
	return name

def threads():
	with ThreadPoolExecutor(max_workers = 50) as tpe:
		names = [tpe.submit(my_function) for _ in range(500)]
		names2 = [f.result() for f in concurrent.futures.as_completed(names)]
	return names2
		

if __name__ == '__main__':
	timer2 = time.time()
	print(threads())
	print(f'MultiThreading: {time.time()-timer2}')
#	print(f'Normal: {time1}')
	# timer = time.time()







