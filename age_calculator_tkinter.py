#source: https://www.pythonistaplanet.com/age-calculator-app-using-python-tkinter/

import datetime
import tkinter as tk


# window
window = tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ")

# labels
nlabel = tk.Label(text="Name")
nlabel.grid(column=0, row=1)
ylabel = tk.Label(text="Year")
ylabel.grid(column=0, row=2)
mlabel = tk.Label(text="Month")
mlabel.grid(column=0, row=3)
dlabel = tk.Label(text="Day")
dlabel.grid(column=0, row=4)

# entry_fields
nentry = tk.Entry()
nentry.grid(column=1, row=1)
yentry = tk.Entry()
yentry.grid(column=1, row=2)
mentry = tk.Entry()
mentry.grid(column=1, row=3)
dentry = tk.Entry()
dentry.grid(column=1, row=4)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


def getInput():
    userName = nentry.get()
    userYear = int(float(yentry.get()))
    userMonth = mentry.get()
    userDay = dentry.get()
    p=Person(userName,datetime.date(yentry.get(),mentry.get(),dentry.get()))
    texter = tk.Text(master=window, height=10, width=25)
    texter.grid(column=1, row=6)
    result = "You are " + p.age() + " years old"
    texter.insert(tk.END, result)

button=tk.Button(window,text="Calculate Age",command=getInput(),bg="pink")
button.grid(column=1,row=5)



window.mainloop()