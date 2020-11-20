"""
Updated version of my previous GUI built
Includes trig functions (sin, cos, tan)
Exponents and logarithmic functions
"""

from tkinter import *
import math

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
    
    def press_button(self, num):
        self.eq = False
        text = text_box.get()
        temp = str(num) 
        if self.new_num:
            self.current = temp
            self.new_num = False 
        else:
        #ensure only one decimal place:
            if temp == ".":
                if temp in text:
                    return
            self.current = text + temp
        #display updated text 
        self.display(self.current)
    # for the = button:
    def calc_total(self):
        try:
            self.eq = True
            self.current = float(self.current)
            if self.op_pending == True:
                self.operations()
            else:
                self.total = float(text_box.get()) 
        except ZeroDivisionError:
            text_box.insert(0, "Error!")
            return None
    
    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def operations(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "xpowery":
            self.total = self.total ** self.current
        self.new_num = True
        self.op_pending = False 
        self.display(self.total)
    #some operations needed their own function especially when calc_total is not needed:
    def pi(self):
        self.eq = False 
        self.current = math.pi
        self.display(self.current)

    def sin(self):
        self.eq = False 
        self.current = math.sin(math.radians(float(text_box.get())))
        self.display(self.current)

    def cos(self):
        self.eq = False 
        self.current = math.cos(math.radians(float(text_box.get())))
        self.display(self.current)

    def tan(self):
        self.eq = False 
        self.current = math.tan(math.radians(float(text_box.get())))
        self.display(self.current)
    #the try...except method is used to handle mathematical errors without disrupting the program:
    def e_x(self):
        try:
            self.eq = False 
            self.current = math.exp(float(text_box.get()))
            self.display(self.current)
        except OverflowError:
            self.current = "Overflow Error"
            self.display(self.current)

    def ln(self):
        try:
            self.eq = False 
            self.current = math.log(float(text_box.get()))
            self.display(self.current)
        except ValueError:
            self.current = "Error!"
            self.display(self.current)

    def xroot2(self):
        self.eq = False 
        self.current = float(text_box.get())**2 
        self.display(self.current)

    def sqrtx(self):
        try:
            self.eq = False 
            self.current = math.sqrt(float(text_box.get()))
            self.display(self.current)
        except ValueError:
            self.current = "Error!"
            self.display(self.current) 

    def log10(self):
        try:
            self.eq = False 
            self.current = math.log(float(text_box.get()), 10)
            self.display(self.current)
        except ValueError:
            self.current = "Error!"
            self.display(self.current)

    def factoiral(self):
        self.current = int(text_box.get())
        self.current = math.factorial(self.current) 
        self.display(self.current)

    def inverse(self):
        self.eq = False
        self.current = 1 / float(text_box.get())
        self.display(self.current)

    def solve(self, s):
        self.current = float(self.current)
        if self.op_pending:
            self.operations()
        elif not self.eq:
            self.total = self.current
        self.new_num = True 
        self.op_pending = True
        self.op = s 
        self.eq = False

    def clear(self):
        self.eq = False 
        self.current = "0"
        self.display(0)
        self.new_num = True 
    
    def clear_all(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False 
        self.current = -(float(text_box.get()))
        self.display(self.current)

yay_science = Calculator()
root = Tk()

root.title("Scientific Calculator")
root.geometry("755x345")
root.configure(background="grey")
text_box = Entry(root, justify=RIGHT, width=25, font="Times 16 bold", bd=10)
text_box.grid(row=1, columnspan=5, ipadx=70, ipady=2)
text_box.insert(0, "0")
image = PhotoImage(file = "thank_u_tam.png")
reimage = image.subsample(40, 40)

#creation of all buttons go here:
button_7 = Button(root, text='7', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(7))
button_7.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

button_8 = Button(root, text='8', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(8))
button_8.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

button_9 = Button(root, text='9', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(9))
button_9.grid(row=2, column=2, padx=2, pady=2, sticky="ew")

button_4 = Button(root, text='4', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(4))
button_4.grid(row=3, column=0, padx=2, pady=2, sticky="ew")

button_5 = Button(root, text='5', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(5))
button_5.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

button_6 = Button(root, text='6', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(6))
button_6.grid(row=3, column=2, padx=2, pady=2, sticky="ew")

button_1 = Button(root, text='1', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(1))
button_1.grid(row=4, column=0, padx=2, pady=2, sticky="ew")

button_2 = Button(root, text='2', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(2))
button_2.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

button_3 = Button(root, text='3', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(3))
button_3.grid(row=4, column=2, padx=2, pady=2, sticky="ew")

button_0 = Button(root, text='0', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button(0))
button_0.grid(row=5, columnspan=2, padx=2, pady=2, sticky="ew")

button_dot = Button(root, text=' . ', font='helvetica 14 bold', fg='black', bg='steelblue1', bd=6, height=2,width=6, command=lambda: yay_science.press_button('.'))
button_dot.grid(row=5, column=2, padx=2, pady=2, sticky="ew")

button_div = Button(root, text=' / ', font='helvetica 14 bold', fg='black', bg='orange', bd=6, height=2, width=6, command=lambda: yay_science.solve("divide"))
button_div.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

button_mult = Button(root, text=' x ', font='helvetica 14 bold', fg='black', bg='orange', bd=6, height=2, width=6, command=lambda: yay_science.solve("multiply"))
button_mult.grid(row=3, column=3, padx=2, pady=2, sticky="ew")
# the "-" is so tiny...
button_minus = Button(root, text=' -- ', font='helvetica 14 bold', fg='black', bg='orange', bd=6, height=2, width=6, command=lambda: yay_science.solve("subtract"))
button_minus.grid(row=4, column=3, padx=2, pady=2, sticky="ew")

button_add = Button(root, text=' + ', font='helvetica 14 bold', fg='black', bg='orange', bd=6, height=2, width=6, command=lambda: yay_science.solve("add"))
button_add.grid(row=5, column=3, padx=2, pady=2, sticky="ew")

button_ac = Button(root, text="AC", font='helvetica 14 bold', fg="black", bg="orange red", bd=6, height=2, width=6, command=yay_science.clear_all)
button_ac.grid(row=2, column=4, padx=2, pady=2, sticky="ew")

button_clear = Button(root, text="C", font='helvetica 14 bold', fg="black", bg="yellow", bd=6, height=2, width=6, command=yay_science.clear)
button_clear.grid(row=3, column=4, padx=2, pady=2, sticky="ew")

button_neg = Button(root, text="+/-", font='helvetica 14 bold', fg="black", bg="orange", bd=6, height=2, width=6, command=yay_science.sign)
button_neg.grid(row=4, column=4, padx=2, pady=2, sticky="ew")

button_equal = Button(root, text=" = ", font='helvetica 14 bold', fg="black", bg="orange", bd=6, height=2, width=6, command=yay_science.calc_total)
button_equal.grid(row=5, column=4, padx=2, pady=2, sticky="ew")

button_pi = Button(root, text="π", font='helvetica 14 bold', fg="black", bg="seagreen1", bd=6, height=2, width=6, command=yay_science.pi)
button_pi.grid(row=2, column=5, padx=2, pady=2, sticky="ew")

button_sin = Button(root, text="sin", font='helvetica 14 bold', fg="black", bg="seagreen1", bd=6, height=2, width=6, command=yay_science.sin)
button_sin.grid(row=3, column=5, padx=2, pady=2, sticky="ew")

button_cos = Button(root, text="cos", font='helvetica 14 bold', fg="black", bg="seagreen1", bd=6, height=2, width=6, command=yay_science.cos)
button_cos.grid(row=4, column=5, padx=2, pady=2, sticky="ew")

button_tan = Button(root, text="tan", font='helvetica 14 bold', fg="black", bg="seagreen1", bd=6, height=2, width=6, command=yay_science.tan)
button_tan.grid(row=5, column=5, padx=2, pady=2, sticky="ew")

button_x2 = Button(root, text="x^2", font='helvetica 14 bold', fg="black", bg="seagreen2", bd=6, height=2, width=6, command=yay_science.xroot2)
button_x2.grid(row=2, column=6, padx=2, pady=2, sticky="ew")

button_xy = Button(root, text="x^y", font='helvetica 14 bold', fg="black", bg="seagreen2", bd=6, height=2, width=6, command=lambda: yay_science.solve("xpowery"))
button_xy.grid(row=3, column=6, padx=2, pady=2, sticky="ew")
#buttons with images do not need height, width argument for button size, rather those become size of image in pixels:
button_sqrt = Button(root, image=reimage, fg="black", bg="seagreen2", bd=6, command=yay_science.sqrtx)
button_sqrt.grid(row=4, column=6, padx=2, pady=2, sticky="ew")

button_fact = Button(root, text="x!", font='helvetica 14 bold', fg="black", bg="seagreen2", bd=6, height=2, width=6, command=yay_science.factoiral)
button_fact.grid(row=5, column=6, padx=2, pady=2, sticky="ew")

button_e = Button(root, text="e^x", font='helvetica 14 bold', fg="black", bg="seagreen3", bd=6, height=2, width=6, command=yay_science.e_x)
button_e.grid(row=2, column=7, padx=2, pady=2, sticky="ew")

button_ln = Button(root, text="ln", font='helvetica 14 bold', fg="black", bg="seagreen3", bd=6, height=2, width=6, command=yay_science.ln)
button_ln.grid(row=3, column=7, padx=2, pady=2, sticky="ew")

button_log = Button(root, text="log10", font='helvetica 14 bold', fg="black", bg="seagreen3", bd=6, height=2, width=6, command=yay_science.log10)
button_log.grid(row=4, column=7, padx=2, pady=2, sticky="ew")

button_inv = Button(root, text="1/x", font='helvetica 14 bold', fg="black", bg="seagreen3", bd=6, height=2, width=6, command=yay_science.inverse)
button_inv.grid(row=5, column=7, padx=2, pady=2, sticky="ew")

if __name__ == '__main__':
    root.mainloop()

