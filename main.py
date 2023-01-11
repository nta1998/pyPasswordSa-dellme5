import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_pas():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def a():
    web = website_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        web: {
            "emile": email,
            "password": password
        }
    }
    if len(password)==0 or len(web)==0:
        messagebox.showinfo(title="you forgat samting",message="please make sure you haven't left any fields empty ")
    else:
        m = messagebox.askokcancel(title=f"for website {web}",message=f"These are the info: \n username: {email} \n password: {password}")
        
        
    if m :
        try:
            with open("password.json",mode="r") as data_pas:
                data = json.load(data_pas)
        except FileNotFoundError:
            with open("password.json",mode="w") as data_pas:    
                json.dump(new_data,data_pas,indent= 2 )
                
        else:
            data.update(new_data)
            with open("password.json","w") as data_pas:    
                json.dump(data,data_pas,indent= 2 )
    
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            
    
# ---------------------------- SEARCH ------------------------------- #    
def find():
    with open("password.json","r") as f :
        w = website_input.get()
        print(f[f"{w}"])
    
# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("password by Liloz@")
win.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column= 2,row= 1)

website = Label(text="Website:")
website.grid(column=1,row=2)

website_input = Entry(width=34)
website_input.grid(column=2,row=2)
website_input.focus()

search = Button(text="search",width=14,command=find)
search.grid(column=3,row=2)

user_name = Label(text="Email/Username:")
user_name.grid(column=1,row=3)

user_input = Entry(width=53)
user_input.grid(column=2,row=3,columnspan=2)
user_input.insert(0,"nta199@gmail.com")

password =Label(text="Password:")
password.grid(column=1,row= 4)

password_input = Entry(width=34)
password_input.grid(column=2,row=4)

g_password = Button(text="Generate password",command=new_pas)
g_password.grid(column=3,row=4)

add = Button(text="Add",width=45,command=a)
add.grid(column=2,row=5,columnspan=2)





win.mainloop()