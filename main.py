from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is {password}")

    input_password.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving_data():

    website = input_website.get()
    user = input_user.get()
    password = input_password.get()
    new_data = {
    website:{
        "email" : user,
        "password": password
    }
    }    
    
    

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Do not any fields empty")
    else:
       # is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \nEmail: {user}"
       # f"\nPassword: {password} \n Is it ok to save ?")

        #if is_ok:

        try:
            with open("data.json",'r') as f:

                data = json.load(f)
        except FileNotFoundError:
            
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            
            with open("data.json:=", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            input_user.delete(0, END)
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #

def search_data():
    website_search = input_website.get()

    if len(website_search) == 0:
        messagebox.showinfo(title="Ooops", message="Do not left Website field empty")
    else:
        try:
            with open("data.json",'r') as fi:
                data = json.load(fi)
        except FileNotFoundError:
            messagebox.showinfo(title="Data Error", message="Following data does not exist")
        else:
            if website_search in data:
                email = data[website_search]["email"]
                password = data[website_search]["password"]
                messagebox.showinfo(title=website_search, message=f"Email = {email}\nPassword : {password} ")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Error", message=f"No detalis for {website_search} exists")
            
# webstie_search
# website_search


# ---------------------------- UI SETUP ------------------------------- # 


# Label


window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width= 200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text='Website')
label_website.grid(row=1, column=0)
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

label_user = Label(text='Email/Username:')
label_user.grid(row=2, column=0)
input_user = Entry(width=35)
input_user.insert(0, "Pawelek1998@wp.pl")
input_user.grid(row=2, column=1, columnspan=2)

label_password = Label(text='Password:')
label_password.grid(row=3, column=0)
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

#Buttons 

def generate_password_clicked():
    generate_password()

def add_button_clicked():
    saving_data()

def search_clicked():
    search_data()


button_generate = Button(text="Generate Pass", command=generate_password_clicked)
button_generate.grid(row=3,column=2)

button_add = Button(text="Add", command=add_button_clicked, width=36)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", command=search_clicked)
button_search.grid(row=1, column=3)




window.mainloop()