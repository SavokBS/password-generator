import tkinter as tk
import string
import random

def generate_passwords():
    length = int(length_field.get())
    count = int(count_field.get())
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        passwords.append(password)
    password_field.delete('1.0', tk.END)
    password_field.insert(tk.END, '\n'.join(passwords))

def clear_passwords():
    password_field.delete('1.0', tk.END)

root = tk.Tk()
root.title("Password generator")
length_label = tk.Label(root, text="length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_field = tk.Entry(root)
length_field.insert(0, "8")
length_field.grid(row=0, column=1, padx=5, pady=5)
count_label = tk.Label(root, text="count:")
count_label.grid(row=1, column=0, padx=5, pady=5)
count_field = tk.Entry(root)
count_field.insert(0, "10")
count_field.grid(row=1, column=1, padx=5, pady=5)
generate_button = tk.Button(root, text="Generate", command=generate_passwords)
generate_button.grid(row=2, column=0, padx=5, pady=5)
clear_button = tk.Button(root, text="Clear", command=clear_passwords)
clear_button.grid(row=2, column=1, padx=5, pady=5)
password_field = tk.Text(root)
password_field.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
