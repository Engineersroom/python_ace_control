
import clr
import sys
import os
import time

# Connect to ACE using the remote control client
sys.path.append(r'C:\Program Files (x86)\Analog Devices\ACE\Client')
clr.AddReference('AnalogDevices.Csa.Remoting.Clients')
import AnalogDevices.Csa.Remoting.Clients as adrc
clientManager = adrc.ClientManager.Create()
client = clientManager.CreateRequestClient('localhost:2358')