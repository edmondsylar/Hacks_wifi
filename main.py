import os
from time import sleep

class Mac_Spoof:
	def __init__(self):
		int_check = os.system('ifconfig')
		check = int_check.split(' ')
		for val in check:
			if val == 'wlan0':
				interface = 'wlan0'
			else:
				continue


	def monitor_mode(self):
		pass

Mac_Spoof()