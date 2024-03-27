import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "bio": #Se connecte avec l'id admin et mdp bio
        messagebox.showinfo("Connexion réussie", "Administrateur Connecté!")
    else:
        messagebox.showerror("Erreur de connexion", "Connexion refusée")

root = tk.Tk()
root.title("Formulaire de connexion")

username_label = tk.Label(root, text="Nom d'utilisateur:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Mot de passe:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Se connecter", command=login)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
