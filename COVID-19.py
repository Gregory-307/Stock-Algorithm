from selenium import webdriver
import urllib
import re
import pandas as pd
from newspaper import Article
from collections import Counter
from pandas_datareader import data, wb
import matplotlib.pyplot as plt; plt.rcdefaults()
import random
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
import os
import natsort
import time
import datetime
from datetime import date
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


home = r'C:\python'
save = r'C:\python\Covid'
profile_path=r"C:\Users\Grego\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default"
TOR = r"C:\Users\Grego\Desktop\Tor Browser\Browser"
# DataSets = r"C:\python\So far\Data Sets"
# path = r'C:\Users\Grego\Downloads\F' + str(StockTerm)
# path2 = r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "2"
# path3 = r'C:\Users\Grego\Downloads\F' + str(StockTerm) + "3"


def QuitDriver():
	driver.quit()
	try:
		p.kill()
	except:
		pass

def LoadTorDriver():
	os.chdir(TOR)
	p = subprocess.Popen(
		['firefox.exe'], stdin=subprocess.PIPE)
	os.chdir(home)

	profile = webdriver.FirefoxProfile(profile_path)
	profile.set_preference("browser.download.manager.showWhenStarting",False)
	profile.set_preference("browser.download.folderList",2)
	profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
	profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	profile.set_preference("browser.download.F" + str(StockTerm), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
	profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.socks", "127.0.0.1")
	profile.set_preference("network.proxy.socks_port", 9150)
	profile.set_preference("network.proxy.socks_version", 5)
	profile.update_preferences()

	driver = webdriver.Firefox(firefox_profile=profile)
	driver.set_page_load_timeout(30) 


def LoadDriver():
	os.chdir(home)
	profile = webdriver.FirefoxProfile(profile_path)
	profile.set_preference("browser.download.manager.showWhenStarting",False)
	profile.set_preference("browser.download.folderList",2)
	profile.set_preference("browser.download.dir", r"C:\python\COVID DOWNLOADS")
	profile.set_preference("browser.download.downloadDir", r"C:\python\COVID DOWNLOADS")
	profile.set_preference(("browser.download.COVID DOWNLOADS"), r"C:\python\COVID DOWNLOADS")
	profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
	profile.update_preferences()

	driver = webdriver.Firefox(firefox_profile=profile)
	driver.set_page_load_timeout(30)

def DownloadTerms(Date1, Date2, TERMS):

	print("Scraping Date from {} to {}".format(Date1, Date2))
	Terms = list(set(TERMS))
	Date1 = datetime.date(Date1)
	Date2 = datetime.date(Date2)
	lenterms = len(TERMS)
	
	totalseconds = (len(Terms) * 10.5)
	ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
	print("To Download this much data estimated time of completion is {}".format(ETC))
	Start_Time = time.time()

	for y in Terms:		
		Downloadstr = ("\nDownloading the Trends Data of: " + str(y))
		
		z = y.replace(",", "")
		z = z.replace(" ", "+")

		cycle = time.time()
		urls = []
		while len(urls) < 9 and (time.time() - cycle) < 20:
			try:
				driver.get('https://trends.google.com/trends/?geo=US')
				time.sleep(0.555)
				Downloadstr = "\n".join(Downloadstr, ("https://trends.google.com/trends/explore?date={}%20{}&q={}".format(Date1, Date2, z)))
				driver.get("https://trends.google.com/trends/explore?date={}%20{}&q={}".format(start, end, z))
				time.sleep(0.5)
				urls = ui.WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
				print("Page Loaded...")
				
				
			except Exception as e:
				Downloadstr = "\n".join(Downloadstr, ("There was a problem loading the page:\n{}\n{} was not downloaded".format(e, y)))

		try:
			if urls[9].get_attribute("class"
				) == "widget-actions-item export":
				print("Found it!")
				urls[9].click()
		except Exception as e:
			Downloadstr = "\n".join(Downloadstr, ("There was a problem downloading:\n{}\n{} was not downloaded".format(e, y)))

	
		
		os.chdir(home)
		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
		profile.set_preference("browser.download.downloadDir", r'C:\Users\Grego\Downloads\F' + str(StockTerm))
		profile.set_preference("browser.download.F" + str(StockTerm), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
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

