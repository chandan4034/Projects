__author__ = 'chandan'
#Frame created invisible Frames and we can put widget in those invisible frames
from tkinter import *
root=Tk()
topFrame = Frame(root)
topFrame.pack();
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text='First',fg='red')
button2 = Button(topFrame,text='Second',fg='blue')
button3 = Button(topFrame,text='Third',fg='green')
button4 = Button(bottomFrame,text='Fourth',fg='purple')

button1.pack(side=LEFT) #if no parameter then it looks like it is in same frame but if we put left then it put left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT) # paremeter can be right,top,or botton as it is in bottom frame so no effect can in this way
                        #we can create invisible frames

root.mainloop()