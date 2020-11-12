from newspaper import Article


def scraper_script(Terms):
	z = term.replace(" ", "_")
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
	return mc
	

def scrape_list(Related):
	Google_words = []
	print("Downloading Google Data for " + str(len(Related)) + " Words.")
	for y in Related:
		try:
			Google_words.append(scraper_script(y)[::2])
		except Exception as e:
			print("\nThis one isn't available, Here is the Error:\n")
			print(e)
			pass
	Google_words = list(set(Google_words))
	return Google_words

