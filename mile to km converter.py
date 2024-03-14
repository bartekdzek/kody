import tkinter

window = tkinter.Tk()
window.title("Miles to kilometer converter")


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles", font =("Comic Sans MS", 15))
miles.grid(column=2, row= 0)

km = tkinter.Label(text="Km", font =("Comic Sans MS", 15))
km.grid(column=2, row= 1)

equal_label = tkinter.Label(text="is equal to", font =("Comic Sans MS", 15))
equal_label.grid(column=0, row=1)


km_value = tkinter.Label(text="0", font =("Comic Sans MS", 15))
km_value.grid(column=1, row= 1)




def button_clicked():
    input_val = (input.get())
    input_val = float(input_val)
    km_val = (input_val) * 1.609344
    km_value.config(text=km_val)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()