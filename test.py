import tkinter as tk
import openpyxl
from tkinter.filedialog import askopenfilename

win = tk.Tk()

icon =  tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.title('carfinder v0.1 beta')
win.geometry('320x320')
win.resizable(False, False)


filename = str()

def open_xl_file():
    filename = askopenfilename()
    print(filename)
    return str(filename)

def get_entry():
    entry_value = entry_1.get()
    print(entry_value)
    return entry_value

def insert_entry():
    global filename
    return entry_1.insert(filename)

label_1 = tk.Label(text='Выберите файл')
label_2 = tk.Label(text='Введите марку авто')


label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)


entry_1 = tk.Entry()
entry_1.grid(row=0, column=1)

entry_2 = tk.Entry()
entry_2.grid(row=1, column=1)

button_1 = tk.Button(text='...', command=lambda: (open_xl_file(), insert_entry))
button_1.grid(row=0, column=2, stick='we')

button_2 = tk.Button(text='Готово', command=get_entry)
button_2.grid(row=1, column=2)



win.mainloop()

