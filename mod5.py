import tkinter as tk
from tkinter import messagebox

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
    categories_selectionnees = [categorie_code for categorie_code, var_value in var.items() if var_value.get() == 1]
    if categories_selectionnees:
        produits_categories_selectionnees = [produit["nom"] for produit in lesProduits if produit["categorie"] in categories_selectionnees]
        if produits_categories_selectionnees:
            messagebox.showinfo("Produits des catégories", "Produits des catégories sélectionnées:\n" + "\n".join(produits_categories_selectionnees))
        else:
            messagebox.showwarning("Aucun produit", "Aucun produit trouvé pour les catégories sélectionnées.")
    else:
        messagebox.showwarning("Aucune catégorie sélectionnée", "Veuillez sélectionner au moins une catégorie avant de visualiser les produits.")

root = tk.Tk()
root.title("Sanaya - 5")

var = {categorie_code: tk.IntVar() for categorie_code in lesCategories.keys()}

for categorie_code, categorie_nom in lesCategories.items():
    tk.Checkbutton(root, text=categorie_nom, variable=var[categorie_code], onvalue=1, offvalue=0).pack(anchor=tk.W)

send_button = tk.Button(root, text="Afficher Produits", command=afficher_produits)
send_button.pack()

root.mainloop()
