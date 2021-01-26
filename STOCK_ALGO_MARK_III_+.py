
from pip._internal import main as pipmain

try:
	from selenium import webdriver
except:
	print("Selenium not found")
	pipmain(['install', 'selenium'])
	from selenium import webdriver

import urllib

try:
	import re
except:
	print("'re' not found")
	pipmain(['install', 're'])
	import re

try:
	import pandas as pd
except:
	print("Pandas not found")
	pipmain(['install', 'pandas'])
	import pandas as pd

try:
	from newspaper import Article
except:
	print("newspaper not found")
	pipmain(['install', 'newspaper3k'])
	from newspaper import Article

try:
	from collections import Counter
except:
	print("Collections not found")
	pipmain(['install', 'collections'])
	from collections import Counter

try:
	from pandas_datareader import data, wb
except:
	print("Pandas DataReader not found")
	pipmain(['install', 'pandas_datareader'])
	from pandas_datareader import data, wb

try:
	import matplotlib.pyplot as plt; plt.rcdefaults()
except:
	print("matplotlib not found")
	pipmain(['install', 'matplotlib'])
	import matplotlib.pyplot as plt; plt.rcdefaults()
import random
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *
import os
import natsort
import time
import datetime
from datetime import date
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import math 
import decimal
from pandas.plotting import scatter_matrix
import multiprocessing
from ast import literal_eval
import subprocess
import operator
import pylab
from matplotlib import interactive

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
} 

pd.set_option('precision',16)
#os.environ['MOZ_HEADLESS'] = '1'

home = r'C:\python'
save = r'C:\python\So far'
profile_path=r"C:\Users\Grego\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default"
TOR = r"C:\Users\Grego\Desktop\Tor Browser\Browser"
DataSets = r"C:\python\So far\Data Sets"

window = tk.Tk()

window.title("Data Download")

window.geometry("650x900")

os.chdir(save)

Correlation_technique = 'pearson'

global today
today = date.today()

"""Default"""
entryText1 = tk.StringVar()
entryText2 = tk.StringVar()
entryText3 = tk.StringVar()
entryText4 = tk.StringVar()
entryText5 = tk.StringVar()
entryText6 = tk.StringVar()
entryText7 = tk.StringVar()
entryText8 = tk.StringVar()
entryText9 = tk.StringVar()
entryText10 = tk.StringVar()
entryText11 = tk.StringVar()
entryText12 = tk.StringVar()
entryText13 = tk.StringVar()
entryText14 = tk.StringVar()
entryText15 = tk.StringVar()
entryText16 = tk.StringVar()
entryText1.set( "Insert Term" )
entryText2.set( "Insert Term" )
entryText3.set( "Insert Term" )
entryText4.set( "Insert Term" )
entryText5.set( "Insert Term" )
entryText6.set( "Insert Term" )
entryText7.set( "Insert Term" )
entryText8.set( "Insert Term" )
entryText9.set( "Insert Term" )
try:
	with open("LastStock.txt", "r", encoding="utf8") as f:
		StockTerm = [line.strip() for line in f][0]
except:
	StockTerm = 'Insert Stock Symbol'
	pass
entryText14.set( "Insert Starting Date" )
entryText15.set( "Insert Ending Date" )
entryText13.set( "Insert Amount" )

"""Initial Values"""
#global rWords
#global Wiki_words
#global News_words
#global Google_words
#global AVGRATE
#global Seeds
#global StockTerm
#global start
#global end
#global Numofwords
#global SuccessFinalTerms
Wiki_words = []
News_words = []
Google_words = []
rWords = []
AVGRATE = 0
SuccessFinalTerms = []
Terms = []
NegTerms = []
Percentage_passed0 = 0
Percentage_passed1 = 0
Percentage_passed2 = 0

try:
	with open(str(StockTerm) + "Data Save.txt", "r", encoding="utf8") as f:
		f = [line.strip() for line in f]

		pass
		try:
			Seeds = literal_eval(f[4])
		except Exception as e:
			print(e)
		pass
		try:
			StockTerm = f[7]
		except Exception as e:
			print(e)
		pass
		try:
			start = f[10]
		except Exception as e:
			print(e)
		pass
		try:
			end = f[13]
		except Exception as e:
			print(e)
		pass
		try:
			AVGRATE = f[16]
		except Exception as e:
			print(e)
		pass
		try:
			PosTerms1 = literal_eval(f[30])
			PosTerms2 = literal_eval(f[32])
			PosTerms3 = literal_eval(f[34])
			PosTerms4 = literal_eval(f[36])
			NegTerms1 = literal_eval(f[38])
			NegTerms2 = literal_eval(f[40])
			NegTerms3 = literal_eval(f[42])
			NegTerms4 = literal_eval(f[44])
			Successful_Terms = PosTerms1 + NegTerms1 + PosTerms2 + NegTerms2 + PosTerms3 + NegTerms3 + PosTerms4 + NegTerms4
		except Exception as e:
			print(e)
		pass

		try:
			Numofwords = int(f[27])
		except Exception as e:
			print(e)
		pass
except Exception as e:
	print("Data Save Is Not Working")
	print(e)
	pass



ExtraSeeds = []
try:
	with open(str(StockTerm) + "ExtraSeeds.txt", "r", encoding="utf8") as f:
		for line in f:
			ExtraSeeds.append(str(line.strip()))
except Exception as e:
	print(e)
	pass

try:
	with open(str(StockTerm) + "rWords.txt", "r", encoding="utf8") as f:
		rWords = literal_eval(f.read())
except Exception as e:
	print(e)
	pass

try:
	with open(str(StockTerm) + "Wiki.txt", "r", encoding="utf8") as f:
		Wiki_words = literal_eval(f.read())
except Exception as e:
	print(e)
	pass

try:
	with open(str(StockTerm) + "Google.txt", "r", encoding="utf8") as f:
		Google_words = literal_eval(f.read())
except Exception as e:
	print(e)
	pass

try:
	with open(str(StockTerm) + "News.txt", "r", encoding="utf8") as f:
		News_words = literal_eval(f.read())
except Exception as e:
	print(e)
	pass

try:
	entryText1.set( Seeds[0] )
	entryText2.set( Seeds[1] )
	entryText3.set( Seeds[2] )
	entryText4.set( Seeds[3] )
	entryText5.set( Seeds[4] )
	entryText6.set( Seeds[5] )
	entryText7.set( Seeds[6] )
	entryText8.set( Seeds[7] )
	entryText9.set( Seeds[8] )
except Exception as e:
	#print(e)
	pass

try:
	entryText10.set( StockTerm )
except Exception as e:
	#print(e)
	pass


try:
	entryText13.set( str(Numofwords) )
except Exception as e:
	#print(e)
	pass

try:
	entryText14.set( start )
	start = start.replace('-', '')
	start1 = start[0:4]
	start2 = str(start[4:5].replace('0', '')) + str(start[5:6])
	start3 = str(start[6:7].replace('0', '')) + str(start[7:8])
	start = datetime.date(int(start1), int(start2), int(start3))
except Exception as e:
	#print(e)
	pass

try:
	entryText15.set( end )
	end = end.replace('-', '')
	end1 = end[0:4]
	end2 = str(end[4:5].replace('0', '')) + str(end[5:6])
	end3 = str(end[6:7].replace('0', '')) + str(end[7:8])
	end = datetime.date(int(end1), int(end2), int(end3))
except Exception as e:
	#print(e)
	pass

try:
	Stock = pd.read_csv(str(StockTerm) + 'Stock.csv')
except Exception as e:
	print(e)
	pass

Fails = []

try:
	with open(str(StockTerm) + "Fails.txt", "r") as q:
		for line in q:
			Fails.append(str(line.strip()))

	with open("100commonwords.txt", "r") as q:
		for line in q:
			Fails.append(str(line.strip()))
except:
	pass

Fails = list(set(Fails))

path = r'C:\Users\Grego\Downloads\F' + str(StockTerm)
path2 = r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "2"
path3 = r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "3"

