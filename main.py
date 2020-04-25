from tkinter import *
from PIL import ImageTk, Image
import urllib.request
from bs4 import BeautifulSoup
from threading import Timer

class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Background Color
        self.configure(background='black')

        # Currency
        dollar = Label(self, text="Dolar", font=("Helvetica", 20))
        dollar.grid(row=1, column=1)
        dollar.configure(bg='black', fg='white')
        uyu = Label(self, text="Peso Uruguayo", font=("Helvetica", 20))
        uyu.grid(row=1, column=2)
        uyu.configure(bg='black', fg='white')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Flags
        usa_flag = ImageTk.PhotoImage(Image.open("usa.png"))
        uy_flag = ImageTk.PhotoImage(Image.open("uyu.png"))

        usa_flag_label = Label(self, image=usa_flag)
        usa_flag_label.image=usa_flag
        usa_flag_label.grid(row=2, column=1)
        uy_flag_label = Label(self, image=uy_flag)
        uy_flag_label.image=uy_flag
        uy_flag_label.grid(row=2, column=2)

        # Prices
        dollar_label = Label(self, justify="center", text="1", font=("Helvetica", 18))
        dollar_label.grid(row=3, column=1)
        dollar_label.configure(bg='black', fg='white')

        dollar_price = self.get_dollar_price()

        uy_label = Label(self, justify="center", text=dollar_price, font=("Helvetica", 18))
        uy_label.grid(row=3, column=2)
        uy_label.configure(bg='black', fg='white')

    def get_dollar_price (self):
        # Data Scraping
        data = urllib.request.urlopen('https://themoneyconverter.com/ES/USD/UYU').read().decode()
        soup = BeautifulSoup(data, features="html5lib")
        # Finding the tag that contains conversion
        return str(soup.find(id='res1'))[35:40]
        Timer(7200, get_dollar_price())

if __name__ == "__main__":
    root = Tk()
    root.title("Dollar Price")
    root.geometry("500x250")
    root.resizable(False, False)
    Main(root).grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()
