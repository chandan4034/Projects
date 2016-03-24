__author__ = 'chandan'
from tkinter import *
root=Tk()
Fixed = Label(root,text='Fixed size',bg='black',fg='white')
Fixed.pack()
HorizontalGrow=Label(root,text='Horizontal Grow up',bg='green',fg='blue')
HorizontalGrow.pack(fill = X);
VerticalGrow = Label(root,text='Vertical Grow up',bg='white',fg='black')
VerticalGrow.pack(side=RIGHT,fill = Y); #if side is not left or right then defualt center and in case of center not grow in y direction

root.mainloop()