##### Processing Functions #####
class TS:
	def __init__(self, homepath, path, profile_path, Headless):
		os.chdir(homepath)

		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=Headless)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", str(path) )
		profile.set_preference("browser.download.downloadDir", str(path))
		profile.set_preference("browser.download."+ str(path).split("\\")[-1], path)
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		profile.update_preferences()

		driver = webdriver.Firefox(firefox_profile=profile, options=options, capabilities=cap, executable_path=r"C:\python\geckodriver-v0.23.0-win64\geckodriver.exe")
		driver.set_page_load_timeout(30)
		self.home = homepath
		self.profile_path = profile_path
		self.profile = profile
		self.driver = driver
		self.path = path

	def Start_Tor(self):

		profile_path = self.profile_path
		path = self.path
		self.p = subprocess.Popen(
		['firefox.exe'], stdin=subprocess.PIPE)
		os.chdir(self.home)
		exceptions = 0

		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=Headless)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", str(path) )
		profile.set_preference("browser.download.downloadDir", str(path))
		profile.set_preference("browser.download."+ str(path).split("\\")[-1], path)
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.socks", "127.0.0.1")
		profile.set_preference("network.proxy.socks_port", 9150)
		profile.set_preference("network.proxy.socks_version", 5)
		profile.update_preferences()
		self.driver = webdriver.Firefox(firefox_profile=profile, options=options, capabilities=cap, executable_path=r"C:\python\geckodriver-v0.23.0-win64\geckodriver.exe")
		self.driver.set_page_load_timeout(30)
		self.profile = profile
		

		try:
			self.driver.get("https://www.whatsmyip.org/")
			self.driver.get("https://www.youtube.com/")
			self.driver.get('https://www.google.co.uk/')
			self.driver.get('https://www.google.co.uk/search?q=Google+Trends')
			self.driver.get('https://trends.google.com/trends/?geo=US')
			time.sleep(5)
		except:
			pass

		try:
			self.driver.get('https://trends.google.com/trends/?geo=US')
		except Exception as e:
			print("There was a problem restarting:")
			print(e)
			pass

	def Exit_Tor(self):

		profile_path = self.profile_path
		self.driver.quit()
		path = self.path
		try:
			self.p.kill()
		except:
			pass
		os.chdir(self.home)

		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=Headless)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", str(path))
		profile.set_preference("browser.download.downloadDir", str(path))
		profile.set_preference("browser.download." + str(path).split("\\")[-1], str(path))
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		self.profile = profile
		self.driver = webdriver.Firefox(firefox_profile=profile, options=options, capabilities=cap, executable_path=r"C:\python\geckodriver-v0.23.0-win64\geckodriver.exe")
		self.driver.set_page_load_timeout(30)
		try:
			self.driver.get('https://www.google.co.uk/')
			self.driver.get('https://www.google.co.uk/search?q=Google+Trends')
			self.driver.get('https://trends.google.com/trends/?geo=US')
			time.sleep(5)
		except:
			exceptions = 10
			pass

		try:
			self.driver.get('https://trends.google.com/trends/?geo=US')
		except Exception as e:
			print("There was a problem restarting:")
			print(e)
			pass

	def FileCheck(self):
		Failed2 = []
		os.chdir(self.path)
		z = os.listdir()
		for o in z:
			if "Time" not in str(o):
				try:
					df = pd.read_csv(o)
					df.reset_index(inplace = True)
					term = df.iloc[0,1]
					term.replace(": (Worldwide)", "")
					term = re.sub("[\(\[].*?[\)\]]", "", term)
					Failed2.append(term)
					os.remove(o)
				except:
					pass

		return Failed2


	def Refine(self):
		os.chdir(self.path)
		z = os.listdir()
		for o in z:
			try:
				df = pd.read_csv(o)
				df.reset_index(inplace = True)
				term = re.sub("[\(\[].*?[\)\]]", "", term)
				term = df.iloc[0,1]
				lastdate = df.iloc[-1,0]
				lastdate = lastdate.replace('-', '')
				lastdate1 = lastdate[0:4]
				lastdate2 = str(lastdate[4:5].replace('0', '')) + str(lastdate[5:6])
				lastdate3 = str(lastdate[6:7].replace('0', '')) + str(lastdate[7:8])
				lastdate = datetime.date(int(lastdate1), int(lastdate2), int(lastdate3))
				days25 = today - datetime.timedelta(days = 90)
				if lastdate < days25:
					os.remove(o)
				else:
					pass
			except:
				pass

	def Scrape(self, Terms, Reruns, Start = '', End = ''):
		
		print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms")
		ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
		print("To Download this much data estimated time of completion is " + str(ETC) + "\n")

		if '-' in Start and 'days' in Start:
			Start = Start.replace('-', '').replace('days', '')
			Start = (date.today() - datetime.timedelta(int(Start)))
		elif Start == '':
			Start = (date.today() - datetime.timedelta(269))
		else:
			Start = Start.replace('-', '')
			Start1 = Start[0:4]
			Start2 = str(Start[4:5].replace('0', '')) + str(Start[5:6])
			Start3 = str(Start[6:7].replace('0', '')) + str(Start[7:8])
			Start = datetime.date(int(Start1), int(Start2), int(Start3))


		if '-' in End and 'days' in End:
			End = End.replace('-', '').replace('days', '')
			End = (date.today() - datetime.timedelta(int(End)))
		elif End == '':
			End = date.today()
		else:
			End = End.replace('-', '')
			End1 = End[0:4]
			End2 = str(End[4:5].replace('0', '')) + str(End[5:6])
			End3 = str(End[6:7].replace('0', '')) + str(End[7:8])
			End = datetime.date(int(End1), int(End2), int(End3))

		exceptions = 0
		Successes = 0
		one = 0
		Pauses = 0
		Tor = False
		totalseconds = (len(Terms) * 10.5)
		Failed = []

		for one, y in enumerate(Terms):

			if type(y) is tuple:
				y = ' '.join(y)

			print("\n")
			print(str(y) + ": " + str(one) + " out of " + str(len(Terms)))
			
			print("################################\n__Downloading the Trends Data of: " + str(y)+ "\n################################")
			
			q = y.replace(",", "")
			q = q.replace("-", " ")
			z = q.replace(" ", "+")

			cycle = time.time()
			urls = []
			time.sleep(1)
			while len(urls) < 9 and (time.time() - cycle) < 30:
				try:
					self.driver.get('https://trends.google.com/trends/?geo=US')
					time.sleep(1)
					print("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(Start, End, z))
					self.driver.get("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(Start, End, z))
					time.sleep(3)
					urls = ui.WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
					print("Page Loaded...")
					
					
				except Exception as e:
					if str(e) == 'Message: Timeout loading page after 30000ms':
						time.sleep(100)
					print("There was a problem loading the page:\n" + str(e))
					Failed.append(y)
					exceptions += 1

			try:
				if urls[9].get_attribute("class") == "widget-actions-item export":
					print("Found it!")
					urls[9].click()
					Successes += 1
			except Exception as e:
				print("There was a problem pressing the button:\n" + str(e))
				Failed.append(y)
				exceptions += 1

			try:
				Terms.remove(y)
			except:
				pass
"""
Optional:
"""
			if exceptions >= 10:
				Successes = 0
				Pauses += 1
				Tor = True
				os.chdir(self.home)
				termsandf = (list(set(Terms + Failed)))
				with open("Download.txt", "w", encoding="utf-8") as f:
					f.write(str(termsandf))
					print(str(termsandf))
				print("Saved")
				print("pausing")
				time.sleep(300)
				Start_Tor()
			

			if Successes > 100 and Tor == True:
				Successes = 0
				exceptions = 0
				Exit_Tor()
				Tor = False
				termsandf = (list(set(Terms + Failed)))
				with open("Download.txt", "w", encoding="utf-8") as f:
					f.write(str(termsandf))
					print(str(termsandf))

"""
Neccessary:
"""

		if Reruns > 1:
			Failed = Failed + self.FileCheck()
			self.Scrape(Failed, Reruns-1)
		else:
			print("\nDownload Complete")
			self.driver.quit()
			self.Refine()
			termsandf = (list(set(Terms + Failed)))
			with open("Download.txt", "w", encoding="utf-8") as f:
				f.write(str(termsandf))
			print("Download Has Ended. These are the terms that were not downloaded:\n" + str(termsandf))

			

class Data_Mining:
	def __init__(self):
		global today
		today = date.today()
		global Seeds
		global Numofwords
		global start
		global end
		global StockTerm

		Seeds = [str(entry_field1.get()), str(entry_field2.get()), str(entry_field3.get()), str(entry_field4.get()), str(entry_field5.get()), str(entry_field6.get()), str(entry_field7.get()), str(entry_field8.get()), str(entry_field9.get()), '']
		Seeds = list(set(Seeds))
		try:
			Seeds.remove("Insert Term")
		except:
			pass

		try:
			Seeds.remove('')
		except:
			pass
		Numofwords = str(entry_field13.get())

		start = str(entry_field14.get())
		start = start.replace("Insert Starting Date", '')
		end = str(entry_field15.get())
		end = end.replace("Insert Ending Date", '')

		StockTerm = str(entry_field10.get())
		if str(StockTerm) == 'Insert Stock Symbol':
			messagebox.showinfo("Stock Symbol Needed", "Please Insert Which Stock You Would Like To Work With!!!")
			return

		if '-' in start and 'days' in start:
			start = start.replace('-', '').replace('days', '')
			start = (today - datetime.timedelta(int(start)))
		elif start == '':
			start = (today - datetime.timedelta(269))
		else:
			start = start.replace('-', '')
			start1 = start[0:4]
			start2 = str(start[4:5].replace('0', '')) + str(start[5:6])
			start3 = str(start[6:7].replace('0', '')) + str(start[7:8])
			start = datetime.date(int(start1), int(start2), int(start3))


		if '-' in end and 'days' in end:
			end = end.replace('-', '').replace('days', '')
			end = (today - datetime.timedelta(int(end)))
		elif end == '':
			end = today
		else:
			end = end.replace('-', '')
			end1 = end[0:4]
			end2 = str(end[4:5].replace('0', '')) + str(end[5:6])
			end3 = str(end[6:7].replace('0', '')) + str(end[7:8])
			end = datetime.date(int(end1), int(end2), int(end3))

		c = datetime.datetime.now()	
		print("\n")
		print("##############################")
		print("Today is " + str(today))
		print(c.strftime("The Time now is %H:%M:%S"))
		print("First Date Set to: " + str(start))
		print("Last Date Set to: " + str(end))
		print("The Stock is: " + str(StockTerm))
		print("Amount of related Words to be researched further is Set to: " + str(Numofwords))
		print("##############################")
		print("\n")


	def Related_words(self):
		global Completed
		global rWords
		rWords = []

		driver = webdriver.Firefox()

		for y in Seeds:
			
			print("\n")
			print("################################\n__Finding the related words of: " + str(y)+ "\n################################")
			z = y.replace(" ", "_")

			try:
				driver.get("https://relatedwords.org/relatedto/" + str(z))
			except Exception as e:
				messagebox.showinfo("Wifi", "Try Connecting to Wifi!")

			time.sleep(0.5)
			urls = ui.WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
			print("Related words are:\n")
			words = []
			for url in urls:
				if url.get_attribute("class") == "item":
					qu = str(url.get_attribute("text"))
					print(qu)
					words.append(qu)					
			words.append('')
			words = list(set(words))
			words.remove('')
			rWords.append(words)
		driver.quit()
		Completed = True

		self.__exit__()


	def Wiki(self, Related):
		global Completed
		global Wiki_words

		print("Downloading Wikipedia Data for " + str(len(Related)) + " Words.")
		
		for one, y in enumerate(Related):
			try:
				y = y.replace(",", "")
				z = y.replace(" ", "_")
				print("\n#############\nNow scraping the 100 most common words/phrases of wikipedia on: " + str(y) + "\n#############")

				url = ("https://en.wikipedia.org/wiki/" + str(z))
				
				article = Article(url)

				article.download()

				article.html
				'<!DOCTYPE HTML><html itemscope itemtype="http://...'

				article.parse()
				
				text = str(article.text)
				New = []
				list1 = text.split()
				list2 = list(zip(list1, list1[1:]))
				for word in list1:
					if word.lower() not in Fails:
						New.append(word)

				for word in list2:
					if word[0].lower() not in Fails or word[1].lower() not in Fails:
						' '.join(word)
						New.append(word)

				count = Counter(New)
				
				mc = count.most_common(100)
				
				print("Done!")

				for word in mc:
					Wiki_words.append(word[0])

			except Exception as e:
				print("\nThis one isn't available, Here is the Error:\n")
				print(e)
				pass


		Wiki_words = list(set(Wiki_words))

		print(str(Wiki_words))

		Completed = True

		self.__exit__()
		
		
	def News(self, Related):
		global Completed
		global News_words

		print("Downloading News_Headlines Data for " + str(len(Related)) + " Words.")

		for one, y in enumerate(Related):
			try:
				z = y.replace(" ", "+")
				print("\n#############\nNow scraping the 20 most common words of Google News on: " + str(y) + "\n#############")
				
				url = ('https://www.google.co.uk/search?q=' + str(z) + '&source=lnms&tbm=nws')
				
				article = Article(url)

				article.download()

				article.html
				'<!DOCTYPE HTML><html itemscope itemtype="http://...'

				article.parse()
				
				text = str(article.text)
				New = []
				list1 = text.split()
				list2 = list(zip(list1, list1[1:]))
				for word in list1:
					if word.lower() not in Fails:
						New.append(word)

				for word in list2:
					if word[0].lower() not in Fails or word[1].lower() not in Fails:
						' '.join(word)
						New.append(word)


				count = Counter(New)
				
				mc = count.most_common(20)
				
				print("Done!")

				for word in mc:
					Wiki_words.append(word[0])

			except Exception as e:
				print("\nThis one isn't available, Here is the Error:\n")
				print(e)
				pass
			

		News_words = list(set(News_words))

		print(str(News_words))

		Completed = True

		self.__exit__()


	def Google(self, Related):
		global Completed
		global Google_words

		print("Downloading Google Data for " + str(len(Related)) + " Words.")

		for y in Related:
			try:
				z = y.replace(" ", "_")
				print("\n#############\nNow scraping the 20 most common words of Google on: " + str(y) + "\n#############")
				
				
				url = ("https://www.google.co.uk/search?q=" + str(z))
				
				article = Article(url)

				article.download()

				article.html
				'<!DOCTYPE HTML><html itemscope itemtype="http://...'

				article.parse()
				
				text = str(article.text)
				New = []
				list1 = text.split()
				list2 = list(zip(list1, list1[1:]))
				for word in list1:
					if word.lower() not in Fails:
						New.append(word)

				for word in list2:
					if word[0].lower() not in Fails or word[1].lower() not in Fails:
						' '.join(word)
						New.append(word)


				count = Counter(New)
				
				mc = count.most_common(20)
				
				print("Done!")

				for word in mc:
					Wiki_words.append(word[0])

			except Exception as e:
				print("\nThis one isn't available, Here is the Error:\n")
				print(e)
				pass

		Google_words = list(set(Google_words))

		print(str(Google_words))

		Completed = True

		self.__exit__()


	# def Download(self, TERMS):
	# 	#global Completed
	# 	Paused = False

	# 	progress = Progressbar(window, length=500, mode='determinate')
	# 	progress.grid(column = 1, row = 30, columnspan = 3 )
	# 	label = tk.StringVar()
	# 	label.set("Initialising...")
	# 	title0 = tk.Label(textvariable = label , font = ("Calibri", 20))
	# 	title0.grid(column = 1, row = 29, columnspan = 3, padx=5, pady=5)
	# 	window.update()

	# 	os.chdir(home)
		
	# 	profile = webdriver.FirefoxProfile(profile_path)
	# 	profile.set_preference("browser.download.manager.showWhenStarting",False)
	# 	profile.set_preference("browser.download.folderList",2)
	# 	profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm) )
	# 	profile.set_preference("browser.download.downloadDir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
	# 	profile.set_preference(("browser.download.F" + str(StockTerm)), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	# 	profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
	# 	profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
	# 	profile.update_preferences()

	# 	driver = webdriver.Firefox(firefox_profile=profile)
	# 	driver.set_page_load_timeout(30)

	# 	#try:
	# 	#	driver.get('https://www.google.co.uk/')
	# 	#	#driver.get('https://www.google.co.uk/search?q=Google+Trends')
	# 	#	driver.get('https://trends.google.com/trends/?geo=US')
	# 	#except Exception as e:
	# 	#	messagebox.showinfo("Wifi", "Try Connecting to Wifi!")
	# 	#	title0.grid_forget()
	# 	#	progress.grid_forget()
	# 	#	window.update()
	# 	#	print("Wifi Connection Error")
	# 	#	return

	# 	Terms = list(set(TERMS))

	# 	os.chdir(path)
	# 	z = os.listdir()
	# 	for o in z:
	# 		try:
	# 			df = pd.read_csv(o)
	# 			df.reset_index(inplace = True)
	# 			term = re.sub("[\(\[].*?[\)\]]", "", term)
	# 			term = df.iloc[0,1]
	# 			lastdate = df.iloc[-1,0]
	# 			lastdate = lastdate.replace('-', '')
	# 			lastdate1 = lastdate[0:4]
	# 			lastdate2 = str(lastdate[4:5].replace('0', '')) + str(lastdate[5:6])
	# 			lastdate3 = str(lastdate[6:7].replace('0', '')) + str(lastdate[7:8])
	# 			lastdate = datetime.date(int(lastdate1), int(lastdate2), int(lastdate3))
	# 			days25 = today - datetime.timedelta(days = 90)
	# 			if lastdate < days25:
	# 				os.remove(o)
	# 			else:
	# 				Terms.remove(term)
	# 		except:
	# 			pass

		
	# 	#for x in Terms:
	# 		#if x in Fails:
	# 			#print(str(x) + " Removed")
	# 			#Terms.remove(x)

	# 	os.chdir(home)
		
	# 	print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms Found based on seeds " + str(Seeds) + "\n")

	# 	exceptions = 0
	# 	Failed = []
	# 	one = 0
	# 	Pauses = 0

	# 	totalseconds = (len(Terms) * 10.5)

	# 	ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
	# 	print("To Download this much data estimated time of completion is " + str(ETC) + "\n")

	# 	time.sleep(10)
	# 	exceptions = 0
	# 	Successes = 0

	# 	Start_Time = time.time()
	# 	for ii in range(2):
			
	# 		terms = (list(set(Terms + Failed)))
	# 		Failed = []
	# 		Terms = []
	# 		lenterms = len(terms)
	# 		termscopy = terms.copy()

	# 		for one, y in enumerate(termscopy):

	# 			if type(y) is tuple:
	# 				y = ' '.join(y)

	# 			print("\n")
	# 			print(str(y) + ": " + str(one) + " out of " + str(lenterms))
				
	# 			print("################################\n__Downloading the Trends Data of: " + str(y)+ "\n################################")
				
	# 			q = y.replace(",", "")
	# 			q = q.replace("-", " ")
	# 			z = q.replace(" ", "+")

	# 			cycle = time.time()
	# 			urls = []
	# 			time.sleep(1)
	# 			while len(urls) < 9 and (time.time() - cycle) < 30:
	# 				try:
	# 					driver.get('https://trends.google.com/trends/?geo=US')
	# 					time.sleep(1)
	# 					print("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
	# 					driver.get("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
	# 					time.sleep(3)
	# 					urls = ui.WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
	# 					print("Page Loaded...")
						
						
	# 				except Exception as e:
	# 					if str(e) == 'Message: Timeout loading page after 30000ms':
	# 						time.sleep(100)
	# 					print("There was a problem loading the page:\n" + str(e))
	# 					Failed.append(y)
	# 					exceptions += 1

	# 			try:
	# 				if urls[9].get_attribute("class") == "widget-actions-item export":
	# 					print("Found it!")
	# 					urls[9].click()
	# 					Successes += 1
	# 			except Exception as e:
	# 				print("There was a problem pressing the button:\n" + str(e))
	# 				Failed.append(y)
	# 				exceptions += 1

	# 			try:
	# 				terms.remove(y)
	# 			except:
	# 				pass

	# 			if exceptions >= 10:
	# 				Successes = 0
	# 				Pauses += 1
	# 				Paused = True
	# 				#messagebox.showinfo("Download Error!", "Multiple failed webpages, Swapping IP via VPN is suggested; or check your wifi...")
	# 				os.chdir(home)
	# 				termsandf = (list(set(terms + Failed)))
	# 				with open("Download.txt", "w", encoding="utf-8") as f:
	# 					f.write(str(termsandf))
	# 					print(str(termsandf))
	# 				print("Saved")
	# 				print("pausing")
	# 				driver.quit()
	# 				os.chdir(TOR)
	# 				try:
	# 					p.kill()
	# 				except:
	# 					pass
	# 				time.sleep(300)
	# 				p = subprocess.Popen(
	# 				['firefox.exe'], stdin=subprocess.PIPE)
	# 				os.chdir(home)
	# 				exceptions = 0
		
	# 				profile = webdriver.FirefoxProfile(profile_path)
	# 				profile.set_preference("browser.download.manager.showWhenStarting",False)
	# 				profile.set_preference("browser.download.folderList",2)
	# 				profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
	# 				profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	# 				profile.set_preference("browser.download.F" + str(StockTerm), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	# 				profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
	# 				profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
	# 				profile.set_preference("network.proxy.type", 1)
	# 				profile.set_preference("network.proxy.socks", "127.0.0.1")
	# 				profile.set_preference("network.proxy.socks_port", 9150)
	# 				profile.set_preference("network.proxy.socks_version", 5)
	# 				profile.update_preferences()

	# 				driver = webdriver.Firefox(firefox_profile=profile)
	# 				driver.set_page_load_timeout(30) 

	# 				try:
	# 					driver.get("https://www.whatsmyip.org/")
	# 					driver.get("https://www.youtube.com/")
	# 					driver.get('https://www.google.co.uk/')
	# 					driver.get('https://www.google.co.uk/search?q=Google+Trends')
	# 					driver.get('https://trends.google.com/trends/?geo=US')
	# 					time.sleep(5)
	# 				except:
	# 					pass

	# 				try:
	# 					driver.get('https://trends.google.com/trends/?geo=US')
	# 				except Exception as e:
	# 					print("There was a problem restarting:")
	# 					print(e)
	# 					pass
					
	# 			try:
	# 				Secondssofar = (time.time() - Start_Time)
	# 				print(str(Pauses) + " Pauses")
	# 				Percentage_passed = one/lenterms
	# 				print(str(Percentage_passed*100) + "%")
	# 				Percentage_left = 1 - Percentage_passed
	# 				Seconds_left = datetime.timedelta(seconds =(Secondssofar/Percentage_passed)*Percentage_left)
	# 				x = ("ETC = %.2d hours %.2d minutes %.2d seconds" % (Seconds_left.seconds//3600,(Seconds_left.seconds//60)%60, Seconds_left.seconds%60)+ "  (" + str(ii + 1) + " out of 2.)")
	# 				print(x)
	# 				label.set(x)
	# 				progress['value'] = Percentage_passed*100
	# 				window.update()
	# 			except:
	# 				pass

	# 			if Successes > 100 and Paused == True:
	# 				Successes = 0
	# 				exceptions = 0
	# 				driver.quit()
	# 				try:
	# 					p.kill()
	# 				except:
	# 					pass
	# 				os.chdir(home)
	# 				profile = webdriver.FirefoxProfile(profile_path)
	# 				profile.set_preference("browser.download.manager.showWhenStarting",False)
	# 				profile.set_preference("browser.download.folderList",2)
	# 				profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
	# 				profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	# 				profile.set_preference("browser.download.F" + str(StockTerm), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	# 				profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
	# 				profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
	# 				driver = webdriver.Firefox(firefox_profile=profile)
	# 				driver.set_page_load_timeout(30)
	# 				try:
	# 					driver.get('https://www.google.co.uk/')
	# 					driver.get('https://www.google.co.uk/search?q=Google+Trends')
	# 					driver.get('https://trends.google.com/trends/?geo=US')
	# 					time.sleep(5)
	# 				except:
	# 					exceptions = 10
	# 					pass

	# 				try:
	# 					driver.get('https://trends.google.com/trends/?geo=US')
	# 				except Exception as e:
	# 					print("There was a problem restarting:")
	# 					print(e)
	# 					pass


	# 		os.chdir(path)

	# 		z = os.listdir()
			
	# 		for o in z:
	# 			if "Time" not in str(o):
	# 				try:
	# 					df = pd.read_csv(o)
	# 					df.reset_index(inplace = True)
	# 					term = df.iloc[0,1]
	# 					term.replace(": (Worldwide)", "")
	# 					term = re.sub("[\(\[].*?[\)\]]", "", term)
	# 					Failed.append(term)
	# 					os.remove(o)
	# 				except:
	# 					pass
					
					


	# 	title0.grid_forget()
	# 	progress.grid_forget()
	# 	window.update()

	# 	print("\nDownload Complete")
	# 	driver.quit()
		
	# 	os.chdir(home)

	# 	Completed = True

	# 	self.__exit__()




	def stocks(self):
		global Stock

		if StockTerm == '':
			print("Please enter a term")
			return

			
		Start = today - datetime.timedelta(days = 500)
		End = datetime.datetime.now()

		os.chdir(save)
		#Can use: morningstar (Close, Open), robinhood (close_price, open_price) *cannot use with dates, limited to 1 year, google (Close, Open),  quandl (Close, Open), stooq (Close, Open, Date)

		try:
			Stock = web.DataReader(StockTerm, "stooq", Start, End)
			Stock.reset_index(inplace = True)
			Stock.rename(columns={'Close':'close'}, inplace=True)
			Stock.rename(columns={'Open':'open'}, inplace=True)
			Stock.rename(columns={'Date':'date'}, inplace=True)
			
		except Exception as e:
			print("Try connecting to wifi!")
			time.sleep(1)
			print("error is:\n" + str(e))
			time.sleep(20)

		Stock.to_csv(str(StockTerm) + 'Stock.csv')
		print(Stock)

		self.__exit__()
	
	def Processing(self):
		Removals = []

		#This needs proper object oriented programming
		global Total_Confidence
		global progress
		global label
		global SuccessFinalTerms
		global NegTerms1
		global PosTerms1
		global NegTerms2
		global PosTerms2
		global NegTerms3
		global PosTerms3

		Percentage_passed0 = 0

		SuccessFinalTerms = []
		Graph = []

		os.chdir(path)

		progress = Progressbar(window, length=500, mode='determinate')
		progress.grid(column = 1, row = 30, columnspan = 3 )
		label = tk.StringVar()
		label.set("Initialising...")
		title0 = tk.Label(textvariable = label , font = ("Calibri", 20))
		title0.grid(column = 1, row = 29, columnspan = 3, padx=5, pady=5)
		window.update()
		
		
		z = os.listdir()
		length = len(z)
		Successes = []

		z = os.listdir()
		
		l = len(z)*2

		MainDF = pd.DataFrame({"Stock_Change": [], "Dates" : [], "Dates1" : [], "Dates2" : [], "Dates3" : [], "Dates4" : [], "Enddata": []})
		print(MainDF)



		def Check(term1, list1, NumDays):
			if term1 in list1:
				correctData = []
				StockDif = []
				for index, row in Stock.iterrows():
					ooo = row['date']
					datea = ooo.replace('-', '')
					date1 = datea[0:4]
					date2 = str(datea[4:5].replace('0', '')) + str(datea[5:6])
					date3 = str(datea[6:7].replace('0', '')) + str(datea[7:8])
					dateb = datetime.date(int(date1), int(date2), int(date3))
					dateg = dateb - datetime.timedelta(days = NumDays)
					
					try:
						correctData.append(df.loc[df['index'] == str(dateg)]['Difference'].values[0])
						################################### Difference Switch ##################################
						#StockDif.append(row['close'] - row['open'])
						StockDif.append(row['close'])
					except Exception as e:
						pass
				CorrelationDF = pd.DataFrame({'Stock_Change': StockDif, 'Trends_Difference' : correctData})
				Correl = abs(int(CorrelationDF['Stock_Change'].astype('float64').corr(CorrelationDF['Trends_Difference'].astype('float64')))*100)
				if Correl < 8:
					print(str(term1) + ' removed')
					list1.remove(term1)
					Removals.append(term1)

		####################################### 5 for raw data. 9 for difference data #########################################
		switch = 5
		def BestSettingCheck(setting, list1, DataFrame, Correl, MainDF):
			if setting > (((1-Correl)**2)/switch)*100:
				list1.append(term)
				MainDF = DataFrame
				print(str(term) + " added a correlation of " + str(setting) + "%")
				Correl = MainDF["Enddata"].astype('float64').corr(MainDF["Stock_Change"].astype('float64'), method = Correlation_technique)
				print(Correl)
			elif setting < -(((Correl-1)**2)/2)*100:
				Fails.append(term)

			return MainDF, Correl


		for index, row in Stock.iterrows():
			ooo = str(row['date'])
			datea = ooo.replace('-', '')
			date1 = datea[0:4]
			date2 = str(datea[4:5].replace('0', '')) + str(datea[5:6])
			date3 = str(datea[6:7].replace('0', '')) + str(datea[7:8])
			dateb = datetime.date(int(date1), int(date2), int(date3))
			datec = dateb - datetime.timedelta(days = 1)
			dated = dateb - datetime.timedelta(days = 2)
			datee = dateb - datetime.timedelta(days = 3)
			datef = dateb - datetime.timedelta(days = 4)
			################################### Difference Switch
			Change = row['close'] - row['open']
			Close = row['close']
			MainDF.loc[index] = [Close, dateb, datec, dated, datee, datef, 0]

		MainDF.sort_values(by = 'Dates', inplace = True)

		Correl = 0

		PosTerms1 = []
		NegTerms1 = []
		PosTerms2 = []
		NegTerms2 = []
		PosTerms3 = []
		NegTerms3 = []
		PosTerms4 = []
		NegTerms4 = []
		posTerms1 = []
		negTerms1 = []
		posTerms2 = []
		negTerms2 = []
		posTerms3 = []
		negTerms3 = []
		posTerms4 = []
		negTerms4 = []

		MainDF.drop(MainDF.index[0], inplace = True)
		Start_Time = time.time()
		NumDataSets = 0
		AllDataFrames = pd.DataFrame({'Enddata'+str(NumDataSets): []})

		Terms = []
		z = os.listdir()
		y = list(z)
		for o in y:
			#print(o)
			try:
				df = pd.read_csv(o)
			except:
				#z.remove(o)
				continue
			df.reset_index(inplace = True)
			if df.shape[0] < 5:
				#Fails.append(term)
				#z.remove(o)
				continue
			if "Time" not in str(o):
				print(str(o) + " is invalid")
				#z.remove(o)
				continue
			term = df.iloc[0,1]
			term = term.replace(": (Worldwide)", "")
			term = re.sub("[\(\[].*?[\)\]]", "", term)
			if term in Fails:
				#z.remove(o)
				print(str(o) + "is a faliure")
				continue
			Terms.append(term)
		Terms = list(set(Terms))
		print(z)
		print('There are ' + str(len(Terms)) + ' Terms')

		for o in z:
			#print(o)
			#print(Correl)
			try:
				df = pd.read_csv(o)
			except:
				continue
			df.replace("NaN", 0, inplace = True)
			df.reset_index(inplace = True)
			term = df.iloc[0,1]
			term = term.replace(": (Worldwide)", "")
			term = re.sub("[\(\[].*?[\)\]]", "", term)
			df.drop(df.index[0], inplace = True)
			df.replace('<1', 0.5, inplace = True)
			if df.shape[0] < 5:
				#Fails.append(term)
				#os.remove(o)
				continue

			################################### Difference Switch ######################################

			df['Difference'] = df['Category: All categories']
			#df['Difference'] = [0] + [int(s) - int(t) for t, s in zip(list(df['Category: All categories']), list(df['Category: All categories'])[1:])]
			successful_Terms = posTerms1 + negTerms1 + posTerms2 + negTerms2 + posTerms3 + negTerms3 + posTerms4 + negTerms4
			if term in successful_Terms + Fails:
				continue

			CorrelationDF1 = MainDF.copy()
			CorrelationDF2 = MainDF.copy()
			CorrelationDF3 = MainDF.copy()
			CorrelationDF4 = MainDF.copy()
			CorrelationDF1Neg = MainDF.copy()
			CorrelationDF2Neg = MainDF.copy()
			CorrelationDF3Neg = MainDF.copy()
			CorrelationDF4Neg = MainDF.copy()

			itercopy = MainDF[1:].iterrows()

			for index2, row in itercopy:
				try:
					CorrelationDF1.at[index2, "Enddata"]=(row["Enddata"] + int(df.loc[df['index'] == str(row['Dates1'])]['Difference'].values[0]))
					CorrelationDF1.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF1.drop([index2], inplace = True)
						CorrelationDF1.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF2.at[index2, "Enddata"]=(row["Enddata"] + int(df.loc[df['index'] == str(row['Dates2'])]['Difference'].values[0]))
					CorrelationDF2.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF2.drop([index2], inplace = True)
						CorrelationDF2.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF3.at[index2, "Enddata"]=(row["Enddata"] + int(df.loc[df['index'] == str(row['Dates3'])]['Difference'].values[0]))
					CorrelationDF3.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF3.drop([index2], inplace = True)
						CorrelationDF3.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF4.at[index2, "Enddata"]=(row["Enddata"] + int(df.loc[df['index'] == str(row['Dates4'])]['Difference'].values[0]))
					CorrelationDF4.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF4.drop([index2], inplace = True)
						CorrelationDF4.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF1Neg.at[index2, "Enddata"]=(row["Enddata"] - int(df.loc[df['index'] == str(row['Dates1'])]['Difference'].values[0]))
					CorrelationDF1Neg.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF1Neg.drop([index2], inplace = True)
						CorrelationDF1Neg.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF2Neg.at[index2, "Enddata"]=(row["Enddata"] - int(df.loc[df['index'] == str(row['Dates2'])]['Difference'].values[0]))
					CorrelationDF2Neg.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF2Neg.drop([index2], inplace = True)
						CorrelationDF2Neg.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF3Neg.at[index2, "Enddata"]=(row["Enddata"] - int(df.loc[df['index'] == str(row['Dates3'])]['Difference'].values[0]))
					CorrelationDF3Neg.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF3Neg.drop([index2], inplace = True)
						CorrelationDF3Neg.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

				try:
					CorrelationDF4Neg.at[index2, "Enddata"]=(row["Enddata"] - int(df.loc[df['index'] == str(row['Dates4'])]['Difference'].values[0]))
					CorrelationDF4Neg.sort_values(by = 'Dates', inplace = True)
				except Exception as e:
					if str(e) == 'index 0 is out of bounds for axis 0 with size 0':
						CorrelationDF4Neg.drop([index2], inplace = True)
						CorrelationDF4Neg.sort_values(by = 'Dates', inplace = True)
					else:
						print(e)

			Correla = CorrelationDF1["Enddata"].astype('float64').corr(CorrelationDF1["Stock_Change"].astype('float64'), method = Correlation_technique)
			Correlb = CorrelationDF2["Enddata"].astype('float64').corr(CorrelationDF2["Stock_Change"].astype('float64'), method = Correlation_technique)
			Correlc = CorrelationDF3["Enddata"].astype('float64').corr(CorrelationDF3["Stock_Change"].astype('float64'), method = Correlation_technique)
			Correld = CorrelationDF4["Enddata"].astype('float64').corr(CorrelationDF4["Stock_Change"].astype('float64'), method = Correlation_technique)
			NCorrela = CorrelationDF1Neg["Enddata"].astype('float64').corr(CorrelationDF1Neg["Stock_Change"].astype('float64'), method = Correlation_technique)
			NCorrelb = CorrelationDF2Neg["Enddata"].astype('float64').corr(CorrelationDF2Neg["Stock_Change"].astype('float64'), method = Correlation_technique)
			NCorrelc = CorrelationDF3Neg["Enddata"].astype('float64').corr(CorrelationDF3Neg["Stock_Change"].astype('float64'), method = Correlation_technique)
			NCorreld = CorrelationDF4Neg["Enddata"].astype('float64').corr(CorrelationDF4Neg["Stock_Change"].astype('float64'), method = Correlation_technique)
			increasea = (Correla - Correl)*100
			increaseb = (Correlb - Correl)*100
			increasec = (Correlc - Correl)*100
			increased = (Correld - Correl)*100
			Nincreasea = (NCorrela - Correl)*100
			Nincreaseb = (NCorrelb - Correl)*100
			Nincreasec = (NCorrelc - Correl)*100
			Nincreased = (NCorreld - Correl)*100

			Increases = [increasea, increaseb, increasec, increased, Nincreasea, Nincreaseb, Nincreasec, Nincreased]
			#print(Increases)

			if max(Increases) == increasea:
				MainDF, Correl = BestSettingCheck(increasea, posTerms1, CorrelationDF1, Correl, MainDF)
			elif max(Increases) == increaseb:
				MainDF, Correl = BestSettingCheck(increaseb, posTerms2, CorrelationDF2, Correl, MainDF)
			elif max(Increases) == increasec:
				MainDF, Correl = BestSettingCheck(increasec, posTerms3, CorrelationDF3, Correl, MainDF)
			elif max(Increases) == increased:
				MainDF, Correl = BestSettingCheck(increased, posTerms4, CorrelationDF4, Correl, MainDF)
			elif max(Increases) == Nincreasea:
				MainDF, Correl = BestSettingCheck(Nincreasea, negTerms1, CorrelationDF1Neg, Correl, MainDF)
			elif max(Increases) == Nincreaseb:
				MainDF, Correl = BestSettingCheck(Nincreaseb, negTerms2, CorrelationDF2Neg, Correl, MainDF)
			elif max(Increases) == Nincreasec:
				MainDF, Correl = BestSettingCheck(Nincreasec, negTerms3, CorrelationDF3Neg, Correl, MainDF)
			elif max(Increases) == Nincreased:
				MainDF, Correl = BestSettingCheck(Nincreased, negTerms4, CorrelationDF4Neg, Correl, MainDF)

			if term in Seeds or term in ExtraSeeds:
				print(str(term) + ' when added had increases of %.5f, %.5f, %.5f, %.5f, and whe taken away had increases of %.5f, %.5f, %.5f, %.5f.' % (increasea, increaseb, increasec, increased, Nincreasea, Nincreaseb, Nincreasec, Nincreased))

			Secondssofar = (time.time() - Start_Time)
			Percentage_passed0 += 1/l
			Percentage_left = 1 - Percentage_passed0
			Seconds_left = datetime.timedelta(seconds =(Secondssofar/Percentage_passed0)*Percentage_left)
			x = ("ETC = %.2d hours %.2d minutes %.2d seconds" % (Seconds_left.seconds//3600,(Seconds_left.seconds//60)%60, Seconds_left.seconds%60) + '(Part A)')
			label.set(x)
			#print(Percentage_passed)
			progress['value'] = Percentage_passed0*90
			window.update()

			if str(Correl) == 'None':
				Correl = 0

			if Correl > 0.92:
				print(posTerms1)
				print(negTerms1)
				print(posTerms2)
				print(negTerms2)
				print(posTerms3)
				print(negTerms3)
				print(posTerms4)
				print(negTerms4)
				successful_Terms = posTerms1 + negTerms1 + posTerms2 + negTerms2 + posTerms3 + negTerms3 + posTerms4 + negTerms4

				# os.chdir(path2)

				# Start_Time = time.time()
				
				# self.Download90Days(successful_Terms, Percentage_passed0)

				# os.chdir(path2)
				# DFcheck = DataFrame({})
				# z = os.listdir()
				# for o in z:
				# 	try:
				# 		df = pd.read_csv(o)
				# 		#print(df)
				# 		df.reset_index(inplace = True)
				# 		term = df.iloc[0,1]
				# 		term = term.replace(": (Worldwide)", "")
				# 		term = re.sub("[\(\[].*?[\)\]]", "", term)
				# 		df.drop(df.index[0], inplace = True)
				# 		df.replace('<1', 0.5, inplace = True)
				# 		###################################### Difference Switch #####################################
				# 		#df['Difference'] = [0] + [int(s) - int(t) for t, s in zip(list(df['Category: All categories']), list(df['Category: All categories'])[1:])]
				# 		df['Difference'] = list(df['Category: All categories'])
				# 	except:
				# 		print("there was a problem with one of the files!!!")
				# 		continue

				# 	####################################### Difference Switch at the top ############################
				# 	Check(term, posTerms1, 1)
				# 	Check(term, posTerms2, 2)
				# 	Check(term, posTerms3, 3)
				# 	Check(term, posTerms4, 4)
				# 	Check(term, negTerms1, 1)
				# 	Check(term, negTerms2, 2)
				# 	Check(term, negTerms3, 3)
				# 	Check(term, negTerms4, 4)

				os.chdir(DataSets)
				try:
					with open(str(StockTerm) + "Data Set" + str(NumDataSets) + " - (" + str(StockTerm) + ").txt", "w", encoding="utf-8") as f:
						f.write("""
##############################
    Data Set:               

Positive Terms 1 Day Before:
{}
Positive Terms 2 Day Before:
{}
Positive Terms 3 Day Before:
{}
Positive Terms 4 Day Before:
{}
Negative Terms 1 Day Before:
{}
Negative Terms 2 Day Before:
{}
Negative Terms 3 Day Before:
{}
Negative Terms 4 Day Before:
{}

############################## 

						""".format(posTerms1, posTerms2, posTerms3, posTerms4, negTerms1, negTerms2, negTerms3, negTerms4))
						print("Saved")
				except Exception as e:
					print(e)
					pass

				print("""
##############################
    Data Set:               

Positive Terms 1 Day Before:
{}
Positive Terms 2 Day Before:
{}
Positive Terms 3 Day Before:
{}
Positive Terms 4 Day Before:
{}
Negative Terms 1 Day Before:
{}
Negative Terms 2 Day Before:
{}
Negative Terms 3 Day Before:
{}
Negative Terms 4 Day Before:
{}

############################## 

						""".format(posTerms1, posTerms2, posTerms3, posTerms4, negTerms1, negTerms2, negTerms3, negTerms4))

				print(Correl)

				for x in posTerms1:
					PosTerms1.append(x)
				PosTerms1 = list(set(PosTerms1))
				for x in posTerms2:
					PosTerms2.append(x)
				PosTerms2 = list(set(posTerms2))
				for x in posTerms3:
					PosTerms3.append(x)
				PosTerms3 = list(set(PosTerms3))
				for x in posTerms4:
					PosTerms4.append(x)
				PosTerms4 = list(set(PosTerms4))
				for x in negTerms1:
					NegTerms1.append(x)
				NegTerms1 = list(set(NegTerms1))
				for x in negTerms2:
					NegTerms2.append(x)
				NegTerms2 = list(set(NegTerms2))
				for x in negTerms3:
					NegTerms3.append(x)
				NegTerms3 = list(set(NegTerms3))
				for x in negTerms4:
					NegTerms4.append(x)
				NegTerms4 = list(set(NegTerms4))

				self.__exit__()

				posTerms1 = []
				posTerms2 = []
				posTerms3 = []
				posTerms4 = []
				negTerms1 = []
				negTerms2 = []
				negTerms3 = []
				negTerms4 = []

				MainDF.to_csv(str(StockTerm) + 'MainDF' + str(NumDataSets) + '.csv')

				

				print(MainDF.to_string())
				print('\n')


				MainDF = pd.DataFrame({"Stock_Change": [], "Dates" : [], "Dates1" : [], "Dates2" : [], "Dates3" : [], "Dates4" : [], "Enddata": []})

				for index, row in Stock.iterrows():
					ooo = str(row['date'])
					datea = ooo.replace('-', '')
					date1 = datea[0:4]
					date2 = str(datea[4:5].replace('0', '')) + str(datea[5:6])
					date3 = str(datea[6:7].replace('0', '')) + str(datea[7:8])
					dateb = datetime.date(int(date1), int(date2), int(date3))
					datec = dateb - datetime.timedelta(days = 1)
					dated = dateb - datetime.timedelta(days = 2)
					datee = dateb - datetime.timedelta(days = 3)
					datef = dateb - datetime.timedelta(days = 4)
					################################### Difference Switch
					Change = row['close'] - row['open']
					Close = row['close']
					MainDF.loc[index] = [Close, dateb, datec, dated, datee, datef, 0]

				MainDF.sort_values(by = 'Dates', inplace = True)

				print(MainDF)
				print(Removals)

				Correl = 0
				NumDataSets += 1

				os.chdir(path)
				
		print(Removals)

		label.set("Done!")
		progress['value'] = 100
		window.update()

		os.chdir(save)

		print(PosTerms1)
		print(NegTerms1)
		print(PosTerms2)
		print(NegTerms2)
		print(PosTerms3)
		print(NegTerms3)
		print(PosTerms4)
		print(NegTerms4)
		Successful_Terms = PosTerms1 + NegTerms1 + PosTerms2 + NegTerms2 + PosTerms3 + NegTerms3 + PosTerms4 + NegTerms4
		print("The Successful Terms are: " + str(Successful_Terms))



		title0.grid_forget()
		progress.grid_forget()
		window.update()

		self.__exit__()

		plt.show()


	def Download90Days(self, TERMS, Percentage_passed0):
		global Percentage_passed1
		
		Percentage_passed1 = 0
		label.set("Starting Part B")
		window.update()
		os.chdir(home)
		
		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm) + "2")
		profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "2")
		profile.set_preference(("browser.download.F" + str(StockTerm) + "2"), r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "2")
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		profile.update_preferences()

		driver = webdriver.Firefox(firefox_profile=profile)
		driver.set_page_load_timeout(10)

		try:
			driver.get('https://www.google.co.uk/')
			driver.get('https://www.google.co.uk/search?q=Google+Trends')
			driver.get('https://trends.google.com/trends/?geo=US')
		except Exception as e:
			print("Wifi, Try Connecting to Wifi!")
			return

		Start_Time = time.time()

		Terms = list(set(TERMS))

		os.chdir(path2)
		
		print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms Found based on Successful Terms Proccessed so far\n")

		exceptions = 0
		Failed = []
		one = 0

		totalseconds = (len(Terms) * 10.5)
		ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
		print("To Download this much data estimated time of completion is " + str(ETC) + "\n")

		for ii in range(2):
			
			terms = (list(set(Terms + Failed)))
			
			for i, y in enumerate(terms):
				one += 1

				if type(y) is tuple:
					y = ' '.join(y)
				
				print("\n")
				print(str(y) + ": " + str(one) + " out of " + str(len(terms)))
				
				print("################################\n__Downloading the Trends Data of: " + str(y)+ "\n################################")
				
				q = y.replace(",", "")
				z = q.replace(" ", "+")
				cycle = time.time()
				urls = []
				while len(urls) < 9 and (time.time() - cycle) < 30:
					try:
						time.sleep(1)
						print("https://trends.google.com/trends/explore?date=today%203-m&q={}".format(z))
						driver.get("https://trends.google.com/trends/explore?date=today%203-m&q={}".format(z))
						time.sleep(1)
						urls = ui.WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
						print("Page Loaded...")
						exceptions = 0
					except Exception as e:
						print("There was a problem loading the page:\n" + str(e))
						Failed.append(y)
						exceptions += 1
				

				if exceptions == 8:
					messagebox.showinfo("Download Error!", "Multiple failed webpages, Swapping IP via VPN is suggested; or check your wifi...")

				try:
					if urls[9].get_attribute("class") == "widget-actions-item export":
						print("Found it!")
						urls[9].click()
				except Exception as e:
					print("There was a problem pressing the button:\n" + str(e))
					Failed.append(y)

				try:
					Terms.remove(y)
				except:
					pass

				Secondssofar = (time.time() - Start_Time)
				try:
					Percentage_passed1 += 1/len(terms)
				except:
					pass
				Percentage_left = 1 - Percentage_passed1
				Seconds_left = datetime.timedelta(seconds =(Secondssofar/Percentage_passed1)*Percentage_left)
				x = ("ETC = %.2d hours %.2d minutes %.2d seconds" % (Seconds_left.seconds//3600,(Seconds_left.seconds//60)%60, Seconds_left.seconds%60)+ "  (Part B: " + str(ii + 1) + " out of 2.)")
				label.set(x)
				progress['value'] += Percentage_passed0 + Percentage_passed1*10
				window.update()

			for o in os.listdir():
				if "Time" not in str(o):
					try:
						df = pd.read_csv(o)
						df.reset_index(inplace = True)
						term = df.iloc[0,1]
						term.replace(": (Worldwide)", "")
						term = re.sub("[\(\[].*?[\)\]]", "", term)
						Failed.append(term)
					except:
						pass
					os.remove(o)

		z = os.listdir()

		for o in z:
			df = pd.read_csv(o)
			if df.shape[0] < 3:
				df.reset_index(inplace = True)
				term = df.iloc[0,1]
				term.replace(": (Worldwide)", "")
				term = re.sub("[\(\[].*?[\)\]]", "", term)
				Fails.append(term)
				os.remove(o)

		print("\nDownload Complete")
		driver.quit()
		os.chdir(home)

		self.__exit__()


	def Download7Days(self, TERMS, Percentage_passed0):

		global Percentage_passed1
		Successful_Terms = PosTerms1 + NegTerms1 + PosTerms2 + NegTerms2 + PosTerms3 + NegTerms3 + PosTerms4 + NegTerms4
		print(Successful_Terms)
		
		Percentage_passed1 = 0
		progress = Progressbar(window, length=500, mode='determinate')
		progress.grid(column = 1, row = 30, columnspan = 3 )
		global label
		label = tk.StringVar()
		label.set("Initialising...")
		title0 = tk.Label(textvariable = label , font = ("Calibri", 20))
		title0.grid(column = 1, row = 29, columnspan = 3, padx=5, pady=5)
		window.update()
		# os.chdir(TOR)
		# p = subprocess.Popen(
		# ['firefox.exe'], stdin=subprocess.PIPE)
		os.chdir(home)
		#####
		
		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm)+"3")
		profile.set_preference("browser.download.downloadDir", r"C:\Users\Grego\Downloads\F" + str(StockTerm)+"3")
		profile.set_preference(("browser.download.F" + str(StockTerm)+"3"), r'C:\Users\Grego\Downloads\F' + str(StockTerm)+"3")
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		profile.update_preferences()

		driver = webdriver.Firefox(firefox_profile=profile)
		driver.set_page_load_timeout(30)

		#try:
		#	driver.get('https://www.google.co.uk/')
		#	#driver.get('https://www.google.co.uk/search?q=Google+Trends')
		#	driver.get('https://trends.google.com/trends/?geo=US')
		#except Exception as e:
		#	messagebox.showinfo("Wifi", "Try Connecting to Wifi!")
		#	title0.grid_forget()
		#	progress.grid_forget()
		#	window.update()
		#	print("Wifi Connection Error")
		#	return

		Terms = list(set(TERMS))

		os.chdir(home)
		
		print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms Found based on seeds " + str(Seeds) + "\n")

		exceptions = 0
		Failed = []
		one = 0
		Pauses = 0
		Paused = False

		totalseconds = (len(Terms) * 10.5)

		ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
		print("To Download this much data estimated time of completion is " + str(ETC) + "\n")

		time.sleep(10)
		exceptions = 0
		Successes = 0

		Start_Time = time.time()
		for ii in range(2):
			
			terms = (list(set(Terms + Failed)))
			Failed = []
			Terms = []
			lenterms = len(terms)
			termscopy = terms.copy()

			for one, y in enumerate(termscopy):

				if type(y) is tuple:
					y = ' '.join(y)

				print("\n")
				print(str(y) + ": " + str(one) + " out of " + str(lenterms))
				
				print("################################\n__Downloading the Trends Data of: " + str(y)+ "\n################################")
				
				q = y.replace(",", "")
				z = q.replace(" ", "+")

				cycle = time.time()
				urls = []
				time.sleep(1)
				while len(urls) < 9 and (time.time() - cycle) < 30:
					try:
						driver.get('https://trends.google.com/trends/?geo=US')
						time.sleep(1)
						print("https://trends.google.com/trends/explore?date=now%207-d&geo=US&q={}".format(z))
						driver.get("https://trends.google.com/trends/explore?date=now%207-d&geo=US&q={}".format(z))
						time.sleep(5)
						urls = ui.WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
						print("Page Loaded...")
						
					except Exception as e:
						if str(e) == 'Message: Timeout loading page after 30000ms':
							time.sleep(100)
						print("There was a problem loading the page:\n" + str(e))
						Failed.append(y)
						exceptions += 1

				try:
					if urls[9].get_attribute("class") == "widget-actions-item export":
						print("Found it!")
						urls[9].click()
						Successes += 1
				except Exception as e:
					print("There was a problem pressing the button:\n" + str(e))
					Failed.append(y)
					exceptions += 1

				try:
					terms.remove(y)
				except:
					pass

				if exceptions >= 10:
					Successes = 0
					Pauses += 1
					Paused = True
					#messagebox.showinfo("Download Error!", "Multiple failed webpages, Swapping IP via VPN is suggested; or check your wifi...")
					os.chdir(home)
					termsandf = (list(set(terms + Failed)))
					with open("DownloadFinal.txt", "w", encoding="utf-8") as f:
						f.write(str(termsandf))
						print(str(termsandf))
					print("Saved")
					print("pausing")
					driver.quit()
					os.chdir(TOR)
					try:
						p.kill()
					except Exception as e:
						print(e)
						pass
					time.sleep(300)
					p = subprocess.Popen(
					 ['firefox.exe'], stdin=subprocess.PIPE)
					os.chdir(home)
					exceptions = 0
		
					profile = webdriver.FirefoxProfile(profile_path)
					profile.set_preference("browser.download.manager.showWhenStarting",False)
					profile.set_preference("browser.download.folderList",2)
					profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm)+"3")
					profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm)+"3")
					profile.set_preference("browser.download.F" + str(StockTerm)+"3", r'C:\Users\Grego\Downloads\F' + str(StockTerm)+"3")
					profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
					profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
					profile.set_preference("network.proxy.type", 1)
					profile.set_preference("network.proxy.socks", "127.0.0.1")
					profile.set_preference("network.proxy.socks_port", 9150)
					profile.set_preference("network.proxy.socks_version", 5)
					profile.update_preferences()

					driver = webdriver.Firefox(firefox_profile=profile)
					driver.set_page_load_timeout(30)

					try:
						driver.get("https://www.whatsmyip.org/")
						driver.get("https://www.youtube.com/")
						driver.get('https://www.google.co.uk/')
						driver.get('https://www.google.co.uk/search?q=Google+Trends')
						driver.get('https://trends.google.com/trends/?geo=US')
						time.sleep(5)
					except:
						pass

					try:
						driver.get('https://trends.google.com/trends/?geo=US')
					except Exception as e:
						print("There was a problem restarting:")
						print(e)
						pass
					
				try:
					Secondssofar = (time.time() - Start_Time)
					print(str(Pauses) + " Pauses")
					Percentage_passed = one/lenterms
					print(str(Percentage_passed*100) + "%")
					Percentage_left = 1 - Percentage_passed
					Seconds_left = datetime.timedelta(seconds =(Secondssofar/Percentage_passed)*Percentage_left)
					x = ("ETC = %.2d hours %.2d minutes %.2d seconds" % (Seconds_left.seconds//3600,(Seconds_left.seconds//60)%60, Seconds_left.seconds%60)+ "  (" + str(ii + 1) + " out of 2.)")
					print(x)
					label.set(x)
					progress['value'] = Percentage_passed*100
					window.update()
				except:
					pass

				if Successes > 100 and Paused == True:
					Successes = 0
					exceptions = 0
					driver.quit()
					try:
						p.kill()
					except Exception as e:
						print(e)
						pass
					os.chdir(home)
					profile = webdriver.FirefoxProfile(profile_path)
					profile.set_preference("browser.download.manager.showWhenStarting",False)
					profile.set_preference("browser.download.folderList",2)
					profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm)+"3")
					profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm)+"3")
					profile.set_preference("browser.download.F" + str(StockTerm)+"3", r'C:\Users\Grego\Downloads\F' + str(StockTerm)+"3")
					profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
					profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
					driver = webdriver.Firefox(firefox_profile=profile)
					driver.set_page_load_timeout(30)
					try:
						driver.get('https://www.google.co.uk/')
						driver.get('https://www.google.co.uk/search?q=Google+Trends')
						driver.get('https://trends.google.com/trends/?geo=US')
						time.sleep(5)
					except:
						exceptions = 10
						pass

					try:
						driver.get('https://trends.google.com/trends/?geo=US')
					except Exception as e:
						print("There was a problem restarting:")
						print(e)
						pass

		os.chdir(path3)
		z = os.listdir()

		for o in z:
			df = pd.read_csv(o)
			if df.shape[0] < 3:
				df.reset_index(inplace = True)
				term = df.iloc[0,1]
				term.replace(": (Worldwide)", "")
				term = re.sub("[\(\[].*?[\)\]]", "", term)
				Fails.append(term)
				os.remove(o)

		print("\nDownload Complete")
		driver.quit()
		os.chdir(home)
		try:
			p.kill()
		except:
			pass

		title0.grid_forget()
		progress.grid_forget()
		window.update()

		self.__exit__()


	def show(self):
		pd.plotting.register_matplotlib_converters()
		global today
		today = date.today()
		global progress

		Start = today - datetime.timedelta(7)
		Minus4Days = today - datetime.timedelta(4)
		Minus3Days = today - datetime.timedelta(3)
		Minus2Days = today - datetime.timedelta(2)
		Minus1Day = today - datetime.timedelta(1)
		MarketOpen = datetime.time(14,0,0)
		MarketClose = datetime.time(21,0,0)
		Graph1 = datetime.time(13,0,0)
		Hour1 = datetime.time(14,0,0)
		Hour2 = datetime.time(15,0,0)
		Hour3 = datetime.time(16,0,0)
		Hour4 = datetime.time(17,0,0)
		Hour5 = datetime.time(18,0,0)
		Hour6 = datetime.time(19,0,0)
		Hour7 = datetime.time(20,0,0)
		Hour8 = datetime.time(21,0,0)
		Graph2 = datetime.time(22,0,0)

		sStock = input('Please input the last known Stock Price:')
		sStock = float(sStock)
		
		Times = [datetime.time(14,0,0), datetime.time(15,0,0), datetime.time(16,0,0), datetime.time(17,0,0), datetime.time(18,0,0), datetime.time(19,0,0), datetime.time(20,0,0), datetime.time(21,0,0)]
		TodayPrediction = pd.DataFrame({'Time': Times, 'New': [0]*8})
		TodayPredictionVanilla = pd.DataFrame({'Time': Times, 'New': [0]*8})
		TomorrowPrediction = pd.DataFrame({'Time': Times, 'New': [0]*8})
		DataSet_Today = pd.DataFrame({'Time': Times, 'New': [sStock]*8})
		DataSet_TodayVanilla = pd.DataFrame({'Time': Times, 'New': [sStock]*8})
		DataSet_Tomorrow = pd.DataFrame({'Time': Times, 'New': [sStock]*8})

		NASDAQ = input('Prediction for the NASDAQ (Strong Buy --> 20 --- Strong Sell --> -20):')
		News = input('Recent News Headlines (Very Postive --> 30 --- Very Negative --> -30):')
		NASDAQ = (float(NASDAQ) + float(News))/2
		print(NASDAQ)

		os.chdir(DataSets)
		z = os.listdir()
		Num = 0
		for o in z.copy():
			if StockTerm not in str(o):
				z.remove(o)

		print(z)
		for o in z:
			os.chdir(DataSets)
			Num += 1
			with open(o, "r", encoding="utf8") as f:
				f = [line.strip() for line in f]
				posTerms1 = literal_eval(f[5])
				posTerms2 = literal_eval(f[7])
				posTerms3 = literal_eval(f[9])
				posTerms4 = literal_eval(f[11])
				negTerms1 = literal_eval(f[13])
				negTerms2 = literal_eval(f[15])
				negTerms3 = literal_eval(f[17])
				negTerms4 = literal_eval(f[19])
			successful_Terms = posTerms1 + negTerms1 + posTerms2 + negTerms2 + posTerms3 + negTerms3 + posTerms4 + negTerms4
			print(successful_Terms)

			progress = Progressbar(window, length=500, mode='determinate')
			progress.grid(column = 1, row = 30, columnspan = 3 )
			global label
			label = tk.StringVar()
			label.set("Loading...")
			title0 = tk.Label(textvariable = label , font = ("Calibri", 20))
			title0.grid(column = 1, row = 29, columnspan = 3, padx=5, pady=5)
			window.update()

			os.chdir(path3)
			c = os.listdir()
			
			for p in c:
				#print(p)
				os.chdir(path3)
				try:
					df = pd.read_csv(p)
				except Exception as e:
					#os.remove(p)
					continue
				if df.shape[0] < 3:
					df.reset_index(inplace = True)
					term = df.iloc[0,1]
					term.replace(": (United States)", "")
					term = re.sub("[\(\[].*?[\)\]]", "", term)
					#Fails.append(term)
					#os.remove(p)
					continue
				df.reset_index(inplace = True)
				term = df.iloc[0,1]
				term = term.replace(": (United States)", "")
				term = re.sub("[\(\[].*?[\)\]]", "", term)
				if term in successful_Terms:
					successful_Terms.remove(term)
				else:
					continue
				df.drop(df.index[0], inplace = True)
				df.replace('<1', 0.5, inplace = True)
				df.columns = ['Time', 'Enddata']
				Time = []
				for x in list(df.Time):
					x = x.split('T')
					datea = x[0].replace('-', '')
					date1 = datea[0:4]
					date2 = str(datea[4:5].replace('0', '')) + str(datea[5:6])
					date3 = str(datea[6:7].replace('0', '')) + str(datea[7:8])
					timecell = datetime.datetime(int(date1), int(date2), int(date3), int(x[1]))
					Time.append(timecell)
				df['Time'] = Time
				df['Difference'] = [0] + [float(s) - float(t) for t, s in zip(list(df['Enddata']), list(df['Enddata'])[1:])]
				print(term)
				print(df)

				if term in posTerms1 or (term + ": ") in posTerms1:
					Day1 = Minus1Day
					Day2 = today
					Day3 = Minus4Days
					op_func = ops['+']
				elif term in posTerms2 or (term + ": ") in posTerms2:
					Day1 = Minus2Days
					Day2 = Minus1Day
					Day3 = today
					op_func = ops['+']
				elif term in posTerms3 or (term + ": ") in posTerms3:
					Day1 = Minus3Days
					Day2 = Minus2Days
					Day3 = Minus1Day
					op_func = ops['+']
				elif term in posTerms4 or (term + ": ") in posTerms4:
					Day1 = Minus4Days
					Day2 = Minus3Days
					Day3 = Minus2Days
					op_func = ops['+']				
				elif term in negTerms1 or (term + ": ") in negTerms1:
					Day1 = Minus1Day
					Day2 = today
					Day3 = Minus4Days
					op_func = ops['-']
				elif term in negTerms2 or (term + ": ") in negTerms2:
					Day1 = Minus2Days
					Day2 = Minus1Day
					Day3 = today
					op_func = ops['-']
				elif term in negTerms3 or (term + ": ") in negTerms3:
					Day1 = Minus3Days
					Day2 = Minus2Days
					Day3 = Minus1Day
					op_func = ops['-']
				elif term in negTerms4 or (term + ": ") in negTerms4:
					Day1 = Minus4Days
					Day2 = Minus3Days
					Day3 = Minus2Days
					op_func = ops['-']
					
				else:
					print(term + " not in set")
					pass
				#print(df['Difference'])
				
				for index, x in df.iterrows():
					#print(x)
					if Day1 <= x['Time'].date() and Day2 > x['Time'].date() and x['Time'].time() >= MarketOpen and x['Time'].time() <= MarketClose:
						print(str(op_func(1,1)))
						print(x['Difference'])
						TheDifference = op_func(x['Difference'], NASDAQ)/20
						TheDifferenceVanilla = (x['Difference'])/16
						if Hour1 == x['Time'].time():
							DataSet_Today['New'][0] = op_func(DataSet_Today.loc[0].at['New'], TheDifference/4.5)
							DataSet_TodayVanilla['New'][0] = op_func(DataSet_TodayVanilla.loc[0].at['New'], TheDifferenceVanilla/4.5)
						elif Hour2 == x['Time'].time():
							DataSet_Today['New'][1] = op_func(DataSet_Today.loc[1].at['New'], TheDifference/5)
							DataSet_TodayVanilla['New'][1] = op_func(DataSet_TodayVanilla.loc[1].at['New'], TheDifferenceVanilla/5)
						elif Hour3 == x['Time'].time():
							DataSet_Today['New'][2] = op_func(DataSet_Today.loc[2].at['New'], TheDifference/5.5)
							DataSet_TodayVanilla['New'][2] = op_func(DataSet_TodayVanilla.loc[2].at['New'], TheDifferenceVanilla/5.5)
						elif Hour4 == x['Time'].time():
							DataSet_Today['New'][3] = op_func(DataSet_Today.loc[3].at['New'], TheDifference/6.5)
							DataSet_TodayVanilla['New'][3] = op_func(DataSet_TodayVanilla.loc[3].at['New'], TheDifferenceVanilla/6.5)
						elif Hour5 == x['Time'].time():
							DataSet_Today['New'][4] = op_func(DataSet_Today.loc[4].at['New'], TheDifference/7.5)
							DataSet_TodayVanilla['New'][4] = op_func(DataSet_TodayVanilla.loc[4].at['New'], TheDifferenceVanilla/7.5)
						elif Hour6 == x['Time'].time():
							DataSet_Today['New'][5] = op_func(DataSet_Today.loc[5].at['New'], TheDifference/6.5)
							DataSet_TodayVanilla['New'][5] = op_func(DataSet_TodayVanilla.loc[5].at['New'], TheDifferenceVanilla/6.5)
						elif Hour7 == x['Time'].time():
							DataSet_Today['New'][6] = op_func(DataSet_Today.loc[6].at['New'], TheDifference/6.5)
							DataSet_TodayVanilla['New'][6] = op_func(DataSet_TodayVanilla.loc[6].at['New'], TheDifferenceVanilla/6.5)
						elif Hour8 == x['Time'].time():
							DataSet_Today['New'][7] = op_func(DataSet_Today.loc[7].at['New'], TheDifference/6)
							DataSet_TodayVanilla['New'][7] = op_func(DataSet_TodayVanilla.loc[7].at['New'], TheDifferenceVanilla/6)

					elif Day2 <= x['Time'].date() and Day3 > x['Time'].date() and x['Time'].time() >= MarketOpen and x['Time'].time() <= MarketClose:
						TheDifference2 = (x['Difference'])/11
						if Hour1 == x['Time'].time():
							DataSet_Tomorrow['New'][0] = op_func(DataSet_Tomorrow.loc[0].at['New'], TheDifference2/9)
						elif Hour2 == x['Time'].time():
							DataSet_Tomorrow['New'][1] = op_func(DataSet_Tomorrow.loc[1].at['New'], TheDifference2/10)
						elif Hour3 == x['Time'].time():
							DataSet_Tomorrow['New'][2] = op_func(DataSet_Tomorrow.loc[2].at['New'], TheDifference2/11)
						elif Hour4 == x['Time'].time():
							DataSet_Tomorrow['New'][3] = op_func(DataSet_Tomorrow.loc[3].at['New'], TheDifference2/12)
						elif Hour5 == x['Time'].time():
							DataSet_Tomorrow['New'][4] = op_func(DataSet_Tomorrow.loc[4].at['New'], TheDifference2/13)
						elif Hour6 == x['Time'].time():
							DataSet_Tomorrow['New'][5] = op_func(DataSet_Tomorrow.loc[5].at['New'], TheDifference2/13)
						elif Hour7 == x['Time'].time():
							DataSet_Tomorrow['New'][6] = op_func(DataSet_Tomorrow.loc[6].at['New'], TheDifference2/11)
						elif Hour8 == x['Time'].time():
							DataSet_Tomorrow['New'][7] = op_func(DataSet_Tomorrow.loc[7].at['New'], TheDifference2/10)

				print(DataSet_Today)

			if successful_Terms != []:
				print("INCOMPLETE DATASET")
				print("These remain" + str(successful_Terms))

			os.chdir(save)
			print(DataSet_Today)

			DataSet_TodayPlot = plt.figure(1)
			plt.plot(DataSet_Today['Time'].astype('O'), DataSet_Today['New'], label = "Today " + str(Num))
			plt.xlim(Graph1, Graph2)
			plt.ylim(min(DataSet_Today['New']) - 0.1, max(DataSet_Today['New']) + 0.1)
			DataSet_TodayPlot.canvas.set_window_title("Data Set" + str(Num) + " Today's Prediction")
			

			DataSet_TodayVanillaPlot = plt.figure(2)
			plt.plot(DataSet_TodayVanilla['Time'].astype('O'), DataSet_TodayVanilla['New'], label = "Today Vanilla " + str(Num))
			plt.xlim(Graph1, Graph2)
			plt.ylim(min(DataSet_TodayVanilla['New'])- 0.1, max(DataSet_TodayVanilla['New']) + 0.1)
			DataSet_TodayVanillaPlot.canvas.set_window_title("Data Set" + str(Num) + "Today's Prediction Without User input")
		

			DataSet_TomorrowPlot = plt.figure(3)
			plt.plot(DataSet_Tomorrow['Time'].astype('O'), DataSet_Tomorrow['New'], label = "Tomorrow " + str(Num))
			plt.xlim(Graph1, Graph2)
			plt.ylim(min(DataSet_Tomorrow['New']) - 0.1, max(DataSet_Tomorrow['New']) + 0.1)
			DataSet_TomorrowPlot.canvas.set_window_title("Data Set" + str(Num) + "Tomorrow's Prediction")
			

			TodayPrediction['New'] = TodayPrediction['New'] + DataSet_Today['New']
			TodayPredictionVanilla['New'] = TodayPredictionVanilla['New'] + DataSet_TodayVanilla['New']
			TomorrowPrediction['New'] = TomorrowPrediction['New'] + DataSet_Tomorrow['New']

		os.chdir(save)

		TodayPrediction['New'] = TodayPrediction['New']/len(z)
		TodayPredictionVanilla['New'] = TodayPredictionVanilla['New']/len(z)
		TomorrowPrediction['New'] = TomorrowPrediction['New']/len(z)

		label.set("Done!")
		TodayChange = ((float(TodayPrediction['New'][7]) - float(TodayPrediction['New'][0]))/float(TodayPrediction['New'][7]))*100
		MidHourRange = ((max(list(TodayPrediction['New'])[1:5]) - min(list(TodayPrediction['New'])[1:5]))/max(TodayPrediction['New'][1:5]))*100
		print("The last close was: " + str(sStock))
		print("\n")
		print("Tomorrow's Prediction")
		print(TomorrowPrediction.to_string())
		print("\n")
		progress['value'] = 100
		window.update()
		print("Today's Prediction")
		print(TodayPrediction.to_string())
		print("\n")
		print("Today's Change")
		print(str(TodayChange) + "%")
		print(str(MidHourRange) + "%")
		os.chdir(save)
		
		TodayPrediction.to_csv(str(StockTerm) + 'Prediction ' + str(today) + '.csv')
		plt.style.use('ggplot')
		pylab.legend(loc='upper left')
		plt.ylabel('Prediction')	

		title0.grid_forget()
		progress.grid_forget()
		window.update()

		Todayplot = plt.figure(4)
		plt.plot(TodayPrediction['Time'].astype('O'), TodayPrediction['New'], label = "Today")
		plt.xlim(Graph1, Graph2)
		plt.ylim(min(TodayPrediction['New']) - 0.1, max(TodayPrediction['New']) + 0.1)
		Todayplot.canvas.set_window_title("Today's Prediction")
		plt.savefig(str(StockTerm) + " " + str(today) + " " + str(time.time()) + " Today.jpeg")
		

		TodayplotVanilla = plt.figure(5)
		plt.plot(TodayPredictionVanilla['Time'].astype('O'), TodayPredictionVanilla['New'], label = "Today")
		plt.xlim(Graph1, Graph2)
		plt.ylim(min(TodayPredictionVanilla['New']) - 0.1, max(TodayPredictionVanilla['New']) + 0.1)
		TodayplotVanilla.canvas.set_window_title("Today's Prediction Without User input")
		plt.savefig(str(StockTerm) + " " + str(today) + " " + str(time.time()) + " Today Without User input.jpeg")
		

		Tomorrowplot = plt.figure(6)
		plt.plot(TomorrowPrediction['Time'].astype('O'), TomorrowPrediction['New'], label = "Today")
		plt.xlim(Graph1, Graph2)
		plt.ylim(min(TomorrowPrediction['New']) - 0.1, max(TomorrowPrediction['New']) + 0.1)
		Tomorrowplot.canvas.set_window_title("Tomorrow's Prediction")
		plt.savefig(str(StockTerm) + " " + str(today) + " " + str(time.time()) + " Tomorrow.jpeg")
		

		DataSet_TodayPlot.show()
		DataSet_TodayVanillaPlot.show()
		DataSet_TomorrowPlot.show()
		Todayplot.show()
		TodayplotVanilla.show()
		Tomorrowplot.show()

	def __exit__(self):
		os.chdir(save)
		try:
			with open(str(StockTerm) + "Data Printout - (" + str(today) + ").txt", "w", encoding="utf-8") as f:
				f.write("""
##############################
        Data Printout:               
 Seed Terms:
{}

 Stock:
{}

 Start Date:
{}

 End Date:
{}

 Average Success Rate:
{}

 Correlation Technique:
{}

 Predicition:

 Success?:
[>>Enter Here<<]

 Number of Related Words that were researched further:
{}

 Positive Terms 1 Day Before:
{}
 Positive Terms 2 Day Before:
{}
 Positive Terms 3 Day Before:
{}
 Positive Terms 4 Day Before:
{}
 Negative Terms 1 Day Before:
{}
 Negative Terms 2 Day Before:
{}
 Negative Terms 3 Day Before:
{}
 Negative Terms 4 Day Before:
{}

############################## 

					""".format(Seeds, StockTerm, start, end, AVGRATE, Correlation_technique, Numofwords, PosTerms1, PosTerms2, PosTerms3, PosTerms4, NegTerms1, NegTerms2, NegTerms3, NegTerms4))
				print("Saved")
		except Exception as e:
			print(e)
			pass

		with open(str(StockTerm) + "Data Save.txt", "w", encoding="utf-8") as f:
			try:
				f.write("""
##############################
        Data Printout:               
 Seed Terms:
{}

 Stock:
{}

 Start Date:
{}

 End Date:
{}

 Average Success Rate:
{}

 Correlation Technique:
{}

 Predicition:

 Success?:
[>>Enter Here<<]

 Number of Related Words that were researched further:
{}

 Positive Terms 1 Day Before:
{}
 Positive Terms 2 Day Before:
{}
 Positive Terms 3 Day Before:
{}
 Positive Terms 4 Day Before:
{}
 Negative Terms 1 Day Before:
{}
 Negative Terms 2 Day Before:
{}
 Negative Terms 3 Day Before:
{}
 Negative Terms 4 Day Before:
{}

############################## 

					""".format(Seeds, StockTerm, start, end, AVGRATE, Correlation_technique, Numofwords, PosTerms1, PosTerms2, PosTerms3, PosTerms4, NegTerms1, NegTerms2, NegTerms3, NegTerms4))
				print("Saved")
			except Exception as e:
				print(e)
				f.write("""
##############################
        Data Printout:               
 Seed Terms:
{}

 Stock:
{}

 Start Date:
{}

 End Date:
{}

 Average Success Rate:
{}

 Correlation Technique:
{}

 Predicition:

 Success?:
[>>Enter Here<<]

 Number of Related Words that were researched further:
{}

 Positive Terms 1 Day Before:
--Proccessing Needed--
 Positive Terms 2 Day Before:
--Proccessing Needed--
 Positive Terms 3 Day Before:
--Proccessing Needed--
 Positive Terms 4 Day Before:
--Proccessing Needed--
 Negative Terms 1 Day Before:
--Proccessing Needed--
 Negative Terms 2 Day Before:
--Proccessing Needed--
 Negative Terms 3 Day Before:
--Proccessing Needed--
 Negative Terms 4 Day Before:
--Proccessing Needed--
############################## 

				""".format(Seeds, StockTerm, start, end, AVGRATE, Correlation_technique, Numofwords))
				print("Saved")
				pass

		try:
			print("""
##############################
        Data Printout:               
 Seed Terms:
{}

 Stock:
{}

 Start Date:
{}

 End Date:
{}

 Average Success Rate:
{}

 Correlation Technique:
{}

 Predicition:

 Success?:
[>>Enter Here<<]

 Number of Related Words that were researched further:
{}

 Positive Terms 1 Day Before:
{}
 Positive Terms 2 Day Before:
{}
 Positive Terms 3 Day Before:
{}
 Positive Terms 4 Day Before:
{}
 Negative Terms 1 Day Before:
{}
 Negative Terms 2 Day Before:
{}
 Negative Terms 3 Day Before:
{}
 Negative Terms 4 Day Before:
{}

############################## 

					""".format(Seeds, StockTerm, start, end, AVGRATE, Correlation_technique, Numofwords, PosTerms1, PosTerms2, PosTerms3, PosTerms4, NegTerms1, NegTerms2, NegTerms3, NegTerms4))
			print("Saved")
		except Exception as e:
			print(e)
			pass

		try:
			with open(str(StockTerm) + "rWords.txt", "w", encoding="utf-8") as f:
				f.write(str(rWords))
			print("Saved Related words")
		except Exception as e:
			print(e)
			pass

		try:
			with open(str(StockTerm) + "Wiki.txt", "w", encoding="utf-8") as f:
				f.write(str(Wiki_words))
			print("Saved Wiki")
		except Exception as e:
			print(e)
			pass

		try:
			with open(str(StockTerm) + "Google.txt", "w", encoding="utf-8") as f:
				f.write(str(Google_words))
			print("Saved Google")
		except Exception as e:
			print(e)
			pass

		try:
			with open(str(StockTerm) + "News.txt", "w", encoding="utf-8") as f:
				f.write(str(News_words))
			print("Saved News")
		except Exception as e:
			print(e)
			pass

		try:
			with open(str(StockTerm) + "fails.txt", "w", encoding="utf-8") as f:
				for fail in Fails:
					f.write(str(fail) + "\n")
			print("Saved Fails")
		except Exception as e:
			print(e)
			pass

		try:
			with open("LastStock.txt", "w", encoding="utf8") as f:
				f.write(str(StockTerm))
		except:
			pass

		os.chdir(home)
		

