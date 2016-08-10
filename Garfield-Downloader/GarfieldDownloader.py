#########################################
#		Author : Quentin Delvallet		#
#			Date : 10/08/2016			#
#########################################
#		Disclaimer : I do not own any	#
#		Garfield rights. This is just	#
#		a way to get the Garfield  		#
#		strips to read it offline.		#
#########################################
#				Contact : 				#
#		Quentin.delvallet@hotmail.fr	#
#########################################

### This script downloads every Garfield comic available on www.Garfield.com
### Creates a directory where this script is located and put every strips there.
### It separates each year for better clarity.
### It takes some times, please be patient.
### Approximative size is more than 1,60Go for around 14000 files. (Yeah that's a lot of strips)
### A few files are unavailable today.
### Starts with today's strip to the first one.

import urllib.request as urllib2
import time
from datetime import date, timedelta
import os

day = date.today()

'''Uncomment the next code line and change the date to start from a given date. 

Be careful, no zero allowed. 

Exemple : 
day = date(2000, 1, 1)  is valid
day = date(2000, 01, 01)  is not.

'''
#day = date(2000, 1, 1) 

server = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/"
comic = server + day.strftime('%Y/') + day.strftime('%Y-%m-%d') + ".gif"

for i in range(0, 100000):
	if(day == date(1978, 6, 18)) :
		print ("FIN!")
		break
	try:
		response = urllib2.urlopen(comic)
	except:
		print ("Error, please ignore. Resuming now...")
		day = day - timedelta(1)
		comic = server + day.strftime('%Y/') + day.strftime('%Y-%m-%d') + ".gif"
		continue
	try:
		if (response.getcode() == 200):
			html = response.read()
			print (day.strftime('%Y-%m-%d') + " : " + str(i))
			if not os.path.exists(day.strftime('%Y/')):
				os.makedirs(day.strftime('%Y/'))
			with open(day.strftime('%Y/') + day.strftime('%Y-%m-%d') + ".gif", 'wb+') as file_:
				file_.write(html)
				file_.close()
			day = day - timedelta(1)
			comic = server + day.strftime('%Y/') + day.strftime('%Y-%m-%d') + ".gif"
		else :
			print ("Error, unavailable comic. Resuming now...")
			break
	except :
		print("Error, please ignore. Resuming now...")
		continue