from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import time

class MainMenu():
    def __init__(self,root,UserName):
        self.username = UserName
        self.root = root
        self.AddedImages = []
        #self.root.geometry("800x500")
        self.root.configure(background = "grey")
        self.TOMAINED()

        self.root.mainloop()
        

    def TOMAINED(self):
        self.MainFrame = Frame(self.root) 
        self.MainFrame.pack(side = BOTTOM,expand = True,fill = Y)

        self.Header(self.username)   

        #self.Body()
        self.frame()
        self.footer()

        self.root.mainloop()


    def Header(self, UserName):
        
        def make_label(master, x, y, h , w, *args, **kwargs):
            f = Frame(master, height = h, width = w)
            f.pack_propagate(0)
            f.place(x = x, y = y)
            label = Label(f,*args,**kwargs)
            label.pack(fill = BOTH, expand = 1)
            return label
        
        f = Frame(self.MainFrame,bg = "red")
        f.pack(side = TOP,fill = X)
        
        #f.grid(row = 0,column = 0,sticky = "SE")

        Label(f,text = f"Hoş Geldin {UserName}",background = "red").pack()

        #Topper = make_label(self.root, 0, 0, 20, 800,text = f"Mr {UserName}, Wellcome", background = "red")
        #Label(Topper, text = "Last login : 5.03.2021").pack(anchor = NE)


        # Menü ekleme ve fonksiyonlar #

        # --- Fonksiyonlar --- #

        def show_cash():
            cashMenu = Toplevel()
            cash = Label(cashMenu, text = "Şu kadar paranız var: ").pack()

        # --- Menüler --- #

        header_menu = Menu(self.root)
        self.root.config(menu = header_menu)
       

        account_menu = Menu(header_menu)
        header_menu.add_cascade(label = "MyAccount" ,menu = account_menu)
        account_menu.add_command(label = "My Cash",command = show_cash)
        account_menu.add_command(label = "LogOut",command = self.root.quit)

    def Body(self):

        MidImg = ImageTk.PhotoImage(Image.open("MyTkinter/Animasyon Çember/don1.png").resize((450,300)))
        #MidImg = ImageTk.PhotoImage(Image.open("MyTkinter/images/aot1.jpg").resize((450,300)))

        
        labelImg = Label(self.MainFrame,image = MidImg)
        labelImg.image = MidImg
        #labelImg.pack(side = "top",fill = "both", expand = "yes")
        labelImg.grid(columnspan = 2,sticky = "N",padx = 180)

        add_money = Button(self.MainFrame, text = "Para Ekle")
        add_money.place(x = 345,y = 305)

        def w():
            print(self.root.winfo_height())

        draw_money = Button(self.MainFrame, text = "Para Çek",command =w)
        draw_money.place(x = 415,y = 305)

    def frame(self):

        f = LabelFrame(self.MainFrame,text = "Resimler",pady = 10)
        f.pack(pady = 100,fill = Y,padx = 20)

        MidImg = ImageTk.PhotoImage(Image.open("MyTkinter/Animasyon Çember/don1.png").resize((450,300)))
        MidImg = ImageTk.PhotoImage(Image.open("MyTkinter/images/aot1.jpg").resize((450,300)))
        
        labelImg = Label(f,image = MidImg)
        labelImg.image = MidImg
        labelImg.pack()
        
        label = Button(f,text = "next")
        label.pack(expand = True,fill = BOTH,side = LEFT)

        button = Button(f,text = "frame")
        button.pack(expand = True,fill =BOTH,side = LEFT)

        but = Label(f)
    
    def footer(self):

        f = Frame(self.MainFrame,bg = "red")
        f.pack(side = BOTTOM,fill = X)

        # Profilime giden fonksiyon

        def ToMyProfile():
            self.MainFrame.destroy()
            self.MyProfile()

        Button(f,text = "Profilim",command = ToMyProfile).pack()


    def MyProfile(self):
        self.rowspan = 4
        #Resimlerin gösterileceği frame'i oluşturuyoruz.
        self.myProfileFrame = Frame(self.root)
        self.myProfileFrame.grid(columnspan = 4,rowspan = self.rowspan)

        #resimlerin olduğu dosyaya os yardımı iniyoruz.
    
        maindir = os.path.dirname(__file__)
        imgs_dir = os.path.join(maindir,"images")
        self.col = 0
        self.row = 0
        for filename in os.listdir(imgs_dir):
            MidImg = ImageTk.PhotoImage(Image.open(f"MyTkinter/images/{filename}").resize((150,100)))
            labelImg = Label(self.myProfileFrame,image = MidImg)
            labelImg.image = MidImg
            labelImg.grid(row = self.row, column = self.col)
            self.col += 1
            if self.col % 3 == 0:
                self.row += 1 
                self.col = 0
        
        

        if self.AddedImages:
            for photo in self.AddedImages[::2]:
                print(self.AddedImages)
                MidImg = ImageTk.PhotoImage(Image.open(f"MyTkinter/images/{photo}").resize((150,100)))
                labelImg = Label(self.myProfileFrame,image = MidImg)
                labelImg.image = MidImg
                labelImg.grid(row = self.row, column = self.col)
                self.col += 1
                if self.col % 3 == 0:
                    self.row += 1 
                    self.col = 0
                

        # Resim Yükleme Fonksiyonu

        def AskDialog():
            
            initial_ = "C:/Users/Ömer Dizmen/Desktop/Visual Studio Code Python/MyTkinter/images" 
            self.root.filename = filedialog.askopenfilename(initialdir = initial_,title = "Resim Yükle",filetypes = ( ("all files", "*.*"), ))
            
            print(self.root.filename,"bura bakmaz")
            if self.root.filename != "":
                self.AddedImages.append(self.root.filename.split("/")[len(self.root.filename.split("/"))-1])
                MidImg = ImageTk.PhotoImage(Image.open(self.root.filename).resize((150,100)))
                self.AddedImages.append(MidImg)
                labelImg = Label(self.myProfileFrame,image = MidImg)
                labelImg.image = MidImg
                labelImg.grid(row = self.row, column = self.col)
            
            else:
                pass

            


            self.col += 1
            if self.col % 3 == 0:
                self.row += 1 
                self.col = 0
            
            if self.col >= 2:
                self.rowspan += 1
                
                self.but.grid_forget()
                self.to_main.grid_forget()
                self.b.grid_forget()
            
                self.but = Button(self.myProfileFrame,text = "Ana Menüye Dön",command = TOMAIN)
                self.but.grid(row = self.rowspan -1,column = 0,sticky = E+W)

                self.to_main = Button(self.myProfileFrame,text = "Resim Ekle", command = AskDialog)
                self.to_main.grid(row = self.rowspan -1, column = 1,sticky = E+W)

                self.b = Button(self.myProfileFrame,text = "aa")
                self.b.grid(row = self.rowspan, column = 0,sticky = E+W)


        def TOMAIN():
            self.myProfileFrame.destroy()
            self.TOMAINED()

        self.but = Button(self.myProfileFrame,text = "Ana Menüye Dön",command = TOMAIN)
        self.but.grid(row = self.rowspan -1,column = 0,sticky = E+W)

        self.to_main = Button(self.myProfileFrame,text = "Resim Ekle", command = AskDialog)
        self.to_main.grid(row = self.rowspan -1, column = 1,sticky = E+W)

        self.b = Button(self.myProfileFrame,text = "aa")
        self.b.grid(row = self.rowspan, column = 0,sticky = E+W)

if __name__ == "__main__":
    
    root = Tk()
    name = "Niimen"
    h = MainMenu(root, name)

else:
    print("name is not equal main")
        
