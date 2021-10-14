from os import name as os_name
from functions import *
from tkinter import *
from PIL import ImageTk, Image


class app():
    def __init__(self):

        self.container = Tk()
        self.zoomed(self.container)

        self.container.resizable(True, True)

        self.menu_frame = Frame(self.container, relief= FLAT)
        self.register_frame = Frame(self.container, relief=FLAT)
        self.loggin_frame = Frame(self.container, relief=FLAT)

        self.width = self.container.winfo_screenwidth()
        self.height = self.container.winfo_screenheight()

        #C = Canvas(self.container, bg="blue", height=250, width=300)
        
        bg_img = Image.open('images/bg.jpeg')
        bg_img = bg_img.resize((self.width, self.height), Image.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(bg_img)

        open_eye = Image.open('images/open.png')
        open_eye = open_eye.resize((self.height // 16, self.height // 16), Image.ANTIALIAS)

        closed_eye = Image.open('images/closed.png')
        closed_eye = closed_eye.resize((self.height // 16, self.height // 16), Image.ANTIALIAS)

        self.closed = ImageTk.PhotoImage(closed_eye)
        self.open = ImageTk.PhotoImage(open_eye)
        #-------------------------------------------------------------------------------------
        # BG IMAGE (Need to put it before the other widgets)
        bg_label1 = Label(self.menu_frame, image=photoimg)
        bg_label1.place(x=0, y=0)
        
        #WIDGETS menu_frame
        label_program = Label(self.menu_frame, text='Bem vindo ao GerenciaFácil!', font='Arial 50', relief='sunken')
        registerbutton = Button(self.menu_frame, text='Register', font='Arial 50', padx=50, pady=10, command=lambda: [self.show(self.register_frame, self.menu_frame)])
        logginbutton = Button(self.menu_frame, text='Loggin', font='Arial 50', padx=75, pady=10, command=lambda: self.show(self.loggin_frame, self.menu_frame))

        #LAYOUT menu_frame
        self.menu_frame['width'] = self.width
        self.menu_frame['height'] = self.height

        label_program.place(relx=0.5, rely=0.2, anchor=CENTER)
        registerbutton.place(relx=0.5, rely=0.45, anchor=CENTER)
        logginbutton.place(relx=0.5, rely=0.67, anchor=CENTER)
        
        #-------------------------------------------------------------------------------------
        # BG IMAGE (Need to put it before the other widgets)
        bg_label2 = Label(self.register_frame, image=photoimg)
        bg_label2.place(x=0, y=0)           
        
        #WIDGETS register_frame
        r_label_user = Label(self.register_frame, text='User:', font='Arial 40')
        r_label_password = Label(self.register_frame, text='Password:', justify="right", font='Arial 40')
        r_user_entry = Entry(self.register_frame, font='Arial 40')
        r_password_entry = Entry(self.register_frame, font='Arial 40')
        r_register_button = Button(self.register_frame, text='Register', font='Arial 40', command=lambda: register_attempt(self.container, r_user_entry, r_password_entry))
        r_goback_button = Button(self.register_frame,  text='Go Back', font='Arial 40', command=lambda: self.show(self.menu_frame, self.register_frame))

        self.r_bool = False

        self.r_check_btn = Button(self.register_frame, image=self.open, command=lambda: self.change_eye(r_password_entry, 'r'))

        #LAYOUT register_frame     
        self.register_frame['width'] = self.width
        self.register_frame['height'] = self.height

        r_label_user.place(relx=0.25, rely=0.3, anchor=CENTER)
        r_label_password.place(relx=0.206, rely=0.5, anchor=CENTER)
        r_user_entry.place(relx=0.55, rely=0.3, anchor=CENTER)
        r_password_entry.place(relx=0.55, rely=0.5, anchor=CENTER)
        r_register_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        r_goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)
        self.r_check_btn.place(relx=0.8, rely=0.5, anchor=CENTER)

        #-------------------------------------------------------------------------------------
        # BG IMAGE (Need to put it before the other widgets)
        bg_label3 = Label(self.loggin_frame, image=photoimg)
        bg_label3.place(x=0, y=0)           
        
        #WIDGETS loggin_frame
        l_label_user = Label(self.loggin_frame, text='User:', font='Arial 40')
        l_label_password = Label(self.loggin_frame, text='Password:', justify="right", font='Arial 40')
        l_user_entry = Entry(self.loggin_frame, font='Arial 40')
        l_password_entry = Entry(self.loggin_frame, font='Arial 40')
        l_loggin_button = Button(self.loggin_frame, text='Loggin', font='Arial 40', command=lambda: loggin_attempt(self.container, l_user_entry, l_password_entry))
        l_goback_button = Button(self.loggin_frame,  text='Go Back', font='Arial 40', command=lambda: self.show(self.menu_frame, self.loggin_frame))

        self.l_bool = False
        self.l_check_btn = Button(self.loggin_frame, image=self.open, command=lambda: self.change_eye(l_password_entry, 'l'))
        

        #LAYOUT loggin_frame     
        self.loggin_frame['width'] = self.width
        self.loggin_frame['height'] = self.height

        l_label_user.place(relx=0.25, rely=0.3, anchor=CENTER)
        l_label_password.place(relx=0.206, rely=0.5, anchor=CENTER)
        l_user_entry.place(relx=0.55, rely=0.3, anchor=CENTER)
        l_password_entry.place(relx=0.55, rely=0.5, anchor=CENTER)
        l_loggin_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        l_goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)
        self.l_check_btn.place(relx=0.8, rely=0.5, anchor=CENTER)

        #-------------------------------------------------------------------------------------
        #GUI
        self.show(self.menu_frame)
        self.container.mainloop() 


    def change_eye(self, passwrd_entry: Entry, place: str):
        if place == 'l':
            boolean = self.l_bool
            if self.l_bool:        
                self.l_bool = False
            elif not self.l_bool: 
                self.l_bool = True

        elif place == 'r':
            boolean = self.r_bool
            if self.r_bool: 
                self.r_bool = False
            elif not self.r_bool:
                self.r_bool = True

        if boolean:
            passwrd_entry.config(show='')
            if place == 'l':
                self.l_check_btn.config(image=self.open)
            elif place == 'r':
                self.r_check_btn.config(image=self.open)
             
        elif not boolean:
            passwrd_entry.config(show='*')
            if place == 'l':
                self.l_check_btn.config(image=self.closed)
            elif place == 'r':
                self.r_check_btn.config(image=self.closed)


    def zoomed(self, window: Tk):
        """ 
        Windows and Linux compatible full window creation option

        -> window: Toplevel widget (CLASSNAME)
        """
        if os_name == 'nt': 
            window.state('zoomed') 
        else: 
            window.attributes('-zoomed', True)


    def show(self, frame_a_ir: Frame, frame_atual: Frame = None):
        if frame_atual is not None:
            frame_atual.pack_forget()
        frame_a_ir.pack()
    

if __name__ == "__main__":
    app()
