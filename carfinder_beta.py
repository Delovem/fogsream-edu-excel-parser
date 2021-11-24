import tkinter as tk
import openpyxl
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb

win = tk.Tk()

icon = tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)
win.title('carfinder v0.1 beta')
win.geometry('305x280')
win.resizable(False, False)

filename = str()


def open_xl_file():
    """диалоговое окно для выбора файла
    так же подтягивает путь до файла в первое поле ввода"""

    filename = askopenfilename()
    entry_1.insert(0, filename)
    return str(filename)


def get_entry():
    """Получает текст из поля ввода"""
    entry_value = entry_2.get()
    return entry_value


def get_entry_filename():
    """получает текст пути до файла"""
    entry_value = entry_1.get()
    return entry_value


def excel_delaem_delo():
    wb = openpyxl.load_workbook(get_entry_filename())
    sheet = wb['Лист1']

    row_count = sheet.max_row

    for row in range(1, row_count):
        brand = sheet[row][0].value
        model = sheet[row][1].value

        if brand.lower() == get_entry() or get_entry() in brand.lower():
            field_1.insert(0.0, (f'{brand} {model} \n'))
            print(brand, model)


def close_window():
    """закрывает окно"""
    win.destroy()


def about_soft():
    """информационное окно"""
    mb.showinfo(
        title="О Программе",
        message='Версия 0.1 beta'
                '\n  '
                '\nИсходный код: https://github.com/Delovem/fogsream-edu-excel-parser'
                '\n  '
                '\nДанная программа является учебным проектом и разработана в рамках обучения в компании Forgstream на курсе "Основы Python Сентябрь" в 2021 году'
                '\n  '
                '\nCopyright (c) Delovem software 2021-2022')


label_1 = tk.Label(text='Выберите файл').grid(row=0, column=0)
label_2 = tk.Label(text='Введите марку авто').grid(row=1, column=0)
label_3 = tk.Label(text='Вывод: ').grid(row=2, column=0)

entry_1 = tk.Entry()
entry_1.grid(row=0, column=1)

entry_2 = tk.Entry()
entry_2.grid(row=1, column=1)

button_1 = tk.Button(text='...', command=open_xl_file).grid(row=0, column=2, stick='we')
button_2 = tk.Button(text='Готово', command=excel_delaem_delo).grid(row=1, column=2)
button_3 = tk.Button(text='О программе', command=about_soft).grid(row=4, column=0, stick='we')
button_4 = tk.Button(text='Закрыть', command=close_window).grid(row=4, column=1, columnspan=2, stick='we')

field_1 = tk.Text(win, height=10, width=35, wrap='word')
field_1.grid(row=3, column=0, columnspan=3)

scroller_1 = tk.Scrollbar(win, command=field_1.yview)
scroller_1.grid(row=2, column=3, rowspan=2, columnspan=2, stick='ns')

win.mainloop()
