import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

lesProduits = [
    {"nom": "Ahibero", "categorie": "hl-ess"},
    {"nom": "Ail", "categorie": "hl-ess"},
    {"nom": "Ajowan", "categorie": "hl-ess"},
    {"nom": "Amande", "categorie": "hl-ess"},
    {"nom": "Amyrio", "categorie": "hl-ess"},
    {"nom": "Calendula", "categorie": "mcrt-hlx"},
    {"nom": "Millepertuis", "categorie": "mcrt-hlx"},
    {"nom": "Macadamia", "categorie": "mcrt-hlx"},
    {"nom": "Arnica", "categorie": "mcrt-hlx"},
    {"nom": "Ginkgo Biloba", "categorie": "ext-plnt"},
    {"nom": "Guarana", "categorie": "ext-plnt"},
    {"nom": "Moringa", "categorie": "ext-plnt"},
    {"nom": "Prêle", "categorie": "ext-plnt"},
    {"nom": "Blanche", "categorie": "argl"},
    {"nom": "Illite verte", "categorie": "argl"},
    {"nom": "Montmorillonite", "categorie": "argl"}
]

lesCategories = {
    "hl-ess": "Huiles Essentielles",
    "mcrt-hlx": "Macérâts Huileux",
    "ext-plnt": "Extraits de Plantes",
    "argl": "Argiles"
}

def afficher_produits():
    categorie_selectionnee = categorie_combobox.get()
    if categorie_selectionnee:
        produits_categorie_selectionnee = [produit["nom"] for produit in lesProduits if produit["categorie"] == list(lesCategories.keys())[list(lesCategories.values()).index(categorie_selectionnee)]]
        if produits_categorie_selectionnee:
            messagebox.showinfo("Produits de la catégorie", "Produits de la catégorie sélectionnée:\n" + "\n".join(produits_categorie_selectionnee))
        else:
            messagebox.showwarning("Aucun produit", "Aucun produit trouvé pour la catégorie sélectionnée.")
    else:
        messagebox.showwarning("Aucune catégorie sélectionnée", "Veuillez sélectionner une catégorie avant de visualiser les produits.")

root = tk.Tk()
root.title("Sanaya - 4")

categorie_combobox = Combobox(root, values=list(lesCategories.values()))
categorie_combobox.current(0) 
categorie_combobox.pack()

send_button = tk.Button(root, text="Afficher Produits", command=afficher_produits)
send_button.pack()

root.mainloop()
