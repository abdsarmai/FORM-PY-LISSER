import tkinter as tk
from tkinter import messagebox

produits_disponibles = ['Ahibero' ,'Ajowan' ,'Amande' ,'Amiris' ,'Aneth']

def submit_form():
    produit = produit_entry.get()

    if not produit.strip():
        messagebox.showerror("Erreur", "Veuillez saisir un produit.")
        return

    if produit in produits_disponibles:
        messagebox.showinfo("Sanaya - 1", f"Le produit {produit} est disponible.")
    else:
        messagebox.showerror("Sanaya - Err", f"Le produit {produit} n'est pas disponible.")

root = tk.Tk()
root.title("Sanaya - 1")

produit_label = tk.Label(root, text="Saisir le nom du produit:")
produit_label.grid(row=2, column=0, padx=10, pady=5)
produit_entry = tk.Entry(root, width=25)
produit_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Soumettre", command=submit_form)
submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
