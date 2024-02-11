import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key="todo") # text showed when you over the mouse over the instance
add_button = sg.Button("Add")
List_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [List_box, edit_button]],
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
            window['todos'].update(values=todo_list)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todo_list = functions.get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.write_todos(todo_list)
            window['todos'].update(values=todo_list)
        case 'todos':
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break




window.close()

