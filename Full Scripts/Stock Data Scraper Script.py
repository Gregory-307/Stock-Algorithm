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