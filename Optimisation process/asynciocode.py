
import os
import asyncio
import time

os.chdir(r'C:\Users\gregb\Downloads')
listdir = os.listdir()
# must be a global function    

# timer = time.time()
# for _ in range(500):
# 	for o in listdir:
# 		print(o)
# time1 = time.time()-timer


# time.sleep(2)

async def my_afunction():
	names = [i for i in listdir]
	print(names)
	return(names)
	
async def Aiomain():
	aloop = [loop.create_task(my_afunction()) for x in range(100)]
	# for x in range(500):
	# 	aloop.append())
	await asyncio.wait(aloop)

if __name__ == '__main__':
	timer2 = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(Aiomain())
	loop.close()
#	print(time1)
	print(time.time()-timer2)
			
