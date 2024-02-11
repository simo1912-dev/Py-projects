import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do") # text showed when you over the mouse over the instance
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])  # we should then include the instances created in the layout list
    # when objects in same layout squarebracket => they are on the same row

window.read()
window.close()

