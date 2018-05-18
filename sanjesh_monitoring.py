#In the name of Allah
#Author: SAD

import urllib2
import hashlib
import time
import datetime
import vlc


url = 'http://sanjesh.org/'
response = urllib2.urlopen(url)
web1 = response.read().split("bodyCenter")[1].split("bodyAreaBottom")[0]
hash1 = hashlib.sha224(web1).hexdigest()

starttime=time.time()

while True:
	response = urllib2.urlopen(url)
	web2 = response.read().split("bodyCenter")[1].split("bodyAreaBottom")[0]
	hash2 = hashlib.sha224(web2).hexdigest()
	currentDT = datetime.datetime.now()
	if hash1 == hash2 :
		print str(currentDT)
		print "Results coming soon... please wait."
		print "----------------------"
	else:
		print str(currentDT)
		print "Results just released! Good luck :D"
		print "*****************************************************"
		player = vlc.MediaPlayer("music.mp3")
		player.play()	
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))