"""The Interface"""



title = tk.Label(text = "These are the starting words that the algorithym will use", bg = "DeepSkyBlue2", font = ("Calibri", 20))
title.grid(column = 1, row = 1, columnspan = 3, padx=5, pady=5)

entry_field1 = tk.Entry( window, textvariable=entryText1 )
entry_field1.grid(column = 1, row = 3, columnspan = 1 )
entry_field2 = tk.Entry( window, textvariable=entryText2 )
entry_field2.grid(column = 2, row = 3, columnspan = 1 )
entry_field3 = tk.Entry( window, textvariable=entryText3 )
entry_field3.grid(column = 3, row = 3, columnspan = 1 )
entry_field4 = tk.Entry( window, textvariable=entryText4 )
entry_field4.grid(column = 1, row = 4, columnspan = 1 )
entry_field5 = tk.Entry( window, textvariable=entryText5 )
entry_field5.grid(column = 2, row = 4, columnspan = 1 )
entry_field6 = tk.Entry( window, textvariable=entryText6 )
entry_field6.grid(column = 3, row = 4, columnspan = 1 )
entry_field7 = tk.Entry( window, textvariable=entryText7 )
entry_field7.grid(column = 1, row = 5, columnspan = 1 )
entry_field8 = tk.Entry( window, textvariable=entryText8 )
entry_field8.grid(column = 2, row = 5, columnspan = 1 )
entry_field9 = tk.Entry( window, textvariable=entryText9 )
entry_field9.grid(column = 3, row = 5, columnspan = 1 )

