from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    with open("data.json", "r") as file:
        website = ent_website.get().capitalize()
        data = json.load(file)
        try:
          email = data[website]["email"]
          password = data[website]["password"]
        except KeyError:
          messagebox.askretrycancel(message="No such website in the database!\nPlease enter the correct website to search")  
        else:
          messagebox.showinfo(title= website,message=f"Your email is: \n{email} \nYour password is: \n{password}")
        
        


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    chars = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [random.choice(chars) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    ent_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = ent_website.get()
    username = ent_username.get()
    password = ent_password.get()

    new_data = {website: {"email": username, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.askretrycancel(message="Hey, you left some fields empty...")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            ent_website.delete(0, END)
            ent_password.delete(0, END)
            ent_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website URL: ", font=("Times New Roman", 15))
label_website.grid(row=1, column=0)
ent_website = Entry(width=21)
ent_website.grid(row=1, column=1)
ent_website.focus()

label_username = Label(text="Email/Username: ", font=("Times New Roman", 15))
label_username.grid(row=2, column=0)
ent_username = Entry(width=35)
ent_username.grid(row=2, column=1, columnspan=2)
ent_username.insert(0, "istserbina@gmail.com")

label_password = Label(text="Password: ", font=("Times New Roman", 15))
label_password.grid(row=3, column=0)
ent_password = Entry(width=21)
ent_password.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search,width=13)
search_button.grid(row=1, column=2)


window.mainloop()
