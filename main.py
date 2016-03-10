import billboard
import datetime

#initialize the data
startDate = datetime.date(2015,1,1)
endDate   = datetime.date(2015,3,31)
ouputFile = open("2015charts.csv","w")

date = startDate
oneDay = datetime.timedelta(days=1)

songData={}
days=[]
#Run the program
ouputFile.write("key,value,date\n")
numCharts = 0
#Gather all the data
while date <= endDate:	
	#if the date is a saturday
	if date.weekday() == 5:
		days.append(date.strftime('%m/%d/%y'))
		chart = billboard.ChartData('hot-100', date=date.strftime('%Y-%m-%d'))
		for rank, song in enumerate(chart):
			songKey = song.title + " " + song.artist
			songKey = songKey.replace(",", "")
			songScore = (100-rank)
			if songKey in songData:
				songData[songKey][date.strftime('%m/%d/%y')]=songScore
			else:
				songData[songKey]={date.strftime('%m/%d/%y'):songScore}
		numCharts+=1
		print numCharts
	date += oneDay

#insert a score of zero for every day a song was not on the chart
for songKey, dayRanks in songData.iteritems():
	for day in days:
		if day in dayRanks:
			ouputFile.write("%s,%d,%s\n" %(songKey,dayRanks[day],day))
		else:
			ouputFile.write("%s,%d,%s\n" %(songKey,0,day))

ouputFile.close()