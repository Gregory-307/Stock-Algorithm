os.chdir(home)
		
profile = webdriver.FirefoxProfile(profile_path)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.dir", r"C:\Users\Grego\Downloads\F" + str(StockTerm) )
profile.set_preference("browser.download.downloadDir", r"C:\Users\Grego\Downloads\F" + str(StockTerm))
profile.set_preference(("browser.download.F" + str(StockTerm)), r'C:\Users\Grego\Downloads\F' + str(StockTerm))
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

os.chdir(path)
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
			Terms.remove(term)
	except:
		pass


#for x in Terms:
	#if x in Fails:
		#print(str(x) + " Removed")
		#Terms.remove(x)

os.chdir(home)

print("\nDownloading as many as I can of the " + str(len(Terms)) + " Terms Found based on seeds " + str(Seeds) + "\n")

exceptions = 0
Failed = []
one = 0
Pauses = 0

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
		q = q.replace("-", " ")
		z = q.replace(" ", "+")

		cycle = time.time()
		urls = []
		time.sleep(1)
		while len(urls) < 9 and (time.time() - cycle) < 30:
			try:
				driver.get('https://trends.google.com/trends/?geo=US')
				time.sleep(1)
				print("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
				driver.get("https://trends.google.com/trends/explore?date={}%20{}&geo=US&q={}".format(start, end, z))
				time.sleep(3)
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
			with open("Download.txt", "w", encoding="utf-8") as f:
				f.write(str(termsandf))
				print(str(termsandf))
			print("Saved")
			print("pausing")
			driver.quit()
			os.chdir(TOR)
			try:
				p.kill()
			except:
				pass
			time.sleep(300)
			p = subprocess.Popen(
			['firefox.exe'], stdin=subprocess.PIPE)
			os.chdir(home)
			exceptions = 0

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
			except:
				pass
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


	os.chdir(path)

	z = os.listdir()
	
	for o in z:
		if "Time" not in str(o):
			try:
				df = pd.read_csv(o)
				df.reset_index(inplace = True)
				term = df.iloc[0,1]
				term.replace(": (Worldwide)", "")
				term = re.sub("[\(\[].*?[\)\]]", "", term)
				Failed.append(term)
				os.remove(o)
			except:
				pass
print("\nDownload Complete")
		driver.quit()
os.chdir(home)