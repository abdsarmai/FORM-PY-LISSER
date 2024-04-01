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
    categorie = var.get()
    if categorie: 
        produits_categorie = [produit["nom"] for produit in lesProduits if produit["categorie"] == categorie]
        if produits_categorie:
            messagebox.showinfo("Produits de la catégorie", "Produits de la catégorie " + lesCategories[categorie] + ":\n" + "\n".join(produits_categorie))
        else:
            messagebox.showwarning("Aucun produit", "Aucun produit trouvé pour la catégorie sélectionnée.")
    else:
        messagebox.showwarning("Aucune catégorie sélectionnée", "Veuillez sélectionner une catégorie avant de visualiser les produits.")

root = tk.Tk()
root.title("Sanaya - 4")
var = tk.StringVar()

radio1 = tk.Radiobutton(root, text="Huiles Essentielles", variable=var, value="hl-ess")
radio1.pack(anchor=tk.W)

radio2 = tk.Radiobutton(root, text="Macérâts Huileux", variable=var, value="mcrt-hlx")
radio2.pack(anchor=tk.W)

radio3 = tk.Radiobutton(root, text="Extraits de Plantes", variable=var, value="ext-plnt")
radio3.pack(anchor=tk.W)

radio4 = tk.Radiobutton(root, text="Argiles", variable=var, value="argl")
radio4.pack(anchor=tk.W)

send_button = tk.Button(root, text="Rechercher", command=afficher_produits)
send_button.pack()

root.mainloop()
