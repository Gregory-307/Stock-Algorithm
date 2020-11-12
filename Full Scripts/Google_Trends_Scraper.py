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
from datetime import date
import os

class TS:
	def __init__(self, homepath, path, profile_path):
		os.chdir(homepath)
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = False
		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", str(path) )
		profile.set_preference("browser.download.downloadDir", str(path))
		profile.set_preference("browser.download."+ str(path).split("\\")[-1], path)
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		profile.update_preferences()
		driver = webdriver.Firefox(firefox_profile=profile, capabilities=cap, executable_path=r"C:\python\geckodriver-v0.23.0-win64")
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
		driver = webdriver.Firefox(firefox_profile=self.profile)
		driver.set_page_load_timeout(30)
		self.profile = profile
		self.driver = driver
		

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
		profile = webdriver.FirefoxProfile(profile_path)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.folderList",2)
		profile.set_preference("browser.download.dir", str(path))
		profile.set_preference("browser.download.downloadDir", str(path))
		profile.set_preference("browser.download." + str(path).split("\\")[-1], str(path))
		profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
		self.profile = profile
		self.driver = webdriver.Firefox(firefox_profile=profile)
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

	def Scrape(self, Terms, Reruns):
		
		print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms")
		ETC = datetime.datetime.now() + datetime.timedelta(seconds=(len(Terms) * 10.4))  
		print("To Download this much data estimated time of completion is " + str(ETC) + "\n")

		exceptions = 0
		one = 0
		Pauses = 0
		Tor = False
		totalseconds = (len(Terms) * 10.5)
		Failed = []

		for one, y in enumerate(Terms):

			if type(y) is tuple:
				y = ' '.join(y)

			print("\n")
			print(str(y) + ": " + str(one) + " out of " + str(lenterms))
			
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
					print("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
					self.driver.get("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
					time.sleep(3)
					urls = ui.WebDriverWait(self.driver, 5).until(EC.presence_of_all_elemenself_located((By.TAG_NAME, "button")))
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

		if Reruns > 0:
			Failed = Failed + FileCheck()
			Scrape(Failed, Reruns-1)
		else:
			print("\nDownload Complete")
			self.driver.quit()
			Refine()
			termsandf = (list(set(Terms + Failed)))
			with open("Download.txt", "w", encoding="utf-8") as f:
				f.write(str(termsandf))
			print("Download Has Ended. These are the terms that were not downloaded:\n" + str(termsandf))

	def FileCheck(self):
		Failed2 = []
		os.chdir(self.path)
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

List1 = TS(r"C:\python", r"C:\Users\Grego\Downloads\TEST", r"C:\Users\Grego\Onedrive\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")
List1.Scrape(["cat"],1)