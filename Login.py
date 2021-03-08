from tkinter import *
from PIL import ImageTk, Image
import proc_mainmenu as pm
from tkinter import messagebox

class LogIn():
    page_count = 0
    def __init__(self,root):
        self.root = root
        self.root.title("Giriş/Kayıt")
        self.Submit()
        self.SignIn()

        self.root.mainloop()

    def MainMenu_(self,UserName = None):
        self.root.destroy()
        root = Tk()
        pm.MainMenu(root,UserName)

    
    def Submit(self):
        username = Label(self.root, text = "Kullanıcı Adınızı Girin:")
        username.grid(row = 0, column = 0)
        e_username = Entry()
        e_username.grid(row = 0, column = 1,ipadx = 50,columnspan = 3)
        e_username.insert(END, "Kullanıcı Adınızı girin:")

        mail = Label(self.root, text = "Postanızı girin:")
        mail.grid(row = 1, column = 0)
        e_mail = Entry()
        e_mail.grid(row = 1, column = 1,ipadx = 50,columnspan = 3)
        e_mail.insert(0, "Postanızı Girin:")
        
        password_ = Label(self.root, text = "Şifrenizi Girin:")
        password_.grid(row = 2, column = 0)
        e_password_ = Entry()
        e_password_.grid(row = 2, column = 1,ipadx = 50,columnspan = 3)
        e_password_.insert(0, "Şifrenizi Girin:")

        hack = Button(self.root , text = "Hack",command = lambda: self.MainMenu_(e_username.get()))
        hack.grid(row = 3, column = 0)

        def GetAll():
            
            user_get = e_username.get()
            mail_get = e_mail.get()
            password_get = e_password_.get()
            print(user_get,mail_get,password_get)

            self.LogInControl(user_get, mail_get, password_get)


        
        def UserDiscDisap(event):
            user_cur = e_username.get()
            
            if user_cur == "Kullanıcı Adınızı girin:":
                e_username.delete(0, END)
            elif user_cur == "":
                e_username.insert(END, "Kullanıcı Adınızı girin:")
        
        def MailDiscDisap(event):
            mail_cur = e_mail.get()
            if mail_cur == "Postanızı Girin:":
                e_mail.delete(0, END)

            elif mail_cur == "":
                e_mail.insert(END, "Postanızı Girin:")

        def PassDiscDisap(event):
            e_password_.config(show = "*")
            password_cur = e_password_.get()
            if password_cur == "Şifrenizi Girin:":
                e_password_.delete(0, END)

            elif password_cur == "":
                e_password_.insert(END, "Şifrenizi Girin:")     
                e_password_.config(show = "")


        e_username.bind("<FocusIn>",UserDiscDisap)
        e_username.bind("<FocusOut>",UserDiscDisap)

        e_mail.bind("<FocusIn>",MailDiscDisap)
        e_mail.bind("<FocusOut>",MailDiscDisap)

        e_password_.bind("<FocusIn>",PassDiscDisap)
        e_password_.bind("<FocusOut>",PassDiscDisap)

        allsubmit = Button(self.root, text = "Giriş Yap", command = GetAll)
        allsubmit.grid(row = 3, column = 1)

    def SignIn(self):

        def close_sign():
            page.destroy()
            page.grab_release()

            self.page_count += -1
        
        def sign_page():
            
            if self.page_count < 1:
                global page
                global e_user
                page = Toplevel()
                page.grab_set()

                user_name = Label(page, text = "Kullanıcı adınızı girin:")
                user_name.grid(row = 0, column = 0)

                e_user = Entry(page)
                e_user.insert(0, "Kullanıcı adınızı girin:")
                e_user.grid(row = 0, column = 1,ipadx = 50,columnspan = 3)

                mail = Label(page, text = "Postanızı girin:")
                mail.grid(row = 1, column = 0)

                e_mail = Entry(page)
                e_mail.insert(0, "Postanızı girin:")
                e_mail.grid(row = 1, column = 1,ipadx = 50,columnspan = 3)

                passw =  Label(page, text = "Şifrenizi girin:")
                passw.grid(row = 2, column = 0)

                e_passw = Entry(page)
                e_passw.insert(0, "Şifrenizi girin:")
                e_passw.grid(row = 2, column = 1,ipadx = 50,columnspan = 3)
             

                def PasswDisap(event):
                    e_passw.config(show = "*")
                    cur = e_passw.get()
                    if cur == "Şifrenizi girin:":
                        e_passw.delete(0,END)
                    elif cur == "":
                        e_passw.insert(END,"Şifrenizi girin:")
                        e_passw.config(show = "")

                def MailDisap(event):
                    cur = e_mail.get()
                    if cur == "Postanızı girin:":
                        e_mail.delete(0,END)
                    elif cur == "":
                        e_mail.insert(END,"Postanızı girin:")

                def UserDisap(event):
                    user = e_user.get()
                    if user == "Kullanıcı adınızı girin:":
                        e_user.delete(0,END)
                    elif user == "":
                        e_user.insert(END,"Kullanıcı adınızı girin:")
                
                def FinalSubmit():
                    e_user.get()
                    e_mail.get()
                    e_passw.get()
                    self.AddUserData(e_user.get(), e_mail.get(), e_passw.get())

                    if e_user.get() != "Kullanıcı adınızı girin:" and e_mail.get() != "Postanızı girin:" and e_passw.get() != "Şifrenizi girin:":
                        page.destroy()
                        self.page_count -= 1
                    else:
                        messagebox.showerror(title = "Eksik Bilgi", message="Lütfen Şifre,Mail veya Kullanıcı adı alanlarını giriniz!")


                self.page_count += 1

                e_user.bind("<FocusIn>",UserDisap)
                e_user.bind("<FocusOut>",UserDisap)

                e_mail.bind("<FocusIn>",MailDisap)
                e_mail.bind("<FocusOut>",MailDisap)

                e_passw.bind("<FocusIn>",PasswDisap)
                e_passw.bind("<FocusOut>",PasswDisap)

                page.protocol("WM_DELETE_WINDOW",close_sign)

                submit = Button(page, text = "Tamam",command = FinalSubmit)
                submit.grid(row = 3, column = 1)

            else:
                pass

        
        sign_button = Button(self.root, text = "Kayıt Olmak İçin Tıklayınız", command = sign_page)
        sign_button.grid(row = 3,column = 2)
    
    def AddUserData(self,username,mail,password):
        import os
        dir_path = os.path.dirname(__file__)
        joined = os.path.join(dir_path,"All_Accounts")
        account_txt = os.path.join(joined, "Accounts.txt")

        user_passed = False
        email_passed = False
        passw_pass = False

        with open(account_txt,"a",encoding="utf-8") as file:
            if username != "Kullanıcı adınızı girin:":
                user_passed = True
              
            else:
                pass

            if mail != "Postanızı girin:":
                email_passed = True
            else:
                password
            if password != "Şifrenizi girin:":
                passw_pass = True
            
            if user_passed and email_passed and passw_pass:
                file.write(username + "-" + mail + "-" + password + "-"+ str(0)+"\n")
    
    def LogInControl(self,UserName,Email,Password):
        import os
        dir_path = os.path.dirname(__file__)
        joined = os.path.join(dir_path,"All_Accounts")
        account_txt = os.path.join(joined, "Accounts.txt")

        acc = (acc for acc in open(account_txt,"r",encoding="utf-8").readlines())

        for a in acc:
            spl = a.split("-")
            if UserName == spl[0] and Email == spl[1] and Password == spl[2]:
                print("main menü girdik")
                self.MainMenu_(spl[0])
                break
        else:
            messagebox.showerror(title = "Eksik Bilgi", message="Şifre,Mail veya Kullanıcı adı yanlış!")
           
    
# This function is for create random accounts in order to check my LogInControl is working

def random(range_):
    import os
    dir_path = os.path.dirname(__file__)
    joined = os.path.join(dir_path,"All_Accounts")
    account_txt = os.path.join(joined, "Accounts.txt")
    import random
    all_names = """ Yaşar, Ayhan, Dursun, İsmet, Muzaffer, Ümit, Özgür, İlhan, Hikmet, Yüksel, Özcan, Fikret, Cihan, Şerif, Deniz, Servet, Yücel, Sefa, Hidayet, Sezer, Olcay, Saffet, Güngör, Durdu, Günay, Ömür, İlkay, Kamuran, Kudret, Satı, Şenel, Elvan, Seyhan, Zülfü, Muhterem, Güner"""
    spl = all_names.split(",")
    c = 0
    for names in range(range_):
        a = random.choice(spl).split()
        a = "".join(a).lower()
        print(a)
        if a.startswith("i̇"):
            a = a.replace("i̇","i")
        

        
        with open(account_txt,"a",encoding= "utf-8") as f:
            f.write(a + "-" + a +"@gmail.com" + "-" + a + "-"+ str(0)+"\n")
        
#random(100)                  

root = Tk()
l = LogIn(root)
