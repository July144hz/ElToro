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

        salir = ImageTk.PhotoImage(Image.open('resources/salir.png'))
        salir2 = ImageTk.PhotoImage(Image.open('resources/salir2.png'))
        ingresar = ImageTk.PhotoImage(Image.open('resources/ingresar.png'))
        retirar = ImageTk.PhotoImage(Image.open('resources/retirar.png'))


        fcursor.execute("SELECT * FROM tarjetas WHERE usuario = '"+var1+"' and password = '"+var2+"'")
        if fcursor.fetchall():
            global saldo
            fcursor.execute("SELECT saldo FROM tarjetas WHERE usuario = '"+var1+"' and password = '"+var2+"'")
            for i in fcursor:
                #print(i)
                saldo = int(i[0])
                #print(saldo, type(saldo))
            fondo = "#7fffd4"
            
            messagebox.showinfo(message="Has iniciado sesion exitosamente", title="BANCO BILBAO VIZCAYA")
            l4=Label(pady=35,bg=fondo)
            l4.pack()
            def principal():
                global btn2, btn1, btn3, btn4, l5, l4,btnsalir1
                l1.destroy(),l2.destroy(),l3.destroy(),btn1.destroy(),e1.destroy(),e2.destroy()
                root.configure(bg=fondo)
                l5=Label(bg=fondo,font=("bahnschrift",20),text="Que desea hacer?")
                l5.pack()
                btn2=Button(text="INGRESAR MONTO",image=ingresar,font=("bahnschrift",20),bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo,command=lambda:(imonto(),btn2.destroy(),btn3.destroy(),btn4.destroy()))
                btn2.pack(pady=2)
                btn3=Button(text="RETIRAR MONTO",image=retirar,font=("bahnschrift",20),bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo, command = lambda :(btn2.destroy(), btn3.destroy(), btn4.destroy(), rmonto()))
                btn3.pack(pady=2)
                btn4=Button(text="SALIR",image=salir,font=("bahnschrift",20),bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo,command=lambda:(volverinicio()))
                btn4.pack(pady=2)
                btnsalir1=Button(image=salir2,bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo,command=volverinicio)
                btnsalir1.place(x=15,y=15)
            def volverinicio():
                global btnsalir1
                btn4.destroy(),btn3.destroy(),btn2.destroy(),l5.destroy(),l4.destroy(),btnsalir1.destroy()
                main()

            principal()

            def volverprincipal():
                global btn5,e3,btn7, l5, l8, btnsalir2
                btn5.destroy(),e3.destroy(),btn7.destroy(),l5.destroy(),l8.destroy(),btnsalir2.destroy(),principal()

            def imonto():
                global l8, btnsalir2,btn5,e3,btn7, l5, l8, btnsalir2
                l5.config(text="Que cantidad desea ingresar?")
                monto= StringVar()
                btnsalir1.destroy()
                e3=Entry(textvariable=monto,justify=CENTER,font=('calibri',20))
                e3.bind('<Return>', lambda x:ingreso(monto))
                e3.pack()
                btnsalir2=Button(image=salir2,bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo,command=lambda:(volverprincipal()))
                btnsalir2.place(x=15,y=15)
                btn5=Button(text="INGRESAR",font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D",command=lambda:(l8.configure(text=f"Saldo actual:{saldo+20}"),ingreso(monto)))
                btn5.pack()
                btn7 = Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C",command=lambda:(btn5.destroy(),e3.destroy(),btn7.destroy(),l5.destroy(),l8.destroy(),principal()))
                btn7.pack()
                l8 = Label(text=f"Saldo actual:{saldo}",font=("consola",20),bg=fondo,activebackground=fondo)
                l8.pack()
                pass
            
            def ingreso(monto):
                global saldo
                fcursor.execute("UPDATE tarjetas SET saldo = (saldo+'"+monto.get()+"') WHERE usuario = '"+var1+"' and password = '"+var2+"'")
                try:
                    saldo= saldo + float(monto.get())
                    l8.configure(text=f"Saldo actual:{saldo}")
                except:
                    messagebox.showerror(message = "Ha ocurrido un error, intente ingresar otro valor.", title="BANCO BILBAO VIZCAYA")
                    l8.configure(text=f"Saldo actual:{saldo}")

            def volverprincipal2():
                global e4,btn6,btn8,l7,btnsalir2
                e4.destroy(),btn6.destroy(),btn8.destroy(),l7.destroy(),btnsalir2.destroy(),l5.destroy(),principal()

            def rmonto():
                global e4,btn6,btn8,l7,btnsalir2
                l5.config(text="Que cantidad desea retirar?")
                monto = StringVar()
                btnsalir1.destroy()
                btnsalir2=Button(image=salir2,bg=fondo,activebackground=fondo,padx=75,borderwidth=0,highlightthickness=0,highlightcolor=fondo,command=lambda:(volverprincipal2()))
                btnsalir2.place(x=15,y=15)
                e4 = Entry(textvariable=monto, justify=CENTER, font=('calibri', 20))
                e4.bind('<Return>', lambda x:retiro(monto))
                e4.pack()
                btn6 = Button(text="RETIRAR", font=("bahnschrift",20),bg="#029D4D",activebackground="#029D4D", command=lambda:(retiro(monto)))
                btn6.pack()
                btn8 = Button(text="SALIR",font=("bahnschrift",20),bg="#E33F2C",activebackground="#E33F2C", command=lambda : (l5.destroy(),e4.destroy(),btn8.destroy(),l7.destroy(),btn6.destroy(),principal()))
                btn8.pack()
                l7 = Label(text=f"Saldo actual:{saldo}", font=("consola",20),bg=fondo,activebackground=fondo)
                l7.pack()
                pass

            def retiro(monto):
                global saldo
                fcursor.execute("UPDATE tarjetas SET saldo = (saldo-'"+monto.get()+"') WHERE usuario = '"+var1+"' and password = '"+var2+"'")
                try:
                    saldo = saldo - float(monto.get())
                    l8.configure(text=f"Saldo actual:{saldo}")
                except:
                    messagebox.showerror(message="Ha ocurrido un error, intente ingresar otro valor.", title="BANCO BILBAO VIZCAYA")
                

        else:
            messagebox.showerror(message="Error, Intente denuevo", title="BANCO BILBAO VIZCAYA")
        pass

    main()

    pass

tarjetas()
##asd