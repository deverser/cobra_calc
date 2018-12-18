from tkinter import *

root = Tk()
root.title("CobraCalc")
root.geometry('400x500')

btn_7 = Button(text='7', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_8 = Button(text='8', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_9 = Button(text='9', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_4 = Button(text='4', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_5 = Button(text='5', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_6 = Button(text='6', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_1 = Button(text='1', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_2 = Button(text='2', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_3 = Button(text='3', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_0 = Button(text='0', background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
btn_comma = Button(text=',', background="#555", foreground="#ccc",
                   padx=10, pady=5, font=16)
btn_div = Button(text='/', background="#555", foreground="#ccc",
                 padx=10, pady=5, font=16)
btn_mltp = Button(text='*', background="#555", foreground="#ccc",
                  padx=10, pady=5, font=16)
btn_minus = Button(text='-', background="#555", foreground="#ccc",
                   padx=10, pady=5, font=16)
btn_equal = Button(text='=', background="#555", foreground="#ccc",
                   padx=10, pady=5, font=16)
btn_plus = Button(text='+', background="#555", foreground="#ccc",
                  padx=10, pady=5, font=16)

buttons = [btn_7, btn_8, btn_9, btn_div, btn_4, btn_5, btn_6, btn_mltp, btn_1,
           btn_2, btn_3, btn_minus, btn_0, btn_comma, btn_equal, btn_plus]


def draw_btn_row(x0, y0, btn_dict):
    """Рисует ряд кнопок"""
    for button in btn_dict:
        button.place(x=x0, y=y0, anchor='c', height=60, width=60,
                     bordermode=OUTSIDE)
        x0 += 75


def draw_btn_grid(x0, y0, btn_dict):
    """Выводит сетку кнопок на экран"""
    i = 0          # первый элемент ряда кнопок
    j = 4          # последний элемент ряда кнопок
    while True:
        draw_btn_row(x0, y0, btn_dict[i:j])
        y0 += 70
        i += 4
        j += 4
        if j > len(btn_dict):
            break


draw_btn_grid(35, 250, buttons)
root.mainloop()
