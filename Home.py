import streamlit
import function as y

streamlit.set_page_config(layout="wide")
todos=y.get_todos()
def newtodo():
    todo = streamlit.session_state['new'] + "\n"
    if todo:
        if todo not in todos:
            todos.append(todo)
            y.write(todos)
            streamlit.session_state['new']=''
        else:
            streamlit.warning("Item already exists!")

def complete():
    todo=y.get_todos()
    for n ,i in enumerate (todo):
        complted = streamlit.session_state[i]
        if complted == True:
            todos.pop(n)
            y.write(todos)

streamlit.title(" To-Do App")
streamlit.subheader("This is my todo App.")
streamlit.write("This app is to increase your productivity")
for i in todos:
    streamlit.checkbox(i,key=i)

streamlit.text_input(label=" ",placeholder="Enter the new todo",key="new",on_change=newtodo)
streamlit.button("Completed",key='com',on_click=complete)

