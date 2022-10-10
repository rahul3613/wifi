import rssi

interface = 'wlan0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['NISER-AP']

ap_info = rssi_scanner.getAPinfo()

print(ap_info)
