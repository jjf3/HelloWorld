#Created on Mon May 22 11:27:14 2023
#author: jjf3

import PySimpleGUI as sg

layout = [[sg.Text("This app was written in Python")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Test", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
