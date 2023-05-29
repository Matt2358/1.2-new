from tkinter import *
root = Tk()
root.title('Произведение двух чисел')
Label(root, text='Первое число').grid(row=0, sticky=W)
Label(root, text='Второе число').grid(row=1, sticky=W)
EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)
EntryC.grid(row=2, columnspan=2)
def plus():
    a = EntryA.get() 
    a = int(a)

    b = EntryB.get() 
    b = int(b)

    result = str(a + b)
    EntryC.delete(0, END) 
    EntryC.insert(0, result)  

button = Button(root, text='Сумма',command=plus)
button.grid(row=3, column=1, sticky=E)

root.mainloop()
