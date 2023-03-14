from tkinter import*
w=Tk()
w.width=w.winfo_screenwidth()
w.height=w.winfo_screenheight()
w.geometry("{j}x{h}+0+0".format(j=w.width , h=w.height))   
#print(w.winfo_screenwidth())
#print(w.winfo_screenheight())
mainloop()