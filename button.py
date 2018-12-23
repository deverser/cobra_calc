from tkinter import *


def init_button(text):
    """Создает объект кнопки"""
    btn = Button(text=text, background="#555", foreground="#ccc",
                 padx=10, pady=5, font='arial 16')
    return btn


def btn_tk_img(texts):
    """Создает список с объектами кнопок"""
    buttons = []
    for text in texts:
        button = init_button(text)
        buttons.append(button)
    return buttons


if __name__ == '__main__':
    texts = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', ',', '=', '+']
    print(btn_tk_img(texts))