title2 = tk.Label(text = "The stock to correlate with:", bg = "cyan2", font = ("Calibri", 20))
title2.grid(column = 1, row = 6, padx=5, pady=5, columnspan = 3 )

entry_field10 = tk.Entry( window, textvariable=entryText10 )
entry_field10.grid(column = 1, row = 7, columnspan = 3 )

title3 = tk.Label(text = "Settings:", bg = "aquamarine2", font = ("Calibri", 20))
title3.grid(column = 1, row = 8, padx=5, pady=5, columnspan = 3 )

title4 = tk.Label(text = "How many related words do\nyou want to reseach further\n('ALL' accepted)", bg = "seashell2", font = ("Calibri", 8))
title4.grid(column = 3, row = 9, columnspan = 1 )
title5 = tk.Label(text = "Start Date\n(accept YYYY-MM-DD or -xdays)\nDefault 269 days (leave blank)", bg = "seashell2", font = ("Calibri", 8))
title5.grid(column = 2, row = 9, columnspan = 1 )
title6 = tk.Label(text = "End Date\n(accept YYYY-MM-DD or -xdays)\nDefault Today (leave blank)", bg = "seashell2", font = ("Calibri", 8))
title6.grid(column = 1, row = 9, columnspan = 1 )

entry_field13 = tk.Entry( window, textvariable=entryText13 )
entry_field13.grid(column = 3, row = 10, padx=5, pady=(5,20), columnspan = 1 )
entry_field14 = tk.Entry( window, textvariable=entryText14 )
entry_field14.grid(column = 2, row = 10, padx=5, pady=(5,20), columnspan = 1 )
entry_field15 = tk.Entry( window, textvariable=entryText15 )
entry_field15.grid(column = 1, row = 10, padx=5, pady=(5,20), columnspan = 1 )

