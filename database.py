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
        e2.bind('<Return>',lambda x:(verificar(userEntry.get(),passEntry.get())))
        e2.pack(pady=5)

        fotoLogin=ImageTk.PhotoImage(Image.open('resources/login4.png'))
        btn1=Button(bg=fondo,activebackground=fondo,borderwidth=0,highlightthickness=0,highlightcolor=fondo,image=fotoLogin,pady=50,padx=50, command=lambda:(verificar(userEntry.get(),passEntry.get())))
        btn1.pack(pady=5)

        root.mainloop()
        pass

    def verificar(var1,var2):
        fcursor.execute("SELECT * FROM tarjetas WHERE usuario = '"+var1+"' and password = '"+var2+"'")
        if fcursor.fetchall():
            fondo = "#61E9A3"
            messagebox.showwarning(message="Has logeado con exito", title="SI")
            l1.destroy(),l2.destroy(),l3.destroy(),btn1.destroy(),e1.destroy(),e2.destroy()
            root.configure(bg=fondo)
            l4=Label(pady=50,bg=fondo)
            l4.pack()
            l5=Label(bg=fondo,font=("bahnschrift",20),text="Que desea hacer?")
            l5.pack()
            btn2=Button(text="INGRESAR MONTO",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D")
            btn2.pack()
            btn3=Button(text="RETIRAR MONTO",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D",padx=12)
            btn3.pack()
            btn4=Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C",padx=75)
            btn4.pack()



        else:
            messagebox.showerror(message="Error, Intente denuevo", title="NO")
        pass

    main()

    pass

tarjetas()