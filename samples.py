import os
from time import sleep

delay = int(input('Delay:: '))

print ('Switched to monitoring mode on interface wlan0mon')
for i in range (0, delay):
	print(i, 'secs')
	sleep(1)
	os.system('clear')

# os.system('sudo airmon-ng stop wlan0mon')