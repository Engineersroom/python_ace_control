import clr
import sys
import os
import time
from pytictoc import TicToc

t = TicToc()

#Connect to ACE using the remote control client
sys.path.append(r'C:\Program Files (x86)\Analog Devices\ACE\Client')
clr.AddReference('AnalogDevices.Csa.Remoting.Clients')
clr.AddReference('AnalogDevices.Csa.Remoting.Contracts')
import AnalogDevices.Csa.Remoting.Clients as adrc
import AnalogDevices.Csa.Remoting.Contracts as adrck

clientManager = adrc.ClientManager.Create()
client = clientManager.CreateRequestClient('localhost:2357')
client.AddHardwarePlugin('AD9164-FMC-EBZ')
#Subsystem_1.AD9164-FMC-EBZ.ADF4355: Evaluation.Control
#client.NavigateToPath('Root::System.Subsystem_1.AD9208-3000EBZ.AD9208.AD9208 Analysis')
client.set_ContextPath(r'\System\Subsystem_1\AD9164-FMC-EBZ\AD9164')
client.NavigateToPath('Root::System.Subsystem_1.AD9164-FMC-EBZ.AD9164')
t.tic()

for i in range(1,500):
    client.RawWriteRegister(2048,1)
    i = i + 1
t.toc()
elapsed_time =t.elapsed
print(f"Elapsed time: {elapsed_time:.3f} seconds")



# adrc
# #Navigate to initialization wizard and set to one converter
# client.set_ContextPath(r'\System\Subsystem_1\AD9164-FMC-EBZ\AD9164')
# #client.NavigateToPath('Root::System.Subsystem_1.AD9164-FMC-EBZ.AD9164')
# client.SetWizardParameter('initwizard','jtx_m_cfg','0')
# time.sleep(2)
# client.ApplyWizardSettings('initwizard','Apply')

# #Navigate to capture wizard and set the number of samples to 500MSamples (1GB)
# client.NavigateToPath('Root::System.Subsystem_1.AD9208-3000EBZ.AD9208.AD9208 Analysis')
# client.SetWizardParameter('captureWizard','validatedSampleCount',str(2**29))

# #Divert the output of the ADS7V2/ADS8V1 to a file
# client.AsyncRawCaptureToFile(os.path.expanduser('~\Desktop\largeCapture.bin'),'test','false','true')

# # Wait up to 5secs for the capture to complete
# client.WaitOnRawCaptureToFile('5000','test','false',os.path.expanduser('~\Desktop\largeCapture.bin'))
