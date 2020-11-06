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