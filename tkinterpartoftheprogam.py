from tkinter import *
from defofthemain import *


# logginwindow = Tk()
# zoomed(logginwindow)
# logginwindow.title('Loggin')
# logginwindow.iconbitmap
# logginwindow.resizable(height=False, width=False)


# registerbutton = Button(logginwindow, 
#                         text=('register'), 
#                         font=('Arial', 40, 'bold'), 
#                         padx=600, 
#                         pady=150,
#                         bg='white', 
#                         justify="center", 
#                         command=lambda: register(registerbutton, logginbutton, logginwindow))

# logginbutton = Button(logginwindow, 
#                       text="loggin", 
#                       font=("Arial", 40, "bold"), 
#                       padx=620,
#                       pady=150, 
#                       bg='white', 
#                       command=lambda: loggin(registerbutton, logginbutton, logginwindow))

# registerbutton.grid()
# logginbutton.grid()
# logginwindow.update()
# windowname = 'Menu'
# logginwindow.mainloop()
runMainWindow()
root = Tk()
# root.geometry("500x300+450+250")
root.title("Personal Database")
zoomed(root)
# root.attributes('-fullscreen', True)
# root.iconbitmap("C:/Users/Guilherme/Downloads/personaldata_Msh_icon.ico")
icon = PhotoImage(file="C:/Users/guilh/OneDrive/Progamar/personaldata.png")
root.iconphoto(True, icon)
# or u can also put instead of black the hex code of some color u want
root.config(background="White")
Name_label = Label(root, width=20, height=10, text="CDB PANEL")
Name_label.grid(row=0, column=0)

conn.commit()
conn.close()
