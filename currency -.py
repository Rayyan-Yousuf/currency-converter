from tkinter import *
from tkinter import messagebox
import requests
from tkinter import ttk

url = "https://api.exchangerate-api.com/v4/latest/USD"
currency_names = requests.get(url).json()
currency_names = currency_names['rates']
names = currency_names.keys()
names = list(names)

window = Tk()


def window_config():
    # window-configuration
    window.geometry("600x400")
    window.resizable(width=0, height=0)
    window.title('Currency Converter')
    window.config(background="#42aaf5")
    icon = PhotoImage(file='E:\Programming\Currency-Converter\money.png')
    window.iconphoto(True,icon)


# currency-calculating-logic
def calccurrency(currencyname, amount, to_currency):
    currency = requests.get(url).json()
    exchange_rate = currency['rates'][currencyname]

    amount = float(amount / exchange_rate)
    amount = round(amount * currency['rates'][to_currency], 4)
    result.config(text=str(amount))


def gui():
    # Intro-Label
    Title = Label(window, text="Welcome To Currency Converter", font=(
        "corbel", 25, "bold"), bg="#3165e8", relief=FLAT, border=3)
    Title.place(x=50, y=70)

    # From-currency-box
    combo = ttk.Combobox(window, values=names,
                        state="readonly", font=("Corbel", 11))
    combo.current(112)  # Default Value
    combo.place(x=50, y=300)

    # To-Currency-Box
    combo2 = ttk.Combobox(window, values=names,
                        state="readonly", font=("Corbel", 12))
    combo2.current(0)  # Default Value
    combo2.place(x=350, y=300)

    # entry-box
    entry = float
    entry = Entry(window, font=("Corbel", 11, "bold"), borderwidth=3, relief=FLAT)
    entry.insert(0, "Enter Amount")
    entry.place(x=51, y=325)

    # convert-button
    def convert():
        try:
            from_currency = combo.get()
            to_currency = combo2.get()
            amount = float(entry.get())
            # calling the main function here
            calccurrency(from_currency, amount, to_currency)
            
        except ValueError:
            messagebox.showwarning(title="Value Error",
                                    message="Please enter a valid value")


    convert = Button(window, text="Convert!", font=(
        "corbel", 16, "bold"), command=convert, bg="#545c58", activebackground="#7d827f")
    convert.place(x=250, y=220)

    # result box
    global result
    result = Label(window, font=("Corbel", 11, "bold"), borderwidth=3,
                text='                                                     ', bg="white", relief=FLAT)
    result.place(x=351, y=326)


window_config()
gui()
window.mainloop()


