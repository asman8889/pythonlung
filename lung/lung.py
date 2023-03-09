import tkinter as tk

def deposit(amount):
    with open("deposit.txt", "a") as f:
        f.write(str(amount) + "\n")
    status_label.config(text="Deposit successful")

def view_deposits():
    with open("deposit.txt", "r") as f:
        deposits = f.readlines()
    if deposits:
        deposit_list.delete(0, tk.END)
        for deposit in deposits:
            deposit_list.insert(tk.END, deposit.strip())
    else:
        status_label.config(text="No deposits found")

def handle_choice():
    choice = choice_var.get()
    if choice == "1":
        amount = float(amount_entry.get())
        deposit(amount)
    elif choice == "2":
        view_deposits()
    elif choice == "3":
        root.destroy()
    else:
        status_label.config(text="Invalid choice")

root = tk.Tk()
root.title("Deposit Tracker")

# Choice section
choice_label = tk.Label(root, text="Choose an option:")
choice_label.pack()

choice_var = tk.StringVar()
choice_var.set("1")

deposit_radio = tk.Radiobutton(root, text="Deposit", variable=choice_var, value="1")
deposit_radio.pack()

view_radio = tk.Radiobutton(root, text="View deposits", variable=choice_var, value="2")
view_radio.pack()

exit_radio = tk.Radiobutton(root, text="Exit", variable=choice_var, value="3")
exit_radio.pack()

# Amount section
amount_label = tk.Label(root, text="Enter deposit amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

# Button section
submit_button = tk.Button(root, text="Submit", command=handle_choice)
submit_button.pack()

# Deposit list section
deposit_list = tk.Listbox(root)
deposit_list.pack()

# Status section
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
