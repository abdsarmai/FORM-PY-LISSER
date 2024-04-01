import tkinter as tk
from tkinter import messagebox

def submit_form():
    if not nom_entry.get() or not prenom_entry.get() or not telephone_entry.get() or not email_entry.get():
        messagebox.showwarning("Champs obligatoires", "Veuillez remplir tous les champs obligatoires (nom, prénom, téléphone, email).")
        return

    recap = "Récapitulatif des informations :\n"
    recap += f"Civilité: {civilite_var.get()}\n"
    recap += f"Nom: {nom_entry.get()}\n"
    recap += f"Prénom: {prenom_entry.get()}\n"
    recap += f"Téléphone: {telephone_entry.get()}\n"
    recap += f"Email: {email_entry.get()}\n"
    recap += f"Raison de la prise de contact: {raison_var.get()}\n"
    recap += f"Modes de réponse: {', '.join(modes_reponse)}\n"
    recap += f"Date de rappel: {date_rappel_entry.get()}\n"
    recap += f"Message complémentaire: \n{message_text.get('1.0', tk.END)}"

    messagebox.showinfo("Récapitulatif", recap)

root = tk.Tk()
root.title("Formulaire de Contact")

civilite_var = tk.StringVar()
raison_var = tk.StringVar()
modes_reponse = []

formulaire_frame = tk.Frame(root)
formulaire_frame.pack(padx=10, pady=10)

civilite_label = tk.Label(formulaire_frame, text="Civilité:")
civilite_label.grid(row=0, column=0, sticky="w")
civilite_combobox = tk.OptionMenu(formulaire_frame, civilite_var, "M.", "Mme", "Mlle")
civilite_combobox.grid(row=0, column=1, sticky="w")

nom_label = tk.Label(formulaire_frame, text="Nom:")
nom_label.grid(row=1, column=0, sticky="w")
nom_entry = tk.Entry(formulaire_frame)
nom_entry.grid(row=1, column=1, sticky="w")

prenom_label = tk.Label(formulaire_frame, text="Prénom:")
prenom_label.grid(row=2, column=0, sticky="w")
prenom_entry = tk.Entry(formulaire_frame)
prenom_entry.grid(row=2, column=1, sticky="w")

telephone_label = tk.Label(formulaire_frame, text="Téléphone:")
telephone_label.grid(row=3, column=0, sticky="w")
telephone_entry = tk.Entry(formulaire_frame)
telephone_entry.grid(row=3, column=1, sticky="w")

email_label = tk.Label(formulaire_frame, text="Email:")
email_label.grid(row=4, column=0, sticky="w")
email_entry = tk.Entry(formulaire_frame)
email_entry.grid(row=4, column=1, sticky="w")

modes_reponse_label = tk.Label(formulaire_frame, text="Modes de réponse:")
modes_reponse_label.grid(row=6, column=0, sticky="w")
email_checkbox = tk.Checkbutton(formulaire_frame, text="Email", command=lambda: modes_reponse.append("Email"))
email_checkbox.grid(row=6, column=1, sticky="w")
sms_checkbox = tk.Checkbutton(formulaire_frame, text="SMS", command=lambda: modes_reponse.append("SMS"))
sms_checkbox.grid(row=7, column=1, sticky="w")
telephone_checkbox = tk.Checkbutton(formulaire_frame, text="Téléphone", command=lambda: modes_reponse.append("Téléphone"))
telephone_checkbox.grid(row=8, column=1, sticky="w")


date_rappel_label = tk.Label(formulaire_frame, text="Objet:")
date_rappel_label.grid(row=9, column=0, sticky="w")
date_rappel_entry = tk.Entry(formulaire_frame)
date_rappel_entry.grid(row=9, column=1, sticky="w")

message_label = tk.Label(formulaire_frame, text="Message complémentaire:")
message_label.grid(row=10, column=0, sticky="w")
message_text = tk.Text(formulaire_frame, height=5, width=30)
message_text.grid(row=10, column=1, sticky="w")


submit_button = tk.Button(root, text="Soumettre", command=submit_form)
submit_button.pack(pady=10)

root.mainloop()
