import os
from time import sleep

# monitor = input('Monitoring Interface:: ')
# bssid = input('BSSID:: ')
interface = input('Interface:: ')
class hacker_ways:
	def __init__(self):
		pass

	def check_available_networks(self):
		os.system('airodump-ng {}'.format(monitor_inteface))
		sleep(20)
		get_network_specified()


	def get_network_specified(self):
		bssid = input('BSSID:: ')
		if bssid != "":
			os.system('airodump-ng {} --bssid {}'.format(monitor_inteface, bssid))
			sleep(10)


	def enter_monitor_mode(self):
		os.system('airmon-ng start {}'.format(interface))
		if interface == 'wlan0':
			monitor_inteface = 'wlan0mon'
			check_available_networks()

		elif interface != 'wlan0':
			print ('It seems you entered a wrong inteface name..')
			# os.system('a')
			pass

user = hacker_ways()
user.enter_monitor_mode()