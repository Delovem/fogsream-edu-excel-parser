import tkinter as tk
import openpyxl
from tkinter.filedialog import askopenfilename

win = tk.Tk()

icon =  tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.title('carfinder v0.1 beta')
win.geometry('305x280')
win.resizable(False, False)


filename = str()

def open_xl_file():
    filename = askopenfilename()
    print(filename)
    return str(filename)

def get_entry():
    entry_value = entry_2.get()
    print(entry_value)
    return entry_value

def insert_entry():
    global filename
    return entry_1.insert()

label_1 = tk.Label(text='Выберите файл').grid(row=0, column=0)
label_2 = tk.Label(text='Введите марку авто').grid(row=1, column=0)
label_3 = tk.Label(text='Вывод: ').grid(row=2, column=0)

entry_1 = tk.Entry()
entry_1.grid(row=0, column=1)

entry_2 = tk.Entry()
entry_2.grid(row=1, column=1)

button_1 = tk.Button(text='...', command=open_xl_file).grid(row=0, column=2, stick='we')
button_2 = tk.Button(text='Готово', command=get_entry).grid(row=1, column=2)
button_3 = tk.Button(text='О программе').grid(row=4, column=0, stick='we')
button_4 = tk.Button(text='Закрыть').grid(row=4, column=1, stick='we')


field_1 = tk.Text(win,height=10, width=35)
field_1.grid(row=3, column=0, columnspan=3)

scroller_1 = tk.Scrollbar(win, command=field_1.yview)
scroller_1.grid(row=2, column=3, rowspan=3, columnspan=2)




win.mainloop()

