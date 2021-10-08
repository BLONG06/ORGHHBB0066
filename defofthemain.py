from sqlite3.dbapi2 import Error
from tkinter import *
from tkinter import font, messagebox
from tkinter.font import BOLD, Font
from sqlofthemain import *
import time
import itertools
from os import name as os_name


# -------------------------------------------------------------------------------------
# Functions
def show(frame, *entries):
    '''
         This function raise a frame and clean the frame's entries
    '''
    frame.tkraise()
    for entry in entries:
        entry.delete(0, "end")

def login_info_verify(user, password):
    # c.execute(f"SELECT USER,PASSWORD FROM LOGGINDATA WHERE USER='{user}' AND PASSWORD='{password}'")
    # return c.fetchone()
    c.execute(f"SELECT PASSWORD FROM LOGGINDATA WHERE USER='{user}'")
    passwordDB = flatit(c.fetchall())
    try:
        if password in passwordDB[0]:
            return True
        else:
            return False
    except IndexError as error:
        return False
def selectUser():
    c.execute("SELECT USER FROM LOGGINDATA")

def selectPassword():
    c.execute("SELECT PASSWORD FROM LOGGINDATA")

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list

def showPassword(pwdenf, checkboxvar):
    
    # for checkbox in checkboxvar:
    if checkboxvar.get() == 1:
        pwdenf.config(show="")
        
    elif checkboxvar.get() == 0:
        pwdenf.config(show="*")
        

def cleanWindow(MainWindow):
    widget_list = all_children(MainWindow)
    for item in widget_list:
        item.destroy()

def registernow(mainwindow,usrentv,pwdentv, frameback):
    c.execute("SELECT * FROM LOGGINDATA")
    c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)", (usrentv, pwdentv))
    conn.commit()
    messagebox.showinfo(title="Successful",
                        message="Successfully Registered")
    show(frameback)
    mainwindow.update()

def flatit(listtoflat):
    flatten = itertools.chain.from_iterable
    listtoflat = list(flatten(listtoflat))
    return listtoflat

def usersList(): 
    selectUser()
    userinlist = []
    for queryresult in c.fetchall():
        userinlist.append(queryresult)
    userinlist = flatit(userinlist)
    return userinlist


def passwordList():
    selectPassword()
    passwordinlist = []
    for queryresult in c.fetchall():
        passwordinlist.append(queryresult)
    passwordinlist = flatit(passwordinlist)
    return passwordinlist

def entryValueChecker(entry, entry2):
    """
        It's gonna return True if there is nothing, or it's gonna return False if there is anything.

    """
    if (entry.isspace() == True or entry == "") or (entry2.isspace() == True or entry2 == ""):
        return True
    else:
        return False
def abcc(h, suposed_color):
            '''abcc = Any Button color changer'''
            v = h['bg'] = f'{suposed_color}'
            return v
def ab(a,suposed_color_on="white", suposed_color_off="SystemButtonFace"):
    a.bind("<Enter>", lambda e: abcc(a, f'{suposed_color_on}'))
    a.bind("<Leave>", lambda e: abcc(a, f'{suposed_color_off}'))
    
def register_attempt(rootwindow,usrentv, pwdetv, frameback):
    userinlist = usersList()
    passwordinlist = passwordList()
    userentryvalue = str(usrentv.get())
    passwordentryvalue = str(pwdetv.get())
    x = str(userentryvalue)
    y = str(passwordentryvalue)
    if (userentryvalue in userinlist): #and (passwordentryvalue in passwordinlist)
        messagebox.showerror(
            title="Error", message="The typed user already exist")
    elif (userentryvalue not in userinlist) or (passwordentryvalue not in passwordinlist):
        if entryValueChecker(x, y) == True :
            messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
        elif (" " in x) or (" " in y):
            messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
        elif (x.isascii() == False) or (y.isascii() == False):
            messagebox.showerror(title='ASCII Error', message="All charcters has to be on a ASCII format")
        else:
            registernow(rootwindow, x, y, frameback=frameback)    


def loggin_attempt(rootwindow,usrentv,pwdetv):
    userentryvalue = str(usrentv.get())
    passwordentryvalue = str(pwdetv.get())
    x = str(userentryvalue)
    y = str(passwordentryvalue)
    if login_info_verify(x,y):
        cleanWindow(rootwindow)
    elif login_info_verify(x,y) == False:
        if x == "" or y == "":# if entryValueChecker(x, y) == True :
            messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
        elif " " in x or " " in y:
            messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
        elif (x.isascii() == False) or (y.isascii() == False):
            messagebox.showerror(title='ASCII Error', message="All charcters has to be on a ASCII format")
        elif login_info_verify(x,y) == False:
            messagebox.showinfo(title='Password Error', message="Wrong password")
        else:
            messagebox.showinfo(title="User Error", message="The Typed User Doesn't Exist")

# -------------------------------------------------------------------------------------
