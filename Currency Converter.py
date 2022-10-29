from cProfile import label
from tkinter import *
from tkinter import ttk
import requests

names = [
        "USD",
        "AED",
        "AFN",
        "ALL" ,
        "AMD" ,
        "ANG" ,
        "AOA" ,
        "ARS" ,
        "AUD" ,
        "AWG" ,
        "AZN" ,
        "BAM" ,
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "FOK",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KID",
        "KMF",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STN",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TVD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "UYU",
        "UZS",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XDR",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
]

window = Tk()


def window_config():
        #window-configuration
        window.geometry("600x500")
        window.resizable(width=1366,height=768)
        window.title('Currency Converter v2 by Rayyan')
        window.config(background="#000000")
        icon = PhotoImage(file='F:\VSCode\Playground\Currency Converter\money.png')
        window.iconphoto(True,icon)


#currency-calculating-logic
def calccurrency(currencyname,amount,to_currency):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    currency = requests.get(url).json()    
    exchange_rate = currency['rates'][currencyname]

    amount = float(amount / exchange_rate)
    amount = round(amount * currency['rates'][to_currency],4)
    #result = Label(window,font = ("Arial",11,"bold"),borderwidth=5,text=amount,bg="white",relief=RAISED)
    #result.place(x=350,y=325)
    result.config(text = str(amount))
        

def gui():
        #Intro-Label 
        Title = Label(window ,text="Welcome To My Basement",font=("Consolas",25,"bold"),bg="#FFFFFF",relief=FLAT,border= 1)
        Title.place(x=110,y=70)

        #From-currency-box
        combo = ttk.Combobox(window,values=names,state="readonly",font = ("Consolas",11))
        combo.current(112) #Default Value
        combo.place(x=50,y=300)

        #To-Currency-Box
        combo2 = ttk.Combobox(window,values=names,state="readonly",font = ("Consolas",12))
        combo2.current(0) #Default Value
        combo2.place(x=350,y=300)

        #entry-box
        entry = float
        entry = Entry(window,font = ("Consolas",11),borderwidth=1, text = "",bg="white",relief=FLAT)
        #entry = Entry(window,font = ("Consolas",11),borderwidth=1)
        entry.insert(2, "Enter Amount Here!")
        entry.place(x=50,y=330)

        #convert-button
        def convert():      
            from_currency = combo.get()
            to_currency =  combo2.get()
            amount = float(entry.get())
            calccurrency(from_currency,amount,to_currency)  #calling the main function here

        convert = Button(window,text="Convert!",font = ("Consolas",16),command=convert,bg="#545c58",activebackground="#7d827f")
        convert.place(x=250,y=220)

        #result box
        global  result
        result = Label(window,font = ("Consolas",11,"bold"),borderwidth=1, text = "                       " ,bg="white",relief=FLAT)
        result.place(x=350,y=330)

window_config()
gui()
window.mainloop()

