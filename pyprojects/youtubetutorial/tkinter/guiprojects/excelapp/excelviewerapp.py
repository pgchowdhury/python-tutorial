"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 01-Jan-2025
    Project: Excel Spreadsheet Viewer App
    Library: Tkinter, TTKBootstrap, Openpyxl
"""
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Messagebox
from openpyxl import load_workbook

xl_view = ''
xl_frame = ''

## Function - Do Something ##
def choose_file():
    file_name = filedialog.askopenfilename()
    file_path.set(value=file_name)
    # print(file_path.get())
    load_xl_values(file_path.get())

def load_xl_values(file_name):
    coldata = []
    rowdata = []
    wb = load_workbook(filename=file_name)
    ws = wb.active
    list_values = list(ws.values)
    coldata = list(list_values[0])
    rowdata = [item for item in list_values[1:]] 
    show_xl(coldata, rowdata)

def show_xl(coldata, rowdata):
    ## Widget ##
    global xl_frame
    xl_frame = ttk.Frame(master=window)
    global xl_view
    xl_view = Tableview(master=xl_frame, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, pagesize=30, 
                        height=30, bootstyle='success', autofit=True, autoalign=True)
    ## Layout ##
    xl_frame.pack(padx=(20, 20), pady=(20, 20), fill='both')
    xl_view.pack(fill='both', expand=1)

def close_xl():
    global xl_view
    if xl_view != '':
        xl_view.destroy()
        global xl_frame
        xl_frame.destroy()
    else:
        Messagebox.show_warning(alert=True, message='No Excel File Selected', title='No File')

if __name__ == '__main__':
    ## Window ##
    window = ttk.Window(themename='journal')
    window.title('XL Viewer App')
    window.minsize(500, 700)
    
    ## variable ##
    file_path = tk.StringVar()
    
    ## Widegts ##
    header_label = ttk.Label(master=window, text='View Excel Spreadsheet', font=('verdana', 20, 'bold'), bootstyle='info')
    open_frame = ttk.Frame(master=window)
    open_button = ttk.Button(master=open_frame, text='Open Xl File', bootstyle='success-outline', command=choose_file)
    close_button = ttk.Button(master=open_frame, text='Close XL File', bootstyle='success-outline', command=close_xl)
    separtor = ttk.Separator(master=window, orient='horizontal', bootstyle='primary')
    
    ## layout ##
    header_label.pack(pady=(10, 20))
    open_frame.pack(pady=(0, 10))
    open_button.pack(side='left', padx=(0, 10))
    close_button.pack()
    separtor.pack(fill='x')
    
    ## run ##
    window.mainloop()
