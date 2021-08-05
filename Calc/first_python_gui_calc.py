from tkinter import *

#Sorry about the spaghetti code I was just experimenting

window = Tk()
window.geometry("500x500")
window.title("El calculator")
window.configure(bg="#636262")
first_number = 0.0

#Colors
dark_grey = "#444444"
white = "#fff"


first_num_label = Label(window, text = "", font="Calibra 40", bg = dark_grey,
    fg=white)
first_num_label.place(anchor="sw", relwidth= 0.6, relheight=0.2, rely=0.4,
     relx=0.2)
operator_label = Label(window, text = "", bg = dark_grey, fg=white)
operator_label.place(anchor="sw", relwidth = 0.2, relheight=0.2, rely=0.4,
    relx= 0.8)




number_entry = Entry(window, font="Calibra 40", justify="right", bg=dark_grey, fg = white)

number_entry.config(highlightbackground = white)
number_entry.place(relwidth=0.8, relheight=0.18)

#Function for buttons
def button_click(number):
    inn = number_entry.get()
    ind = len(inn)
    ind += 1
    number_entry.insert(ind, number)

def clear_entry():
    number_entry.delete(0, len(number_entry.get()))

def operator(operated):
    operator_label["text"] = operated

    first_num_label["text"] = float(number_entry.get())
    number_entry.delete(0, len(number_entry.get()))

    return first_number

def solve(first_num, second_num):
    answer = float(first_num)

    if(operator_label["text"] == "+"):
        answer += float(second_num)

    elif(operator_label["text"] == "-"):
        answer -= float(second_num)

    entry_length = len(number_entry.get())
    number_entry.delete(0, entry_length)

    number_entry.insert(0, answer)



button9 = Button(window, fg = white, bg = dark_grey, text = "9", command=lambda: button_click(9))
button8 = Button(window, fg = white, bg = dark_grey, text = "8", command=lambda: button_click(8))
button7 = Button(window, fg = white, bg = dark_grey, text = "7", command=lambda: button_click(7))
button6 = Button(window, fg = white, bg = dark_grey, text = "6", command=lambda: button_click(6))
button5 = Button(window, fg = white, bg = dark_grey, text = "5", command=lambda: button_click(5))
button4 = Button(window, fg = white, bg = dark_grey, text = "4", command=lambda: button_click(4))
button3 = Button(window, fg = white, bg = dark_grey, text = "3", command=lambda: button_click(3))
button2 = Button(window, fg = white, bg = dark_grey, text = "2", command=lambda: button_click(2))
button1 = Button(window, fg = white, bg = dark_grey, text = "1", command=lambda: button_click(1))
buttonclear=Button(window, fg = white, bg = dark_grey, text = "C", command= clear_entry)
buttonadd = Button(window, fg = white, bg = dark_grey, text = "+", command=lambda: operator("+"))
buttonminus = Button(window, fg = white, bg = dark_grey, text = "-", command=lambda: operator("-"))
buttonsolve = Button(window, fg = white, bg = dark_grey, text = "=", command=lambda:
    solve(first_num_label["text"], number_entry.get()))

#Making placements
#First column
button1.place(anchor="sw", rely=1.0, relheight=0.2, relwidth=0.2)
button4.place(anchor="sw", rely=0.8, relheight=0.2, relwidth=0.2)
button7.place(anchor="sw", rely=0.6, relheight=0.2, relwidth=0.2)
buttonclear.place(anchor="sw", rely=0.4, relheight=0.2, relwidth=0.2)

#Second column
button2.place(anchor="sw", rely=1.0, relheight=0.2, relwidth=0.2, relx = 0.2)
button5.place(anchor="sw", rely=0.8, relheight=0.2, relwidth=0.2, relx = 0.2)
button8.place(anchor="sw", rely=0.6, relheight=0.2, relwidth=0.2, relx = 0.2)

#Third column
button3.place(anchor="sw", rely=1.0, relheight=0.2, relwidth=0.2, relx = 0.4)
button6.place(anchor="sw", rely=0.8, relheight=0.2, relwidth=0.2, relx = 0.4)
button9.place(anchor="sw", rely=0.6, relheight=0.2, relwidth=0.2, relx = 0.4)

#Fourth column

buttonadd.place(anchor="sw", rely=1.0, relheight=0.2, relwidth=0.2, relx = 0.6)
buttonminus.place(anchor="sw", rely=0.8, relheight=0.2, relwidth=0.2, relx = 0.6)
buttonsolve.place(anchor="sw", rely=0.6, relheight=0.2, relwidth=0.2, relx = 0.6)

window.mainloop()
