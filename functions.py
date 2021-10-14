from tkinter import *
from tkinter import messagebox
from ConnectToDB import *
from itertools import chain


def login_info_verify(user, password):
    c.execute(f'SELECT PASSWORD FROM LOGGINDATA WHERE {user=}')
    passwordDB = flatit(c.fetchall())
    try:
        return True if password in passwordDB[0] else False
    
    except IndexError:
        return False


def selectUser():
    c.execute("SELECT USER FROM LOGGINDATA")


def selectPassword():
    c.execute("SELECT PASSWORD FROM LOGGINDATA")


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children(): # Perguntar sobre .isisntance()
            _list.extend(item.winfo_children())

    return _list


def registernow(mainwindow,usrentv,pwdentv):
    c.execute("SELECT * FROM LOGGINDATA")
    c.execute("INSERT INTO LOGGINDATA (USER, PASSWORD) VALUES (?, ?)", (usrentv, pwdentv))
    conn.commit()
    messagebox.showinfo(title="Successful",
                        message="Successfully Registered")
    mainwindow.update()


def flatit(listtoflat):
    return list(chain(listtoflat))


def usersList(): 
    selectUser()
    return flatit([queryresult for queryresult in c.fetchall()])


def passwordList():
    selectPassword()
    return flatit([queryresult for queryresult in c.fetchall()])


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
    

def register_attempt(rootwindow,usrentv, pwdetv):
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
        if entryValueChecker(x, y):
            messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
        elif (" " in x) or (" " in y):
            messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
        elif (x.isascii() == False) or (y.isascii() == False):
            messagebox.showerror(title='ASCII Error', message="All charcters has to be on a ASCII format")
        else:
            registernow(rootwindow, x, y)    


def loggin_attempt(rootwindow,usrentv,pwdetv):
    userentryvalue = str(usrentv.get())
    passwordentryvalue = str(pwdetv.get())
    x = str(userentryvalue)
    y = str(passwordentryvalue)

    if login_info_verify(x,y):
        widget_list = all_children(rootwindow)
        for item in widget_list:
            item.destroy()

    elif not login_info_verify(x,y):
        if x == "" or y == "":
            messagebox.showerror(title="Empty Field", message="Please fill both of the fields")
        elif " " in x or " " in y:
            messagebox.showerror(title="Space error", message="Remove the spaces on the fields")
        elif (x.isascii() == False) or (y.isascii() == False):
            messagebox.showerror(title='ASCII Error', message="All charcters has to be on a ASCII format")
        elif login_info_verify(x,y) == False:
            messagebox.showinfo(title='Password Error', message="Wrong password")
        else:
            messagebox.showinfo(title="User Error", message="The Typed User Doesn't Exist")
