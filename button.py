from tkinter import *

def init_button(text):
    btn = Button(text=text, background="#555", foreground="#ccc",
               padx=10, pady=5, font=16)
    return btn

def create_btn_dict(texts):
    btn_dict = {}
    for i in range(16):
        btn_dict[i] = init_button(texts[i])
    return btn_dict