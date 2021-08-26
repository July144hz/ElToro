import tkinter
import pymysql
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def tarjetas():
    bd= pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python')
    fcursor = bd.cursor()
    def main():
        global l1,l2,l3,e1,e2,btn1,fotoLogin,root
        root = Tk()
        fondo='#71b4fd'
        root.config(bg=fondo)
        root.title("DataBase")
        root.geometry("500x500")
        root.resizable(False,False)

        logo = ImageTk.PhotoImage(Image.open('resources/bbv.png'))
        l1=Label(image=logo,bg=fondo)
        l1.pack()

        l2=Label(text="USUARIO",bg=fondo,font=("bahnschrift",20))
        l2.pack(pady=5)
        userEntry = StringVar()
        e1=Entry(textvariable=userEntry,justify=CENTER,font=('calibri',20))
        e1.pack(pady=5)

        l3=Label(text="CONTRASEÑA",bg=fondo,font=("bahnschrift",20))
        l3.pack(pady=5)
        passEntry = StringVar()
        e2=Entry(textvariable=passEntry,justify=CENTER,font=('calibri',20),show='*')
        e2.pack(pady=5)

        fotoLogin=ImageTk.PhotoImage(Image.open('resources/login4.png'))
        btn1=Button(bg=fondo,activebackground=fondo,borderwidth=0,highlightthickness=0,highlightcolor=fondo,image=fotoLogin,pady=50,padx=50, command=lambda:(verificar(userEntry.get(),passEntry.get())))
        btn1.pack(pady=5)

        root.mainloop()
        pass

    def verificar(var1,var2):
        fcursor.execute("SELECT * FROM tarjetas WHERE usuario = '"+var1+"' and password = '"+var2+"'")
        if fcursor.fetchall():
            messagebox.showwarning(message="Has logeado con exito", title="SI")
            l1.destroy(),l2.destroy(),l3.destroy(),btn1.destroy(),e1.destroy(),e2.destroy()
        else:
            messagebox.showerror(message="Error, Intente denuevo", title="NO")
        pass

    main()

    pass

<<<<<<< HEAD
def hola():
    print("hola")


=======
    def ols():
        print("Nashe")
>>>>>>> 16625c9f8124f5e8263037651aad23950b7b03f3

tarjetas()