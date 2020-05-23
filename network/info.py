import network

# access point interface
ap_if = network.WLAN(network.AP_IF)
# will return false, it is turned off by default. Do ap_if.active(True) to active. You will see ESP32-... appear on your available Wi-FI connections. The default password is 'micropythoN'.
ap_if.active()
# get access point infos: (IP, Subnet Mask, Gateway, DNS)
ap_if.ifconfig()
# changing its credentials
ap_if.config(essid='network name', password='password')

# station interface
sta_if = network.WLAN(network.STA_IF)
# not active as default as well, so lets activate it
sta_if.active(True)
# scan available connections: the first element in each tuple is the SSID name, the third element is the channel number, and the fourth is the RSSI or signal strength indicator.
sta_if.scan()
# connect to the intended internet
sta_if.connect('your SSID', 'your Wi-Fi password')
# verify if its connected
sta_if.isconnected()
# get connection parameters
sta_if.ifconfig()