def related():
	Data_Mining().Related_words()

def wiki():
	Wiki_words = []
	for y in rWords:
		if Numofwords != 'ALL':
			Data_Mining().Wiki(Related = y[0:int(Numofwords)])
		else:
			Data_Mining().Wiki(Related = y)

def News():
	News_words = []
	for y in rWords:
		if Numofwords != 'ALL':
			Data_Mining().News(Related = y[0:int(Numofwords)])
		else:
			Data_Mining().News(Related = y)

def Google():
	Google_words = []
	for y in rWords:
		if Numofwords != 'ALL':
			Data_Mining().Google(Related = y[0:int(Numofwords)])
		else:
			Data_Mining().Google(Related = y)

def stocks():
	Data_Mining().stocks()

def Download():
	
	Completed = True
	os.chdir(home)

	#with open("Download.txt", "r", encoding="utf8") as f:
	#	y = str(f.read())
	#	
	#	y.replace(",","")
	#	y.replace("/","")
	#	y.replace(";","")
	#	y.replace(":","")
	#	y.replace("*","")
	#	y.replace("{","")
	#	y.replace("}","")
	#	print(y)
	#	x = literal_eval(y)



	if Completed == True:
		Data_Mining().__init__()
		Termsrelated = [j for i in rWords for j in i]
		x = Seeds + Termsrelated + Wiki_words + News_words + Google_words + ExtraSeeds
		#with open("NWSTERMS.txt", "w", encoding="utf8") as f:
		#	x = literal_eval(f.read())
		print("New Download")
		print(x)
	else:
		try:
			with open("Download.txt", "r", encoding="utf8") as f:
				x = literal_eval(f.read())
		except Exception as e:
			print(e)
			pass





	Data_Mining().Download(x)

