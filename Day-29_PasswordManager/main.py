from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 14))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Generated", message="The generated password has been copied to Clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_name = website_entry.get()
    email_address = email_entry.get()
    password_to_save = password_entry.get()

    if len(website_name) == 0 or len(password_to_save) == 0 or len(email_address) == 0:
        messagebox.showinfo(title="Required Fields missing", message="Please fill all the required fields.")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"The details entered are:\nEmail: "
                                                                   f"{email_address}\nPassword: {password_to_save}\n"
                                                                   f"Save this info?")

        if is_ok:
            with open("password_info.txt", mode="a") as file:
                file.write(f"{website_name} | {email_address} | {password_to_save} \n")
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
# email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
