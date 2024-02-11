import streamlit as st

import functions
import functions as fc

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_list.append(todo)
    functions.write_todos(todo_list)

# the python script will be executed with every loading of the page/url in terminal...

todo_list = fc.get_todos()


st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("this app will increase your productivity!!")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Enter a todo:",
              on_change=add_todo, key='new_todo')

#st.session_state
# to deploy this web app we should only have standalone py
#project: (webapp related files) only
