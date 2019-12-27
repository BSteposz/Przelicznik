from tkinter import *
from decimal import Decimal
from tkinter import messagebox


class Aplikacja(Frame):
    def __init__(self, master):
        super(Aplikacja, self).__init__(master)
        self.grid()
        self.przyciski()

    def przyciski(self):
        Label(self,
              text="Przelicznik jednostek create by Bartosz Stęposz"
              ).grid(row=0, column=0,columnspan = 2, sticky=W)
        Label(self,
              text="Wybierz jednostkę początkową:").grid(row=1, column=0, sticky=W)
        Label(self,
              text="Wybierz jednostkę do zamiany:").grid(row=1, column=2, sticky=W)
        self.jednostki1 = StringVar()
        self.jednostki1.set(None)
        self.jednostki2 = StringVar()
        self.jednostki2.set(None)
        self.jednostka = ["mm", "cm", "dm", "m", "km"]
        kolumna =2
        for i in self.jednostka:
            Radiobutton(self,
                        text=i,
                        variable=self.jednostki1,
                        value=i,
                        borderwidth=0
                        ).grid(row=kolumna, column=0,  sticky=W)
            Radiobutton(self,
                        text=i,
                        variable=self.jednostki2,
                        value=i,
                        borderwidth=0
                        ).grid(row=kolumna, column=2,  sticky=W)
            kolumna += 1
        Label(self,
              text="Wartość do zmiany:").grid(row=kolumna, column=0, )
        self.zmieniana = Entry(self, fg="black")
        self.zmieniana.grid(row=kolumna, column=1, sticky=W, )
        kolumna+=1
        Button(self,
               text="Kliknij, aby przeliczyć",
               command=self.akcja
               ).grid(row=kolumna, column=1, sticky=W )
        kolumna+=1
        self.wynik = Text(self, width=15, height=1, wrap = WORD)
        self.wynik.grid(row=kolumna, column=1, sticky=W)
        Label(self,
              text="Wynik:").grid(row=kolumna, column=0, )

    def przeliczaj(self):
        l1=self.jednostki1.get()
        l2=self.jednostki2.get()
        przelicznik = [10 ** -3, 10 ** -2, 10 ** -1, 10 ** 0, 10 ** 3]
        przekabatniki = [10 ** 3, 10 ** 2, 10 ** 1, 10 ** 0, 10 ** -3]
        for i in self.jednostka:
            if i == l1:
                d = przelicznik[self.jednostka.index(i)] * float(self.zmieniana.get())  # zamienia na metry!
                for j in self.jednostka:
                    if j == l2:
                        g = przekabatniki[self.jednostka.index(j)] * d
                       
                    else:
                        continue
            else:
                continue
        if  l1 =="mm" and l2=="km":
            g="{:.6f}".format(g) 
        elif l1=="cm" and l2 == "km":
            g="{:.5f}".format(g)
        else:
            g=g


            
        return g
    
    def akcja(self):
        try:
            wynik=self.przeliczaj()
            self.wynik.delete(0.0, END)
            self.wynik.insert(0.0, str(wynik) + self.jednostki2.get())
        except ValueError:
            Entry(self, fg="red")
            messagebox.showinfo('Błąd', 'Wpisana wartość musi być liczbą')


        except UnboundLocalError:
            messagebox.showinfo('Błąd', 'Proszę wybrać jednostki do przeliczenia')




root = Tk()
root.title("Konwenter BS v0.1.5")
root.geometry("500x250")
app = Aplikacja(root)
root.mainloop()
