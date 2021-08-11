from tkinter import *
from tkinter import messagebox


class Simple_Calc(Tk):
    """docstring for Simple_Calc."""

    def __init__(self):
        super().__init__()

        #Window
        background_color = "#082032"
        self.iconphoto(False, PhotoImage(file = "icon.png"))


        #self.geometry("500x600")
        #self.resizable(False, False)
        self.title("Simple Calculator")
        self.configure(bg = background_color)

        #Entry
        entry_font = "Calibra 20"
        widget_bg = "#2C394B"
        widget_fg = "#fff"
        self.number_entry = Entry( fg = widget_fg, bg = widget_bg,
        font = entry_font, width=18, justify = RIGHT)
        self.number_entry.grid(row=0, column = 0, columnspan = 5, padx = 5,
        pady = 20)
        self.operator = ""
        self.first_num = 0.0
        self.second_num = 0.0

        #Buttons
        button_pady = 20
        button_padx = 20
        #First column
        button_font = "Calibra 20"
        button0 = Button(self, bg = widget_bg, fg = widget_fg, text = "0",
        width = 8, height = 4, command = lambda: self.number_click("0"))

        button0.grid(row=5, column=0)
        button1 = Button(self, bg = widget_bg, fg = widget_fg, text = "1",
        width = 8, height = 4, command = lambda: self.number_click("1"))
        button1.grid(row=4, column=0)
        button4 = Button(self, bg = widget_bg, fg = widget_fg, text = "4",
        width = 8, height = 4, command = lambda: self.number_click("4"))
        button4.grid(row=3, column=0)
        button7 = Button(self, bg = widget_bg, fg = widget_fg, text = "7",
        width = 8, height = 4, command = lambda: self.number_click("7"))
        button7.grid(row=2, column=0)

        #Second column
        button_dot = Button(self, bg = widget_bg, fg = widget_fg, text = ".",
        width = 8, height = 4, command = lambda: self.number_click("."))
        button_dot.grid(row=5, column = 1)
        button_2 = Button(self, bg = widget_bg, fg = widget_fg, text = "2",
        width = 8, height = 4, command = lambda: self.number_click("2"))
        button_2.grid(row=4, column = 1)
        button_5 = Button(self, bg = widget_bg, fg = widget_fg, text = "5",
        width = 8, height = 4, command = lambda: self.number_click("5"))
        button_5.grid(row=3, column = 1)
        button_8 = Button(self, bg = widget_bg, fg = widget_fg, text = "8",
        width = 8, height = 4, command = lambda: self.number_click("8"))
        button_8.grid(row=2, column = 1)

        #Third Row
        button_dot = Button(self, bg = widget_bg, fg = widget_fg, text = "=",
        width = 8, height = 4, command = self.solve_equation)
        button_dot.grid(row=5, column = 2)
        button_2 = Button(self, bg = widget_bg, fg = widget_fg, text = "3",
        width = 8, height = 4, command = lambda: self.number_click("3"))
        button_2.grid(row=4, column = 2)
        button_5 = Button(self, bg = widget_bg, fg = widget_fg, text = "6",
        width = 8, height = 4, command = lambda: self.number_click("6"))
        button_5.grid(row=3, column = 2)
        button_8 = Button(self, bg = widget_bg, fg = widget_fg, text = "9",
        width = 8, height = 4, command = lambda: self.number_click("9"))
        button_8.grid(row=2, column = 2)

        #Fourth Row
        button_plus = Button(self, bg = widget_bg, fg = widget_fg, text = "+",
        width = 8, height = 4, command = lambda: self.set_operator("+"))
        button_plus.grid(row=5, column = 3)
        button_minus = Button(self, bg = widget_bg, fg = widget_fg, text = "-",
        width = 8, height = 4, command = lambda: self.set_operator("-"))
        button_minus.grid(row=4, column = 3)
        button_multiply = Button(self, bg = widget_bg, fg = widget_fg, text = "x",
        width = 8, height = 4, command = lambda: self.set_operator("x"))
        button_multiply.grid(row=3, column = 3)
        button_divide = Button(self, bg = widget_bg, fg = widget_fg, text = "/",
        width = 8, height = 4, command = lambda: self.set_operator("/"))
        button_divide.grid(row=2, column = 3)

        #Fifth Row
        button_clear = Button(self, bg = widget_bg, fg = widget_fg, text = "Clear",
        width = 38, height = 4, command = self.entry_clear)
        button_clear.grid(row=6, column= 0, columnspan = 4)

    def number_click(self, number):

        current_num_length = len(self.number_entry.get().strip())
        if(current_num_length < 18):
            self.number_entry.insert(current_num_length, number)

    def set_operator(self, operator):
        try:
            self.first_num = float(self.number_entry.get())
            self.operator = operator
            self.entry_clear()
        except ValueError:
            messagebox.showwarning(title="Value Error", message="Sorry that is " +
            "not the right type please enter a number.")
            self.entry_clear()


    def entry_clear(self):
        self.number_entry.delete(0, "end")

    def solve_equation(self):
        op = self.operator
        second_num = float(self.number_entry.get().strip())
        answer = 0.0
        if(op == "+"):
            answer = self.first_num + second_num
        elif(op == "-"):
            answer = self.first_num - second_num
        elif(op == "x"):
            answer = self.first_num * second_num
        elif(op == "/"):
            answer = self.first_num / second_num

        self.first_num = answer
        self.entry_clear()
        self.number_entry.insert(0, answer)










if __name__ == '__main__':
    calc = Simple_Calc();
    calc.mainloop()
