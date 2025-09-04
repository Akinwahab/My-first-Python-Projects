from tkinter import *
from tkinter import messagebox
import pyperclip
import secrets
import string
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = string.ascii_letters        
    numbers = string.digits               
    symbols = "!#$%&()*+"

    nr_letters = secrets.randbelow(3) + 6 
    nr_symbols = secrets.randbelow(3) + 2   
    nr_numbers = secrets.randbelow(3) + 2 

    password_chars = (
        [secrets.choice(letters) for _ in range(nr_letters)] +
        [secrets.choice(symbols) for _ in range(nr_symbols)] +
        [secrets.choice(numbers) for _ in range(nr_numbers)]
    )
    secrets.SystemRandom().shuffle(password_chars)
    password = "".join(password_chars)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
#        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
#        if is_ok:
        try:
            with open('data.json', 'r') as data_file:
                #read old data
                data=json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                #create new file and add data
                json.dump(new_data, data_file, indent=4)
        else:
            #update old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                #save updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email=data[website]['email']
            password=data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
            
# ---------------------------- UI SETUP ------------------------------- #

#window 
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e") 
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#buttons
search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2, sticky="ew")
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2 , sticky="ew")
add_button = Button(text="Add", width=33 , command=save)
add_button.grid(row=4, column=1, columnspan=2 , sticky="ew")


window.mainloop()