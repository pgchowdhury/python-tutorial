"""
    Author: Prosenjit Ghosh Chowdhury (techwithpro18)
    Date: 28-Nov-2024
    Project: Calculator
    Library: tkinter and for Mac tkmacosx
    Color Used: background: #006400, button - 1st Row #F0E68C, 4th Column #DCDCDC, Num Row #ADEFD1
    Window Size: 280x380
"""
import tkinter as tk
from tkmacosx import Button

calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation = calculation + str(symbol)
    text_result.delete(0, 'end')
    text_result.insert(0, calculation)
    
def eval_calculation():
    global calculation
    try:
        result = round(eval(calculation), 2)
        text_result.delete(0, 'end')
        text_result.insert(0, result)
        calculation = str(result)
    except Exception as e:
        print(e)
        clear_field()

def negate_num():
    global calculation
    calculation = str(int(calculation) * (-1))
    text_result.delete(0, 'end')
    text_result.insert(0, calculation)
    
def clear_field():
    text_result.delete(0, 'end')
    global calculation
    calculation = ''


root = tk.Tk()
root.title("Calculator")
root.geometry('280x380')
root.resizable(0,0)
root.config(background='#006400')

text_result = tk.Entry(root, width=9, bg='#006400', fg='white', bd= 0, font=('verdana', 40, 'bold'),
                       highlightthickness = 0, borderwidth=0)
text_result.grid(row=0, column=0, pady=(20, 20), columnspan=5)

#### First Row Buttons - Start ####
btn_ac = Button(root, text='AC', bg='#F0E68C',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command = clear_field)
btn_ac.grid(row=1, column=0)
btn_negate = Button(root, text='+/-', bg='#F0E68C',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=negate_num)
btn_negate.grid(row=1, column=1)
btn_mod = Button(root, text='%', bg='#F0E68C',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation('%'))
btn_mod.grid(row=1, column=2)
btn_divide = Button(root, text='/', bg='#DCDCDC',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation('/'))
btn_divide.grid(row=1, column=3)
#### First Row Buttons - End ####

#### Second Row Buttons - Start ####
btn_7 = Button(root, text='7', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(7))
btn_7.grid(row=2, column=0)
btn_8 = Button(root, text='8', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(8))
btn_8.grid(row=2, column=1)
btn_9 = Button(root, text='9', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(9))
btn_9.grid(row=2, column=2)
btn_multi = Button(root, text='*', bg='#DCDCDC',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command=lambda:add_to_calculation('*'))
btn_multi.grid(row=2, column=3)
#### Second Row Buttons - End ####

#### Third Row Buttons - Start ####
btn_4 = Button(root, text='4', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command=lambda:add_to_calculation(4))
btn_4.grid(row=3, column=0)
btn_5 = Button(root, text='5', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command=lambda:add_to_calculation(5))
btn_5.grid(row=3, column=1)
btn_6 = Button(root, text='6', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command=lambda:add_to_calculation(6))
btn_6.grid(row=3, column=2)
btn_sub = Button(root, text='-', bg='#DCDCDC',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20),
              command=lambda:add_to_calculation('-'))
btn_sub.grid(row=3, column=3)
#### Third Row Buttons - End ####

#### Fourth Row Buttons - Start ####
btn_1 = Button(root, text='1', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(1))
btn_1.grid(row=4, column=0)
btn_2 = Button(root, text='2', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(2))
btn_2.grid(row=4, column=1)
btn_3 = Button(root, text='3', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(3))
btn_3.grid(row=4, column=2)
btn_add = Button(root, text='+', bg='#DCDCDC',fg='grey', borderless=1, width=70, height=55, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation('+'))
btn_add.grid(row=4, column=3)
#### Fourth Row Buttons - End ####

#### Fourth Row Buttons - Start ####
btn_0 = Button(root, text='0', bg='#ADEFD1',fg='grey', borderless=1, width=140, height=65, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation(0))
btn_0.grid(row=5, column=0, columnspan=2)
btn_point = Button(root, text='.', bg='#ADEFD1',fg='grey', borderless=1, width=70, height=65, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command=lambda:add_to_calculation('.'))
btn_point.grid(row=5, column=2)
btn_equal = Button(root, text='=', bg='#DCDCDC',fg='grey', borderless=1, width=70, height=65, 
              activebackground='white', activeforeground='grey', font=('verdana', 20), 
              command= eval_calculation)
btn_equal.grid(row=5, column=3)
#### Fourth Row Buttons - End ####
root.mainloop()