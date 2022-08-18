from tkinter import *


def miles_to_km():
    result = float(entry.get()) * 1.60934
    label_result.config(text=result)


window = Tk()
window.title("From miles to km")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

entry = Entry(width=20)
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()