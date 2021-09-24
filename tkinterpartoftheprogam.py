from tkinter import *
from defofthemain import *
# GUI
class app():
    def __init__(self):
        global mainwindow
        self.mainwindow = Tk()
        mainwindow = self.mainwindow
        self.mainwindow.state("zoomed")
        self.menu_frame = Frame(self.mainwindow, relief= FLAT)
        menu_frame = self.menu_frame
        self.register_frame = Frame(self.mainwindow, relief=FLAT)
        self.loggin_frame = Frame(self.mainwindow, relief=FLAT)

        self.width = self.mainwindow.winfo_screenwidth()
        self.height = self.mainwindow.winfo_screenheight()
        # mainwindow.resizable(False, False)

        #-------------------------------------------------------------------------------------
        #WIDGETS menu_frame
        self.registerbutton = Button(self.menu_frame, text='Register', font='Arial 40', command=lambda: show(self.register_frame), padx=15, pady=10)
        self.logginbutton = Button(self.menu_frame, text='Loggin', font='Arial 40', command=lambda: show(self.loggin_frame), padx=50, pady=10)


        #LAYOUT menu_frame
        self.menu_frame['width'] = self.width
        self.menu_frame['height'] = self.height
        self.registerbutton.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.logginbutton.place(relx=0.5, rely=0.6, anchor=CENTER)

        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        
        
        #WIDGETS register_frame
        #Labels
        self.label_user = Label(self.register_frame, text='User:', font='Arial 40')
        self.label_password = Label(self.register_frame, text='Password:', font='Arial 40')
        #----------------------------------------------------------------------------------
        #Entries
        self.user_entry_register = Entry(self.register_frame, font='Arial 40')
        self.password_entry_register = Entry(self.register_frame, show="*", font='Arial 40')
        #----------------------------------------------------------------------------------
        #Buttons
        self.register_button = Button(self.register_frame, text='Register', font='Arial 40', command=lambda: register_attempt(mainwindow, self.user_entry_register, self.password_entry_register, frameback=menu_frame))
        self.goback_button = Button(self.register_frame,  text='Go back', font='Arial 40', command=lambda: show(self.menu_frame, self.user_entry_register, self.password_entry_register))
        #Checkbutton
        self.cregister_var = IntVar()
        self.register_checkbutton = Checkbutton(self.register_frame,font="Arial 15", text="Show Password", width=20,height=20, variable=self.cregister_var, onvalue=1, offvalue=0, command=lambda:showPassword(self.password_entry_register, self.cregister_var))
        
        #------------------------------------------------------------------------------------------------------------------------
        
        #LAYOUT register_frame
        self.loggin_frame['width'] = self.width 
        self.loggin_frame['height'] = self.height

        self.label_user.place(relx=0.25, rely=0.3, anchor=CENTER)
        self.label_password.place(relx=0.210, rely=0.5, anchor=CENTER)
        self.user_entry_register.place(relx=0.55, rely=0.3, anchor=CENTER)
        self.password_entry_register.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.register_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.register_checkbutton.place(relx=0.920, rely=0.65, anchor=CENTER)
        self.goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)

        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        #WIDGETS loggin_frame
        #Labels
        self.label_user = Label(self.loggin_frame, text='User:', font='Arial 40')
        self.label_password = Label(self.loggin_frame, text='Password:', justify="right", font='Arial 40')
        #-----------------------------------------------------------------------------------------------------------------------
        #Entries
        self.user_entry_loggin = Entry(self.loggin_frame, font='Arial 40')
        self.password_entry_loggin = Entry(self.loggin_frame, show="*", font='Arial 40')
        #-----------------------------------------------------------------------------------------------------------------------
        #Buttons
        self.loggin_button = Button(self.loggin_frame, text='Loggin', font='Arial 40', command=lambda: loggin_attempt(mainwindow,self.user_entry_loggin, self.password_entry_loggin))
        self.goback_button = Button(self.loggin_frame,  text='Go Back', font='Arial 40', command=lambda: show(self.menu_frame, self.user_entry_loggin, self.password_entry_loggin))
        #-----------------------------------------------------------------------------------------------------------------------
        #Checkbutton
        self.cloggin_var = IntVar()
        self.loggin_checkbutton = Checkbutton(self.loggin_frame,font="Arial 15", text="Show Password", width=20, height=20, variable=self.cloggin_var, onvalue=1, offvalue=0, command=lambda:showPassword(self.password_entry_loggin, self.cloggin_var))
        #-----------------------------------------------------------------------------------------------------------------------
        
        #LAYOUT loggin_frame     
        self.loggin_frame['width'] = self.width
        self.loggin_frame['height'] = self.height

        self.label_user.place(relx=0.25, rely=0.3, anchor=CENTER)
        self.label_password.place(relx=0.210, rely=0.5, anchor=CENTER)
        self.user_entry_loggin.place(relx=0.55, rely=0.3, anchor=CENTER)
        self.password_entry_loggin.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.loggin_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.loggin_checkbutton.place(relx=0.920, rely=0.65, anchor=CENTER)
        self.goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)

        #-------------------------------------------------------------------------------------
        #GUI
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.register_frame.grid(row=0, column=0, sticky="nsew")
        self.loggin_frame.grid(row=0, column=0, sticky="nsew")

        show(self.menu_frame)

        self.mainwindow.mainloop() 



if __name__ == "__main__":
    app()
