import tkinter as tk

win = tk.Tk()

icon =  tk.PhotoImage(file='icon.png')
win.iconphoto(False, icon)

win.config(bg='#545454')

win.title('carfinder fogstream_education')
win.geometry('500x600+600+100')
win.resizable(False, False)

def add_label():
    label = tk.Label(win, text='Test')
    label.pack()

button_1 = tk.Button(win, text='testing test',

                     bg='grey',
                     padx=30,
                     pady=20
                     )

button_2 = tk.Button(win, text='Выберите файл',
                     command=add_label)

button_1.pack()
button_2.pack()

win.mainloop()