def Processing():
	Data_Mining().Processing()

def Downloadfin():
	os.chdir(DataSets)
	z = os.listdir()
	Successful_Terms = []
	for x in z:
		with open(x, "r", encoding="utf-8")as f:
			f = [line.strip() for line in f]
			posTerms1 = literal_eval(f[5])
			for a in posTerms1:
				Successful_Terms.append(a)
			posTerms2 = literal_eval(f[7])
			for a in posTerms2:
				Successful_Terms.append(a)
			posTerms3 = literal_eval(f[9])
			for a in posTerms3:
				Successful_Terms.append(a)
			posTerms4 = literal_eval(f[11])
			for a in posTerms4:
				Successful_Terms.append(a)
			negTerms1 = literal_eval(f[13])
			for a in negTerms1:
				Successful_Terms.append(a)
			negTerms2 = literal_eval(f[15])
			for a in negTerms2:
				Successful_Terms.append(a)
			negTerms3 = literal_eval(f[17])
			for a in negTerms3:
				Successful_Terms.append(a)
			negTerms4 = literal_eval(f[19])
			for a in negTerms4:
				Successful_Terms.append(a)
	os.chdir(path3)
	z = os.listdir()
	for c in z:
		try:
			df = pd.read_csv(c)
			df.reset_index(inplace = True)
			term = df.iloc[0,1]
			term.replace(": (United States)", "")
			term = re.sub("[\(\[].*?[\)\]]", "", term)
			Successful_Terms.remove(term)
			print("removed" + term)
		except:
			pass
	print("Starting")
	Data_Mining().Download7Days(Successful_Terms, 0)

