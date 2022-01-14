# import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()

# serialObject = serial.Serial()

# portList= []

# for oneport in ports:
#     portList.append(str(oneport))
#     print(str(oneport))

from tkinter import *
import serial.tools.list_ports
import functools

#port_Inisiallation 
ports = serial.tools.list_ports.comports()
serialObject= serial.Serial("COM5")

def initComport(index):
    currentPort = str(ports[index])
    currentPortVar= str(currentPort.split(" ")[0])
    # print(currentPortVar)
    serialObject.port = currentPortVar
    serialObject.baudrate=9600
    serialObject.open()

#gui_code_here
tk = Tk()
tk.config(bg = "grey")

for oneport in ports:
    comButton = Button(tk, text=oneport, width=45, height=1 , command= functools.partial(initComport, index= ports.index(oneport)))
    comButton.grid(row=ports.index(oneport), column=0)

dataCanvas = Canvas(tk, bg = "white", width=600, height=400)
dataCanvas.grid(row=0, column=1, rowspan=100)


vsb = Scrollbar(tk, orient="vertical", command=dataCanvas.yview)
vsb.grid(row=0,column=2, rowspan=100, sticky="ns")

dataCanvas.config(yscrollcommand= vsb.set)

dataFrame= Frame(dataCanvas, bg="white")

dataCanvas.create_window((10,0), window= dataFrame, anchor="nw")

def checkSerialPort():
    if serialObject.isOpen() and serialObject.in_waiting:
        recentRacket = serialObject.readline()
        recentRacketString = recentRacket.decode("utf").rstrip("\n")
        Label(dataFrame, text = recentRacketString, bg="white").pack()
    
    


#Eternally_Run
while(True):
    tk.update()
    checkSerialPort()
    dataCanvas.config(scrollregion=dataCanvas.bbox("all"))


