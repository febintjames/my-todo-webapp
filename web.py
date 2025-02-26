import streamlit as x
import function as y

todos=y.get_todos()
def newtodo():
    todo=x.session_state['new'] +"\n"
    todos.append(todo)
    y.write(todos)


x.title(" To-Do App")
x.subheader("This is my todo App.")
x.write("This app is to increase your productivity")
for n,i in enumerate(todos):
    check=x.checkbox(i,key=i)
    if check == True:
        todos.pop(n)
        y.write(todos)




x.text_input(label=" ",placeholder="Enter the new todo",key="new",on_change=newtodo)
x.button("Exit")
