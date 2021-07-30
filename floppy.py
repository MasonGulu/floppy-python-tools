import PySimpleGUI as sg
import os 

layout = [
    [sg.DropDown(["/dev/fd0", "/dev/fd1"],"/dev/fd0",key="device",size=(12,1),readonly=True), 
        sg.Button(button_text="Low Level Format", key="LLF", disabled=True),
        sg.Checkbox("Enable Destructive Options", key="EDO", enable_events=True)],
    [sg.Button("Make Image",key="ID",size=(10,1)),
        sg.Input(key="outputfile"), sg.FileSaveAs(size=(10,1))],
    [sg.Button("Write Disk",key="WD",size=(10,1),disabled=True),
        sg.Input(key="inputfile"), sg.FileBrowse(size=(10,1))]
]
destructive = [
    "LLF",
    "WD"
]
        # device = Floppy device to use
        # LLF = Low level format button
        # EDO = Enable destructive items checkbox
        # ID = Image Disk button
        # WD = Write disk image button
        # outputfile = Image file to create from disk
        # inputfile = Image to write to disk

win = sg.Window("Floppy Tools", layout)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        win.close()
        break
    for x in destructive:
        win[x].update(disabled=not values["EDO"])
    win.finalize()
    if event == "LLF":
        # Low level format
        print("Low level formatting "+values["device"])
        os.system("sudo fdformat "+values["device"])
    elif event == "ID":
        # Image disk
        print("Attempting to image the disk!")
        os.system("sudo dd if="+values["device"]+" of="+values["outputfile"])
    elif event == "WD":
        print("Attempting to write disk from image!")
        os.system("sudo dd if="+values["inputfile"]+" of="+values["device"])
        