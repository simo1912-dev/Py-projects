import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt") as file:
        pass

sg.theme("DarkPurple4") # we can get the theme names from the internet
clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key="todo") # text showed when you hover the mouse over the instance
add_button = sg.Button("Add")
List_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
Complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App',
                   layout=[ [clock],
                           [label],
                           [input_box, add_button],
                           [List_box, edit_button, Complete_button],
                           [exit_button]],
                   font=("Helvetoca", 20))
# we should then include the instances created in the layout list
# when objects in same layout squarebracket => they are on the same row

while True:
    event, values = window.read(timeout=10) # this will allow the loop to run every 10ms so that the clock
    # can be displayed and updated
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todo_list = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions.write_todos(todo_list)
            window['todos'].update(values=todo_list)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todo_list = functions.get_todos()
                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo
                functions.write_todos(todo_list)
                window['todos'].update(values=todo_list)
            except IndexError:
                sg.popup("Please select a todo first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todo_list = functions.get_todos()
                todo_list.remove(todo_to_complete)
                functions.write_todos(todo_list)
                window['todos'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a todo first", font=("Helvetica", 20))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break




window.close()

