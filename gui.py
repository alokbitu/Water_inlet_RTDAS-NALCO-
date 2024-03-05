from tkinter import *
import tkinter as tk
import tkinter.messagebox
import time
import sys
#import pandas as pd

t = time.localtime(time.time())
Year=t.tm_year
Month=t.tm_mday
Day=t.tm_mday

Minutes = t.tm_min
Hours=t.tm_hour
Seconds = t.tm_sec

# time.sleep(300000)
#=================Root Window====================#
w1 = Tk()
w1.title('NALCO Smelter')
w1.geometry('800x480+0+0')
w1.config(bg='#7f8274')
ptitle = Label(w1, font=('arial', 12, 'bold'),text='NALCO Smelter Water Inlet Station\nStation Id:2',width=102)
ptitle.config(bg='cyan')
ptitle.grid(padx=1,pady=1, columnspan=3)

# ================Read files and get data ====================#
def get_value():
    with open('current_discharge.txt', 'r') as file:
        e_text = file.readlines()
        print(e_text)
        t1.insert(tk.END, e_text)

        file.close()


    with open('total_discharge.txt', 'r') as file2:
        e_text2 = file2.readlines()
        print(e_text2)
        t2.insert(tk.END, e_text2)
        file2.close()

# ================Clear the text box ====================#
def clear_value():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    #t3.delete('1.0', END)
    #t4.delete('1.0', END)

def clear_and_display():
    clear_value()
    get_value()
    w1.after(30000, clear_and_display)


# ==========Define Variables===================#

current_discharge = tk.StringVar()
total_discharge = tk.StringVar()
#last_day_discharge = tk.StringVar()
#today_discharge = tk.StringVar()
description = tk.StringVar()

# ================Initialize==============#
def clear():
    current_discharge.set('')
    total_discharge.set('')
    #last_day_discharge .set('')
    #today_discharge.set('')

    l1.configure(state='normal')
    t1.configure(state='normal')

# ==========Label & TextBoxes ============#
l1 = Label(w1,text=' Rate(m3/hr) ',bg='#ADD8E6', font=("Arial Bold", 30),width=16,height=3)
t1 = tk.Text(w1, height=2, width=13, bg='#ADD8E6',font=('Arial Bold',40),foreground='red')

l6 = Label(w1,text='',bg='#7f8274',width=40)
l7 = Label(w1,text='',bg='#7f8274',width=40)
l8 = Label(w1,text='',bg='#7f8274',width=40)

l2 = Label(w1, text=' Total(m3) ',bg='#ADD8E6',font=("Arial Bold", 30),width=16,height=3)
t2 = tk.Text(w1, height=2, width=13, bg='#ADD8E6',font=('Arial Bold',40),foreground='red')

l5 = Label(w1, text=' Sunjray Infosystems Pvt. Ltd.\nBhubaneswar – 12 ', font=("Arial Bold",12,'bold'),width=83)
l5.config(bg='cyan')
l5.grid(row=15,column=0, columnspan=3)

l10 = Label(w1,text='',bg='#7f8274',width=50)

l11 = Label(w1,text='',bg='#7f8274',width=50)

l12 = Label(w1,text='',bg='#7f8274',width=50)

#Create a button to display the text of entry widget
button1= Button(w1, text=' Display Value ', command=clear_and_display,width=10,height=1,font=("bold"))
# button2= Button(w1, text=' Clear Value ', command=clear_value,width=10,height=1,font=("bold"))
# button4= Button(w1, text='Quit', command=end ,width=10,height=1,font=("bold"))
#Define the position of text boxes for display
l10.grid(row=1, column=0)

l1.grid(row=2, column=0,columnspan=1)
t1.grid(row=2, column=1,columnspan=1)

l6.grid(row=3, column=0)
l7.grid(row=4, column=0)
#l8.grid(row=5, column=0)

l2.grid(row=6, column=0,columnspan=1)
t2.grid(row=6, column=1,columnspan=1)



l11.grid(row=10, column=0)

#l12.grid(row=12, column=0)

button1.grid(row=11, column=0)
# button2.grid(row=11, column=1)
# button4.grid(row=12, column=0)

w1.mainloop()