def show():
	Data_Mining().show()
	
def Start():

	if var1.get() == True:
		related()

	if var2.get() == True:
		wiki()

	if var3.get() == True:
		News()

	if var4.get() == True:
		Google()

	if var6.get() == True:
		Download()

	if var5.get() == True:
		stocks()

	if var7.get() == True:
		Processing()

	if var8.get() == True:
		Downloadfin()

	if var9.get() == True:
		show()


def Save():
	Data_Mining().__exit__()


def ClearFiles():
	print("No way, only folder 3")

	# os.chdir(path)
	# z = listdir()
	# for o in os.listdir():
	# 	os.remove(o)
	# os.chdir(path2)
	# z = listdir()
	# for o in os.listdir():
	# 	os.remove(o)
	os.chdir(path3)
	z = listdir()
	for o in os.listdir():
		os.remove(o)

def ClearTerms():
	global rWords
	global Wiki_words
	global Google_words
	global News_words
	global SuccessFinalTerms
	global ExtraSeeds

	Wiki_words = []
	Google_words = []
	News_words = []
	SuccessFinalTerms = []
	rWords = []
	ExtraSeeds = []

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()
var6 = tk.BooleanVar()
var7 = tk.BooleanVar()
var8 = tk.BooleanVar()
var9 = tk.BooleanVar()


