from reactpy import component, html, run 

# Defining the component
@component
def HelloWorld():
    return html.h1("Hello, World!")

run(HelloWorld)