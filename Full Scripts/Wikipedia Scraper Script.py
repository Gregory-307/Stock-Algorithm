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
