import time
import os
import datetime
from playsound import playsound


def check(atime):
	if len(atime) == 1:
		if atime[0] < 24 and atime[0] >= 0:
			return True
	if len(atime) == 2: # HH:MM
		if atime[0] < 24 and atime[0] >= 0 and \
		   atime[1] < 60 and atime[1] >= 0:
			return True
	elif len(atime) == 3: # HH:MM:SS
		if atime[0] < 24 and atime[0] >= 0 and \
		   atime[1] < 60 and atime[1] >= 0 and \
		   atime[2] < 60 and atime[2] >= 0:
			return True
	else:
	    return False

print("Set the Alarm Time (Format: HH:MM or HH:MM:SS) : ")

while True:
	alarm_input=input(">> ")
	try:
		atime=[int(n) for n in alarm_input.split(":")]
		if check(atime):
			break
		else:
			raise ValueError
	except ValueError:
		print("ERROR: Enter in HH:MM or HH:MM:SS format")

#convert to seconds
seconds_hms = [3600, 60, 1]
alarmseconds = sum([a*b for a,b in zip(seconds_hms[:len(atime)], atime)])

# Get the current time of day in seconds
now = datetime.datetime.now()
currenttime = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until alarm goes off
diff = alarmseconds - currenttime

#next day
if diff < 0:
	diff+= 86400

# Display amount of time
print("Alarm set to go off in:",datetime.timedelta(seconds=diff))

time.sleep(diff)

print("Wake Up!")
playsound('alarm.mp3')
