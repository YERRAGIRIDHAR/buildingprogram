from tkinter import *

# Create an empty Tkinter window
window = Tk()

def km_to_miles():
    miles=float(e1_value.get())*2.5# Get user value from input box and multiply by 2,5

    t1.delete("1.0", END)# Deletes the content of the Text box from start to END
    t1.insert(END,miles)# Fill in the text box with the value of multipled 


b1 = Button(window,text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)# The Label is placed in position 0, 0 in the window

e1_value=StringVar()# Create a special StringVar objec
e1=Entry(window, textvariable=e1_value)# Create an Entry box for users to enter the value
e1.grid(row=0, column=1)

# Create three empty text boxe t1
t1=Text(window, height=2, width=20)
t1.grid(row=0, column=2)

# This makes sure to keep the main window open
window.mainloop()   