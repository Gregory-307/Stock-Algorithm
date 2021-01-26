import os
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


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
	name = [i for i in listdir for _ in range(500)]
	return name
# for _ in range(1)
def Cores():
	with ProcessPoolExecutor(max_workers = 5) as ppe:
		names = [ppe.submit(my_function)]
		names2 = [f.result() for f in concurrent.futures.as_completed(names)]
		print(names2)
	#return names2
		

if __name__ == '__main__':
	timer2 = time.time()
	Cores()
	print(f'MultiProcessing: {time.time()-timer2}')
#	print(f'Normal: {time1}')
	# timer = time.time()
