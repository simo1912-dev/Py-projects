import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key="todo") # text showed when you over the mouse over the instance
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetoca", 20))
# we should then include the instances created in the layout list
# when objects in same layout squarebracket => they are on the same row

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo_list = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions.write_todos(todo_list)
        case sg.WIN_CLOSED:
            break


window.close()

