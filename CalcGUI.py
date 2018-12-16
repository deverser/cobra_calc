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

btn_7.place(x=35, y=250, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_8.place(x=110, y=250, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_9.place(x=185, y=250, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_div.place(x=260, y=250, anchor='c',
              height=60, width=60, bordermode=OUTSIDE)
btn_4.place(x=35, y=320, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_5.place(x=110, y=320, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_6.place(x=185, y=320, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_mltp.place(x=260, y=320, anchor='c',
               height=60, width=60, bordermode=OUTSIDE)
btn_1.place(x=35, y=390, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_2.place(x=110, y=390, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_3.place(x=185, y=390, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_minus.place(x=260, y=390, anchor='c',
                height=60, width=60, bordermode=OUTSIDE)
btn_0.place(x=35, y=460, anchor='c',
            height=60, width=60, bordermode=OUTSIDE)
btn_comma.place(x=110, y=460, anchor='c',
                height=60, width=60, bordermode=OUTSIDE)
btn_equal.place(x=185, y=460, anchor='c',
                height=60, width=60, bordermode=OUTSIDE)
btn_plus.place(x=260, y=460, anchor='c',
               height=60, width=60, bordermode=OUTSIDE)


root.mainloop()
