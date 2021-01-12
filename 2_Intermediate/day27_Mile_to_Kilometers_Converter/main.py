# import tkinter
#
# window = tkinter.Tk()
# window.title("Mile to Km Converter")
# window.minsize()
# window.config(padx=20, pady=20)
#
# # Gets the requested values of the height and width.
# windowWidth = window.winfo_reqwidth()
# windowHeight = window.winfo_reqheight()
#
# # Gets the requested values of the height and width.
# positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
# positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
#
# # Positions the window in the center of the page.
# window.geometry("+{}+{}".format(positionRight, positionDown))
#
# # Label
# label_1 = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
# label_1.grid(column=0, row=1)
#
# label_2 = tkinter.Label(text="0", font=("Arial", 24, "bold"))
# label_2.grid(column=1, row=1)
#
# label_3 = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
# label_3.grid(column=2, row=0)
#
# label_4 = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
# label_4.grid(column=2, row=1)
#
# # Button
#
#
# def calculate():
#     new_text = int(input.get())
#     new_text *= 1.60934
#     label_2.config(text=new_text)
#
#
# button = tkinter.Button(text="Calculate", command=calculate)
# button.grid(column=1, row=2)
#
# # Entry
# input = tkinter.Entry(width=10)
# input.insert(index=0, string="0")
# input.grid(column=1, row=0)
#
# window.mainloop()

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round((miles * 1.609), 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
