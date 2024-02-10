def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list
    of to-do items"""

    with open(filepath, "r") as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todo_list_arg, filepath="todos.txt"):  # this function modifies a file but doesnt return anything
    """ Write the to-do list in the text files"""
    with open(filepath, 'w') as file:
        file.writelines(todo_list_arg)