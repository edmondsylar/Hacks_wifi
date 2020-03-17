from os import system
from time import sleep

interface = input('Interface:: ')
if interface == 'wlan0':
	monitor_inteface = 'wlan0mon'
	print('switching to monitor mode on interface {}'.format(monitor_inteface))
	sleep(5)
	system('sudo airmon-ng start {}'.format(interface))
	sleep(2)
	system('sudo airodump-ng {}'.format(monitor_inteface))
	sleep(10)
	system('sudo airmon-ng stop {}'.format(monitor_inteface))

elif interface == "":
	print('No interface provided.....')
else:
	print('Unrecognised Interface....')