import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty")
    else:
        try:
            with open("passwordFile.json", "r") as file:
                # Reading of old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwordFile.json", "w") as file:
                json.dump(new_data, file, indent=4)
            # Updating old data with new data
        else:
            data.update(new_data)

            with open("passwordFile.json", "w") as file:
                # Writing the new data to the file
                json.dump(data, file, indent=4)
        finally:
            websiteEntry.delete(0, tkinter.END)
            passwordEntry.delete(0, tkinter.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = websiteEntry.get()
    email = emailEntry.get()
    try:
        with open("passwordFile.json", "r") as file:
            data = json.load(file)
            password = data[website]["password"]
    except KeyError:
        messagebox.showwarning(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File found")
    else:
        messagebox.showwarning(title=f"{website}", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #


# WINDOW
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CANVAS
canvas = tkinter.Canvas(height=200, width=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(57, 100, image=img)
canvas.grid(row=0, column=1)

# WEBSITE LABEL
websiteLabel = tkinter.Label(text="Website:")
websiteLabel.grid(row=1, column=0)

# WEBSITE ENTRY
websiteEntry = tkinter.Entry(width=35)
websiteEntry.grid(row=1, column=1)
websiteEntry.focus()

# EMAIL LABEL
emailLabel = tkinter.Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)

# EMAIL ENTRY
emailEntry = tkinter.Entry(width=35)
emailEntry.grid(row=2, column=1)
emailEntry.insert(0, "mahipal2002rana@gmail.com")

# PASSWORD LABEL
passwordLabel = tkinter.Label(text="Password:")
passwordLabel.grid(row=3, column=0)

# PASSWORD ENTRY
passwordEntry = tkinter.Entry(width=35)
passwordEntry.grid(row=3, column=1)

# GENERATE PASSWORD BUTTON
button1 = tkinter.Button(text="Generate Password", width=29, command=generate_password)
button1.grid(row=4, column=1)

# SEARCH BUTTON
button3 = tkinter.Button(text="Search", width=29, command=find_password)
button3.grid(row=5, column=1)

# ADD PASSWORD BUTTON
button2 = tkinter.Button(text="Add", width=29, command=save)
button2.grid(row=6, column=1)

window.mainloop()
