import billboard
import datetime

#initialize the data
startDate = datetime.date(2015,1,1)
endDate   = datetime.date(2015,12,31)
ouputFile = open("2015charts.csv","w")

date = startDate
oneDay = datetime.timedelta(days=1)

#Run the program
ouputFile.write("key,value,date\n")
numCharts = 0
while date <= endDate:	
	#if the date is a saturday
	if date.weekday() == 5:
		dateString = date.strftime('%Y-%m-%d')
		chart = billboard.ChartData('hot-100', date=dateString)
		for rank, song in enumerate(chart):
			songKey = song.title + " " + song.artist
			songKey = songKey.replace(",", "")
			songPopularity = (100-rank)/100
			ouputFile.write("%s,%d,%s\n" %(songKey,songPopularity,date.strftime('%m/%d/%y')))
		numCharts+=1
		print numCharts
	date += oneDay
ouputFile.close()