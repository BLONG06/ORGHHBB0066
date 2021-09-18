from sqlite3.dbapi2 import Error
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from sqlofthemain import *
from itertools import chain
from os import name as os_name


def zoomed(window):
    """ 
    Windows and Linux compatible full window creation option

    -> window: Toplevel widget (CLASSNAME)
    """
    if os_name == 'nt': 
        window.state('zoomed') 
    else: 
        window.attributes('-zoomed', True)


def selectUser():
    c.execute("SELECT USER FROM LOGGINDATA")


def selectPassword():
    c.execute("SELECT PASSWORD FROM LOGGINDATA")


def runMainWindow():
    global mainwindowframe, mainwindow
    mainwindow = Tk()
    # mainwindow.state('zoomed')
    zoomed(mainwindow)
    # mainwindow.attributes('-fullscreen', True)
    mainwindow.title('Loggin')
    mainwindow.iconbitmap
    mainwindow.resizable(height=False, width=False)
    mainwindowframe = Frame(mainwindow, relief=FLAT)
    
    registerbutton = Button(mainwindowframe, 
                            text=('register'), 
                            font=('Arial', 40, 'bold'), 
                            padx=600, 
                            pady=150,
                            bg='white', 
                            justify="center", 
                            command=lambda: register(rootwindow=mainwindow)
                            ).grid()    
    
    logginbutton = Button(mainwindowframe, 
                            text="loggin", 
                            font=("Arial", 40, "bold"), 
                            padx=620,
                            pady=150, 
                            bg='white', 
                            command=lambda: loggin(mainwindow)
                            ).grid()

    mainwindowframe.grid()
    # mainwindow.update()
    mainwindow.mainloop()

    
class ValueIsEmptyError(Error):
    """Raised when there is nothing in the entry input field"""
    pass


def entryValueChecker(entry, entry2):
    """
        It's gonna return True if there is nothing, or it's gonna return False if there is anything.

    """
    return True if entry.strip().isspace() or entry2.strip().isspace() else False


# class valueIsEmpty(Exception):
#     def __init__(self, message, entry, entry2):
#        super().__init__(message)
#        entryValueChecker().__init__(entry, entry2)
#        self.entry = entry
#        self.entry2 = entry2
#        if entryValueChecker(entry, entry2) == True:
#            raise valueIsEmpty(message="You have to put something on the entry", entry=entry, e2=entry2)


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    
    return _list


def goBack(packbuttonframe, fmtpk):

    def goBackNow(forgetframe,frametopack):
        forgetframe.grid_forget()
        frametopack.grid()

    gobackbutton = Button(packbuttonframe, 
                        text='Go Back', 
                        font=("Arial", 60, BOLD), 
                        relief=GROOVE, 
                        padx=220, 
                        pady=50, 
                        command=lambda: goBackNow(packbuttonframe, fmtpk)
                        ).grid()


def cleanWindow(MainWindow):
    widget_list = all_children(MainWindow)
    for item in widget_list:
        item.destroy()


def registernow(mainwindow,usrentv,pwdentv):
    c.execute("SELECT * FROM LOGGINDATA")
    c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)", (usrentv, pwdentv))
    print(usrentv, pwdentv)
    messagebox.showinfo(title="Successful",
                        message="Successfully Registered")
    cleanWindow(mainwindow)
    mainwindow.update()


def Lists(TipeofList: str):

    def flatit(listtoflat):
        flatten = chain.from_iterable
        return list(flatten(listtoflat))

    selectUser() if TipeofList.upper() == 'USER' else selectPassword()

    List = [queryresult for queryresult in c.fetchall()]
    return flatit(List)


def MyClick(rootwindow, whatever):
    MyLabel = Label(rootwindow, 
                    text=(f"Hello {whatever.get()}")
                    )
    MyLabel.grid()


