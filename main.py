from tkinter import *
from tkinter import Tk ,ttk
from PIL import Image, ImageTk
import requests


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1=combo1.get()
    currency_2=combo2.get()
    amount=value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	"x-rapidapi-key": "1f7360e0c2msh7b327ab86d56603p15ce7ejsn65d9c0717758",
	"x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    converted_amount=data["result"]["convertedAmount"]
    formatted_amount=round(converted_amount,2)
    result["text"]=formatted_amount
    print(formatted_amount)







#colors
color0="#fefae0"
color1="#283618"
color2="#dda15e"

window= Tk()
window.geometry("500x500")  
window.title("currency converter")
window.configure(bg=color0)
window.resizable(height=False, width=False)


#frames 

top=Frame(
    window,
    width=500,
    height=100,
    bg=color2,
)
top.grid(row=0,column=0)

main=Frame(window,width=500,height=400,bg=color0)
main.grid(row=1,column=0)

#top frame

icon= Image.open('images/icon.png')
icon = icon.resize((70,70))
icon= ImageTk.PhotoImage(icon)
app_name=Label( top , image=icon , compound=LEFT ,text="Currency Converter",font=("Arial",20),height=5,padx=25,pady=47 ,anchor=CENTER , bg=color2,fg=color0)
app_name.place(x=0,y=0)

#main frame

result=Label( main ,text="",font=("Arial",20),width=20,height=3,pady=10 ,relief="solid",anchor=CENTER , bg=color0,fg=color1)
result.place(x=80,y=20)

currency=["USD","EUR","TND","GBP","AUD","CAD","SGD","CHF","MYR","JPY","CNY"]

from_label=Label( main ,text="From",font=("Arial",17),width=10,height=2,pady=10 ,anchor=NW , bg=color0,fg=color1)
from_label.place(x=80,y=140)
combo1=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy",15) )
combo1['values']= (currency)
combo1.place(x=80,y=180)


to_label=Label( main ,text="To",font=("Arial",17),width=10,height=2,pady=10 ,anchor=NW , bg=color0,fg=color1)
to_label.place(x=300,y=140)
combo2=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy",15) )
combo2['values']= (currency)
combo2.place(x=300,y=180)

value = Entry(main,font=("Arial",15),width=30,relief="solid",justify=CENTER)
value.place(x=80,y=250)

btn=Button(main,text="Convert",font=("Arial",15),width=30,height=1,bg=color1,fg=color0 , command=convert)
btn.place(x=80,y=300)



window.mainloop()