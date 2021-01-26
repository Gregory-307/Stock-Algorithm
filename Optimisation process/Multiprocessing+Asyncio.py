import os
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio



os.chdir(r'C:\Users\gregb\Downloads')
listdir = os.listdir()
# must be a global function    


def my_function():
	name = [i for i in listdir]
	return name
# for _ in range(1)

async def my_afunction():
	name = [i for i in listdir]
	return(name)
	
	
	
async def Aiomain(aloop):
	#print('mew2')
	runningtask = [aloop.create_task(my_afunction()) for _ in range(100)]
	await asyncio.wait(runningtask)
	# for x in runningtask:
	# 	print(x.result())
	

def Aiomainrun(newloop):
	#print('mew2')
	asyncio.set_event_loop(newloop)
	names = [newloop.run_until_complete(Aiomain(newloop) for _ in range(10))]
	

# def AioThread():
# 	with ThreadPoolExecutor(max_workers = 1) as tpe:
# 		Aioloops = tpe.submit(Aiomainrun())


def Cores():
	mew = 0
	with ProcessPoolExecutor(max_workers = 7) as ppe:
		LoopsDict = {}
		for o in range(50):
			key = 'loop' + str(o)
			new_loop = asyncio.new_event_loop()
			#print('new loop created: ' + key)
			LoopsDict[key] = new_loop

		fs = []
		for k, l in LoopsDict.items():
			asyncio.set_event_loop(l)
			fs.append(ppe.submit(l.run_until_complete(Aiomain(l))))

		concurrent.futures.wait(fs)


		for k, l in LoopsDict.items():
			#print('closing loop ' + k)
			LoopsDict[k].close()
			#print(l)
		
		
		# # 	names2 = [f.result() ]

		
	#return names2
if __name__ == '__main__':
	timer2 = time.time()
	Cores()
	print(f'MultiProcessing: {time.time()-timer2}')
			
