import time
import os
import datetime
from playsound import playsound

def check(time):
	if len(time) == 1:
		if time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(time) == 2: # [Hour:Minute] Format
		if time[0] < 24 and alarm_time[0] >= 0 and \
		   time[1] < 60 and alarm_time[1] >= 0:
			return True
	elif len(time) == 3: # [Hour:Minute:Second] Format
		if time[0] < 24 and alarm_time[0] >= 0 and \
		   time[1] < 60 and alarm_time[1] >= 0 and \
		   time[2] < 60 and alarm_time[2] >= 0:
			return True
	else:
    return False

print("Set the Alarm Time (Format: HH:MM or HH:MM:SS) : ")

while True:
	alarm_input = input(">> ")
	try:
		time = [int(n) for n in alarm_input.split(":")]
		if check_alarm_input(alarm_time):
			break
		else:
			raise ValueError
	except ValueError:
		print("ERROR: Enter time in HH:MM or HH:MM:SS format")
    
#convert to seconds
seconds_hms = [3600, 60, 1]
alarmseconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get the current time of day in seconds
now = datetime.datetime.now()
currenttime = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until alarm goes off
diff = alarmseconds - currenttime

#next day if alarm is negative
if time_diff_seconds < 0:
	time_diff_seconds += 86400

time.sleep(diff)

print("Wake Up!")
playsound('alarm.mp3')
