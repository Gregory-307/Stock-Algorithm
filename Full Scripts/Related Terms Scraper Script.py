driver = webdriver.Firefox()
rWords = []

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