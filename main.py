import tkinter as tki
from tkinter import messagebox
import random
import pyperclip
import json

# Constants/User Changeable Stuff #
FONT_NAME = "Times New Roman"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Generates "Strong" Password #
# xkcd.com/936/ #
# https://github.com/shoe-bham-cries/PyPassWord - reformatted code #
def generate_action():
    password_entry.delete(0, 'end')
    pass_letters = [random.choice(letters) for _ in range(random.randint(6, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pas = pass_letters + pass_numbers + pass_symbols
    random.shuffle(pas)
    final = ''.join(pas)

    password_entry.insert(0, string=final)
    pyperclip.copy(final)


# File Handling Part #


def save():
    website_entry_data = website_entry.get()
    username_entry_data = username_entry.get()
    password_entry_data = password_entry.get()

    new_data = {
        website_entry_data: {
            "username": username_entry_data,
            "password": password_entry_data,
        }
    }
    if len(website_entry_data) == 0 or len(password_entry_data) == 0:
        messagebox.showinfo("Error", "You've left empty fields")
    else:
        is_ok = messagebox.askokcancel("Confirm Details", f"Details entered are:\nWebsite: {website_entry_data}\nEmail:"
                                                          f" {username_entry_data} \nPassword: {password_entry_data}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Write all data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update it
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Rewrite all data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# Search Function#


def search():
    key = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "File not found.")
    else:
        try:
            messagebox.showinfo(key, f"Username: {data[key]['username']}\nPassword: {data[key]['password']}")
        except KeyError:
            messagebox.showinfo("Error", f"No details for the website {key} exists.")
# UI Setup #
window = tki.Tk()

window.title("MyPassManager")
window.config(padx=50, pady=50)
my_img = tki.PhotoImage(file='logo.png')
canvas = tki.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

website_label = tki.Label(text="Website: ", font=(FONT_NAME, 10, "normal"))
website_label.grid(column=0, row=1, pady=2)

username_label = tki.Label(text="Email/Username: ", font=(FONT_NAME, 10, "normal"))
username_label.grid(column=0, row=2, pady=2)

password_label = tki.Label(text="Password: ", font=(FONT_NAME, 10, "normal"))
password_label.grid(column=0, row=3, pady=2)

website_entry = tki.Entry(width=34)
website_entry.grid(row=1, column=1, pady=2)
website_entry.focus()

username_entry = tki.Entry(width=43)
username_entry.grid(column=1, row=2, columnspan=2, pady=2)
username_entry.insert(0, "shubhamrathore3261@gmail.com")

password_entry = tki.Entry(width=34)
password_entry.grid(column=1, row=3, pady=2)

generate_button = tki.Button(text="Generate", command=generate_action, highlightthickness=0)
generate_button.grid(column=2, row=3, pady=2)
search_button = tki.Button(text="Search", command=search, highlightthickness=0, width=6)
search_button.grid(column=2, row=1, pady=2)

add_button = tki.Button(text="Add", command=save, highlightthickness=0, width=36)
add_button.grid(column=1, row=4, columnspan=2, pady=2)
window.mainloop()
#
# with open("data.json", "r") as data_file:
#     # Reading old data
#     data = json.load(data_file)
#     # Update it
#     data.update(new_data)
#
# with open("data.json", "w") as data_file:
#     # Rewrite all data
#     json.dump(data, data_file, indent=4)
