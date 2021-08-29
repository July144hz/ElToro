import tkinter
import pymysql
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def tarjetas():
    global root
    root = Tk()
    bd= pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='python')
    fcursor = bd.cursor()
    def main():
        global l1,l2,l3,e1,e2,btn1,fotoLogin,root
        
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
            global saldo
            fcursor.execute("SELECT saldo FROM tarjetas WHERE usuario = '"+var1+"' and password = '"+var2+"'")
            for i in fcursor:
                #print(i)
                saldo = i[0]
                #print(saldo, type(saldo))
            fondo = "#7fffd4"
            
            messagebox.showinfo(message="Has logeado con exito", title="BANCO BILBAO VIZCAYA")
            
            l1.destroy(),l2.destroy(),l3.destroy(),btn1.destroy(),e1.destroy(),e2.destroy()
            root.configure(bg=fondo)
            l4=Label(pady=50,bg=fondo)
            l4.pack()
            l5=Label(bg=fondo,font=("bahnschrift",20),text="Que desea hacer?")
            l5.pack()
            btn2=Button(text="INGRESAR MONTO",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D",command=lambda:(imonto(),btn2.destroy(),btn3.destroy(),btn4.destroy()))
            btn2.pack(pady=2)
            btn3=Button(text="RETIRAR MONTO",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D",padx=12, command = lambda :(btn2.destroy(), btn3.destroy(), btn4.destroy(), rmonto()))
            btn3.pack(pady=2)
            btn4=Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C",padx=75,command=lambda:(volverinicio()))
            btn4.pack(pady=2)
            def volverinicio():
                btn4.destroy(),btn3.destroy(),btn2.destroy(),l5.destroy(),l4.destroy()
                main()
            pass

            def imonto():
                l5.config(text="Que cantidad desea ingresar?")
                monto= StringVar()
                e3=Entry(textvariable=monto,justify=CENTER,font=('calibri',20))
                e3.bind('<Return>', lambda x:ingreso(monto))
                e3.pack()
                btn5=Button(text="INGRESAR",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D",command=lambda:(l8.configure(text=f"Saldo actual:{saldo+20}"),ingreso(monto)))
                btn5.pack()
                btn7 = Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C",command=lambda:())
                btn7.pack()
                l8 = Label(text=f"Saldo actual:{saldo}",font=("consola",20),bg=fondo,activebackground=fondo)
                l8.pack()
                pass

            def ingreso(monto):
                global saldo
                fcursor.execute("UPDATE tarjetas SET saldo = (saldo+'"+monto.get()+"') WHERE usuario = '"+var1+"' and password = '"+var2+"'")
                try:
                    saldo= saldo + float(monto.get())
                except:
                    messagebox.showerror(message = "Ha ocurrido un error, intente ingresar otro valor.", title="BANCO BILBAO VIZCAYA")
                pass

            def rmonto():
                l5.config(text="Que cantidad desea retirar?")
                monto = StringVar()
                e4 = Entry(textvariable=monto, justify=CENTER, font=('calibri', 20))
                e4.bind('<Return>', lambda x:retiro(monto))
                e4.pack()
                btn6 = Button(text="RETIRAR", font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D", command=lambda:(retiro(monto)))
                btn6.pack()
                btn8 = Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C")
                btn8.pack()
                l7 = Label(text=f"Saldo actual:{saldo}", font=("consola",20),bg=fondo,activebackground=fondo)
                l7.pack()
                pass

            def retiro(monto):
                global saldo
                fcursor.execute("UPDATE tarjetas SET saldo = (saldo - '"+monto.get()+"') WHERE usuario = '"+var1+"' and password = '"+var2+"'")
                try:
                    saldo = saldo - int(monto.get())
                except:
                    messagebox.showerror(message="Ha ocurrido un error, intente ingresar otro valor.", title="BANCO BILBAO VIZCAYA")
                pass

        else:
            messagebox.showerror(message="Error, Intente denuevo", title="BANCO BILBAO VIZCAYA")
        pass

    main()

    pass

tarjetas()


