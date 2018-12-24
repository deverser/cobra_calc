from tkinter import *
import button as bt

root = Tk()
root.title("CobraCalc")
root.geometry('300x500')
root.resizable(False, False)

options = Menu(tearoff=0)
options.add_command(label="Settings")
options.add_command(label="About")
options.add_command(label="Exit")

display = Label(text='', bg='white', fg='black', font='arial 16', width=295, height=5)


btn_7 = bt.init_button('7')
btn_8 = bt.init_button('8')
btn_9 = bt.init_button('9')
btn_4 = bt.init_button('4')
btn_5 = bt.init_button('5')
btn_6 = bt.init_button('6')
btn_1 = bt.init_button('1')
btn_2 = bt.init_button('2')
btn_3 = bt.init_button('3')
btn_0 = bt.init_button('0')
btn_comma = bt.init_button(',')
btn_div = bt.init_button('/')
btn_mltp = bt.init_button('*')
btn_minus = bt.init_button('-')
btn_equal = bt.init_button('=')
btn_plus = bt.init_button('+')

buttons = [btn_7, btn_8, btn_9, btn_div, btn_4, btn_5, btn_6, btn_mltp, btn_1, btn_2,
           btn_3, btn_minus, btn_comma, btn_0, btn_equal, btn_plus]

main_menu = Menu()
main_menu.add_cascade(label="Options", menu=options)


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


def show_nums(event):
    event['text'] = '7'


btn_7.bind('7', show_nums)


def exit_win(event):
    root.destroy()


display.pack()
draw_btn_grid(35, 250, buttons)
root.config(menu=main_menu)
root.bind('q', exit_win)

root.mainloop()