def superattempt(rootwindow, TypeofAttempt):
    global x, y, userinlist, passwordinlist
    def attempts(TypeofAttempt: str):

        def register():
            print(x, y)

            if (x in userinlist): #and (y in passwordinlist)
                messagebox.showerror(title="Error", message="The typed user already exist")
            
            elif (x not in userinlist) or (y not in passwordinlist):
                
                if entryValueChecker(x, y) == True :
                    messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
                
                elif (" " in x) or (" " in y):
                    messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
                
                else:
                    registernow(rootwindow, x, y)

        def loggin():
            if (x in userinlist) and (y in passwordinlist):
                cleanWindow(frame)
            
            elif (x not in userinlist) or (y not in passwordinlist):
                
                if x == "" or y == "":# if entryValueChecker(x, y) == True :
                    messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
                
                elif " " in x or " " in y:
                    messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
                
                elif (x in userinlist) and (y not in passwordinlist):
                    messagebox.showwarning(title='Password Error', message="Wrong Password")
                
                else:
                    messagebox.showerror(
                    title="Error", message="The typed user doesn't exist")

        selectUser()
        x = str(usersv.get())
        # userentryvalue = str(userentryvalue)
        y = str(passwordsv.get())
        # passwordentryvalue = str(passwordentryvalue)
        
        userinlist = Lists('USER')
        passwordinlist = Lists('PASSWRD')

        if TypeofAttempt.upper() == 'REGISTER':
            register()
        
        elif TypeofAttempt == 'LOGGIN':
            loggin()

    mainwindowframe.grid_forget()
    usersv = StringVar()
    passwordsv = StringVar()
    frame = Frame(rootwindow, relief=FLAT)

    userentry = Entry(frame, 
                        textvariable=usersv, 
                        font=("Arial", 60, "bold")
                        )
    
    passwordentry = Entry(frame, 
                            textvariable=passwordsv,
                            font=("Arial", 60, "bold")
                            )
    
    userentry.grid()
    passwordentry.grid()
                
    # register_attempt()

    confirmbutton = Button(frame, 
                            text='Click Here to Register', 
                            font=("Arial", 60, BOLD), 
                            relief=GROOVE, 
                            padx=220, 
                            pady=50, 
                            command=lambda: attempts('REGISTER') 
                                    if TypeofAttempt == 'REGISTER' else 'LOGGIN'
                            ).grid()
    
    goBack(frame, mainwindowframe)
    frame.grid()
    print()


def register(rootwindow): 
    superattempt(rootwindow, 'REGISTER')


def loggin(rootwindow):
    superattempt(rootwindow, 'LOGGIN')

    # for query_result in c.fetchall():
    #         if userentryvalue not in query_result:
    #             # messagebox.showerror(title="Error", message="User doesn't exist, please come back and register")
    #             notinlist = []
    #             notinlist.append(query_result)
    #             if userentryvalue in notinlist:
    #                 widget_list = all_children(rootwindow)
    #                 for item in widget_list:
    #                     item.destroy()

    #             else:
    #                 messagebox.showerror(title="Error", message="User does not exists")
    #             print(notinlist)


# widget_list = all_children(rootwindow)
#                 for item in widget_list:
#                         item.destroy()
#             elif userentryvalue not in query_result:
#                 messagebox.showerror(title="Error", message="User doesn't exist, please come back and register")


   #     time.sleep(5)
                # errorobject = valueIsEmpty(message="We got a error", entry=x, entry2=y)
                # try:
                #     rootwindow.update()
                #     if (x or y == "") or (x.isspace() or y.isspace() == True):
                #         raise ValueIsEmptyError
                #     # c.execute("SELECT * FROM LOGGINDATA")
                #     # print("Something just for a simple test")
                #     # c.exe-cute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)",
                #     #           (userentryvalue, passwordentryvalue))
                #     # messagebox.showinfo(title="Successful",
                #     #                     message="Successfully Registered")
                #     # cleanWindow(rootwindow)
                #     # rootwindow.update()
                # except ValueIsEmptyError:
                #     print("Please, fill in the fields")
                #     # rootwindow.update()
                #     print("Error: It should be something in the entry")
                #     messagebox.showerror(title="Error", message="It should be something on the entry field")
                #     break
                # print('deu certo')
                # registernow(mainwindow=rootwindow, usrentv=x, pwdentv=y)
