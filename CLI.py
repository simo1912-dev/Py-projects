import time

from functions import get_todos, write_todos
from time import strftime
now = strftime("%b %d, %Y %H:%M:%S")
print(f"Hello, we are the {now}")
while True:

    user_action = (input("type add or show, edit, complete or exit: ")).strip() # this strips the additional spaces

    if user_action.startswith('add'):
        todo = user_action[4:] # string slicing

        todo_list = get_todos()

        todo_list.append(todo + '\n')

        write_todos(todo_list)


    elif user_action.startswith('show'):

        todo_list = get_todos()
        for index, item in enumerate(todo_list):
             print(f"{index + 1}.{item}", end = "")

    elif user_action.startswith('edit'):
        # to give the user the opportunity to correct an error instead of just showing it and exiting
        try:
            number = int(user_action[5:]) - 1
            todo_list = get_todos()

            new_input = input("new to_do editted: ")
            todo_list[number] = new_input + "\n"

            write_todos(todo_list)

        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todo_list = get_todos()
            todo_to_remove = todo_list[number - 1].strip('\n')
            todo_list.pop(number - 1)
            write_todos(todo_list)

            print(f"Todo {todo_to_remove} was removed")
        except IndexError:
            print("wrong index")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("command not valid")

print("Byeee!")




