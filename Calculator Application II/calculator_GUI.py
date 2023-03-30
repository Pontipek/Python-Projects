from tkinter import *
def enter(number):
    global user_input
    user_input = user_input + str(number)
    input_display.set(user_input)
def calculate():
    try:
        global user_input
        input_display.set(str(eval(user_input)))
        user_input = ""
    except:
        input_display.set("0")
        user_input = ""
def percentage():
    try:
       global user_input
       input_display.set(str(int(user_input)/100))
       user_input = ""
    except:
        input_display.set("0")
        user_input = ""
def reset():
    global user_input
    user_input = ""
    input_display.set("0")

calculator = Tk()
calculator.title("IOS Calculator")
calculator.geometry("300x400")
calculator.configure(background="black")

user_input = ""

input_display = StringVar()
input_display.set("0")

result = Label(calculator, textvariable=input_display, width= 400, height=5, fg="white", background="grey")
result.pack()

Button(calculator, text="AC", height=3, width=8, background="grey", bd=1, fg="black",
       command= lambda : reset()).place(x=5, y=100)
Button(calculator, text="MOD", height=3, width=8, background="grey", bd=1, fg="black",
       command=lambda: enter("%")).place(x=80, y=100)
Button(calculator, text="%", height=3, width=8, background="grey", bd=1, fg="black",
       command=lambda: percentage()).place(x=155, y=100)
Button(calculator, text="/", height=3, width=8, background="orange", bd=1, fg="white",
       command=lambda: enter("/")).place(x=230, y=100)

Button(calculator, text="7", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("7")).place(x=5, y=160)
Button(calculator, text="8", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("8")).place(x=80, y=160)
Button(calculator, text="9", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("9")).place(x=155, y=160)
Button(calculator, text="*", height=3, width=8, background="orange", bd=1, fg="white",
       command=lambda: enter("*")).place(x=230, y=160)

Button(calculator, text="4", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("4")).place(x=5, y=220)
Button(calculator, text="5", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("5")).place(x=80, y=220)
Button(calculator, text="6", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("6")).place(x=155, y=220)
Button(calculator, text="-", height=3, width=8, background="orange", bd=1, fg="white",
       command=lambda: enter("-")).place(x=230, y=220)

Button(calculator, text="1", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("1")).place(x=5, y=280)
Button(calculator, text="2", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("2")).place(x=80, y=280)
Button(calculator, text="3", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("3")).place(x=155, y=280)
Button(calculator, text="+", height=3, width=8, background="orange", bd=1, fg="white",
       command=lambda: enter("+")).place(x=230, y=280)

Button(calculator, text="0", height=3, width=19, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter("0")).place(x=5, y=340)
Button(calculator, text=".", height=3, width=8, background="#2F2E2E", bd=1, fg="white",
       command=lambda: enter(".")).place(x=155, y=340)
Button(calculator, text="=", height=3, width=8, background="orange", bd=1, fg="white",
       command=lambda: calculate()).place(x=230, y=340)

calculator.mainloop()