import PySimpleGUI as sg 
import pyttsx3


layout = [ [sg.Text("Enter text to speak")],
            [sg.Input()],
            [sg.OK(), sg.Cancel()] ]


window = sg.Window('TEXT-TO-SPEECH').Layout(layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    if event in ('OK'):
        engine = pyttsx3.init()
        engine.say(values[0])
        engine.runAndWait()
        break

# read window

button, values = window.Read()