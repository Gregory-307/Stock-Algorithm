from selenium import webdriver
import pandas as pd
import random
import datetime
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from datetime import date
import os

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

	

TESTFILE = TS(r"C:\python", r"C:\Users\gregb\Downloads\TEST", r"C:\Users\gregb\Onedrive\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default", False)
TESTFILE.Scrape(["cat"],2)
TESTFILE.Start_Tor()