button1 = tk.Button(text="Related Words", bg = "SeaGreen1", font = ("Calibri", 15), command = related)
button1.grid(column = 1, row = 16, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var1).grid(row=17, column = 1)

button2 = tk.Button(text="Wikipedia", bg = "SeaGreen1", font = ("Calibri", 15), command = wiki)
button2.grid(column = 2, row = 16, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var2).grid(row=17, column = 2)

button3 = tk.Button(text="News Headlines", bg = "SeaGreen1", font = ("Calibri", 15), command = News)
button3.grid(column = 3, row = 16, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var3).grid(row=17, column = 3)

button4 = tk.Button(text="Google Results", bg = "SpringGreen2", font = ("Calibri", 15), command = Google)
button4.grid(column = 1, row = 19, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var4).grid(row=20, column = 1)

button11 = tk.Button(text="Save", bg = "SpringGreen2", font = ("Calibri", 15), command = Save)
button11.grid(column = 2, row = 19, columnspan = 1 )


button5 = tk.Button(text="Download Stock Data", bg = "SpringGreen2", font = ("Calibri", 15), command = stocks)
button5.grid(column = 3, row = 19, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var5).grid(row=20, column = 3)

button6 = tk.Button(text="Download Trends Data", bg = "green2", font = ("Calibri", 15), command = Download)
button6.grid(column = 1, row = 22, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var6).grid(row=23, column = 1)

button7 = tk.Button(text="Processing", bg = "green2", font = ("Calibri", 15), command = Processing)
button7.grid(column = 2, row = 22, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var7).grid(row=23, column = 2)

button8 = tk.Button(text="Download Final Data", bg = "green2", font = ("Calibri", 15), command = Downloadfin)
button8.grid(column = 3, row = 22, columnspan = 1 )
checkbox = tk.Checkbutton(window, variable = var8).grid(row=23, column = 3)

button12 = tk.Button(text="Clear Files", bg = "green2", font = ("Calibri", 15), command = ClearFiles)
button12.grid(column = 1, row = 24, columnspan = 1 )


button13 = tk.Button(text="Clear Terms", bg = "green2", font = ("Calibri", 15), command = ClearTerms)
button13.grid(column = 3, row = 24, columnspan = 1 )


button9 = tk.Button(text="Give Today's Prediction", bg = "DarkOliveGreen3", font = ("Calibri", 20), command = show)
button9.grid(column = 1, row = 26, padx=5, pady=10, columnspan = 3 )
checkbox = tk.Checkbutton(window, variable = var9).grid(row=27, column = 2)

button10 = tk.Button(text="START SELECTED", bg = "khaki1", font = ("Calibri", 20), command = Start)
button10.grid(column = 1, row = 28, padx=5, pady=10, columnspan = 3 )


window.mainloop()