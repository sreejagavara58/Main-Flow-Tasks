from tkinter import *
from PIL import ImageTk, Image

def init_calculator():
  rt = Tk()
  rt.title("Basic Calculator")

  rt.iconbitmap("Calculator_30001.ico")
  rt.geometry("300x450")
    
  bg = ImageTk.PhotoImage(file="background.jpg")
  bg_label = Label(rt, image=bg)
  bg_label.place(x=0, y=0)

  e = Entry(rt, width=35, borderwidth=10, font=("Times", 10))
  e.grid(row=0, column=0, columnspan=3, padx=30, pady=20)

  images = {
      "1": ImageTk.PhotoImage(file="Copy of 1.png"),
      "2": ImageTk.PhotoImage(file="Copy of 2.png"),
      "3": ImageTk.PhotoImage(file="Copy of 3.png"),
      "4": ImageTk.PhotoImage(file="Copy of 4.png"),
      "5": ImageTk.PhotoImage(file="Copy of 5.png"),
      "6": ImageTk.PhotoImage(file="Copy of 6.png"),
      "7": ImageTk.PhotoImage(file="Copy of 7.png"),
      "8": ImageTk.PhotoImage(file="Copy of 8.png"),
      "9": ImageTk.PhotoImage(file="Copy of 9.png"),
      "0": ImageTk.PhotoImage(file="Copy of 10.png"),
      "+": ImageTk.PhotoImage(file="Copy of 11.png"),
      "-": ImageTk.PhotoImage(file="Copy of 12.png"),
      "*": ImageTk.PhotoImage(file="Copy of 13.png"),
      "/": ImageTk.PhotoImage(file="Copy of 14.png"),
      "=": ImageTk.PhotoImage(file="Copy of 15.png"),
      "C": ImageTk.PhotoImage(file="Copy of 16.png")
  }
  def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

  def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

  def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

  def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

  def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

  def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
      e.insert(0, f_num + int(second_number))
    if math == "subtraction":
      e.insert(0, f_num - int(second_number))
    if math == "multiplication":
      e.insert(0, f_num * int(second_number))
    if math == "division":
      e.insert(0, f_num / int(second_number))

  def button_clear():
    e.delete(0, END)

  buttons = {
      "1": (1, 0, lambda: button_click(1)),
      "2": (1, 1, lambda: button_click(2)),
      "3": (1, 2, lambda: button_click(3)),
      "4": (2, 0, lambda: button_click(4)),
      "5": (2, 1, lambda: button_click(5)),
      "6": (2, 2, lambda: button_click(6)),
      "7": (3, 0, lambda: button_click(7)),
      "8": (3, 1, lambda: button_click(8)),
      "9": (3, 2, lambda: button_click(9)),
      "0": (4, 0, lambda: button_click(0)),
      "+": (4, 1, button_add),
      "-": (4, 2, button_sub),
      "*": (5, 0, button_mul),
      "/": (5, 1, button_div),
      "=": (5, 2, button_equal),
      "C": (6, 0, button_clear)
  }

  for (btn, (row, col, cmd)) in buttons.items():
    Button(rt,  border="3", image=images[btn]  ,command=cmd).grid(row=row, column=col)

  rt.images = images

  rt.mainloop()

#initialise calculator
init_calculator()
