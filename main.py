# Separate file containing the main code

import lab_pc_module

#lab_pc_module is the module containing the class
#LabPC is the class in this module, we have imported it over here

lpc= lab_pc_module.LabPC("1","Windows 7","Running") # Creating some sample objects
lpc2=lab_pc_module.LabPC("2","MacOS 10.12","Running")
lpc3=lab_pc_module.LabPC("3","Windows 10","Damaged")  

while 1<2: # Calling the main menu repeatedly
    lab_pc_module.LabPC.main_menu()  
