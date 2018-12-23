from tkinter import *
import button as bt

root = Tk()
root.title("CobraCalc")
root.geometry('400x500')

btn_names = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', ',', '=', '+']
buttons = bt.btn_tk_img(btn_names)


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
