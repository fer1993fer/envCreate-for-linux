
import os
import tkinter as tk
from tkinter import ttk


class App(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.geometry("370x100")
        self.resizable(False, False)

        self.eth2 = ttk.Label(master=self)
        self.eth2.configure(text="Dale un nombre a tu entorno : ")
        self.eth2.place(x=30, y=30)

        self.ent2 = ttk.Entry(master=self)
        self.ent2.configure(width=12)
        self.ent2.place(x=240, y=25)

        self.var = tk.BooleanVar()
        self.rdbt = ttk.Checkbutton(master=self)
        self.rdbt.configure(text="Parametros adicionales", variable=self.var,\
                            command=self.avilitar)
        self.rdbt.place(x=30, y=70)

        self.btn2 = ttk.Button(master=self)
        self.btn2.configure(text="crear", command=self.crear)
        self.btn2.place(x=260, y=60)

    def avilitar(self) :
        estado = self.var.get()
        if estado == True :
            self.geometry("370x320")
            
            self.sep = ttk.Separator(master=self, orient="horizontal")
            self.sep.place(x=40, y=100, width=290)

            self.chbt1 = ttk.Button(master=self)
            self.chbt1.configure(text="--system-site-packages", style="Toolbutton", command=self.syms)
            self.chbt1.place(x=30, y=110)

            self.chbt2 = ttk.Button(master=self)
            self.chbt2.configure(text="--symlinks ", style="Toolbutton", command=self.sym)
            self.chbt2.place(x=30, y=140)

            self.chbt6 = ttk.Button(master=self)
            self.chbt6.configure(text="--copies ", style="Toolbutton", command=self.cop)
            self.chbt6.place(x=30, y=170) 

            self.chbt = ttk.Button(master=self)
            self.chbt.configure(text="--clear", style="Toolbutton", command=self.clear)
            self.chbt.place(x=30, y=200) 

            self.chbt3 = ttk.Button(master=self)
            self.chbt3.configure(text="--upgrade", style="Toolbutton", command=self.up)
            self.chbt3.place(x=220, y=110)

            self.chbt5 = ttk.Button(master=self)
            self.chbt5.configure(text="--without-pip ", style="Toolbutton", command=self.wit)
            self.chbt5.place(x=220, y=140)

            self.chbt4 = ttk.Button(master=self)
            self.chbt4.configure(text="--prompt", style="Toolbutton", command=self.prom)
            self.chbt4.place(x=220, y=170)

            self.chbt7 = ttk.Button(master=self)
            self.chbt7.configure(text="--upgrade-deps", style="Toolbutton", command=self.updeps)
            self.chbt7.place(x=220, y=200)

            self.ent = ttk.Entry(master=self)
            self.ent.configure(width=25)
            self.ent.place(x=75, y=240)

            self.btn3 = ttk.Button(master=self)
            self.btn3.configure(text="--help", command=ayuda)
            self.btn3.place(x=130, y=275)


        else :
            self.geometry("370x100")



    def crear(self) :
        pass

    def syms(self) :
        self.ent.insert(tk.END, "--system-site-packages ")
    def sym(self) :
        self.ent.insert(tk.END, "--symlinks ")
    def cop(self) :
        self.ent.insert(tk.END, "--copies ")
    def clear(self) :
        self.ent.insert(tk.END, "--clear ")
    def up(self) :
        self.ent.insert(tk.END, "--upgrade ")
    def wit(self) :
        self.ent.insert(tk.END, "--without-pip ")
    def prom(self) :
        self.ent.insert(tk.END, "--promp ")
    def updeps(self) :
        self.ent.insert(tk.END, "--upgrade-deps ")
        
def ayuda() :
    os.system("python3 -m venv --h")


if __name__ == "__main__" :
    app = App()
    app.mainloop()