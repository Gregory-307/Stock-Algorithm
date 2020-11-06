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