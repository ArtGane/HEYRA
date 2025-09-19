import os
import xml.etree.ElementTree as ET
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from generatorMdp import generate_password
from pasteUrl import paste_url
from saveData import save_to_xml, delete_from_xml, search_url_in_xml, update_data
from accesData import view_data

data_window = None

# Fonction pour générer le mot de passe et sauvegarder les informations
def generate_and_save():
    url = url_entry.get()
    username = username_entry.get()
    password_length = int(password_length_entry.get())
    password = generate_password(password_length)  # Générer le mot de passe
    
    # Vérifier si tous les champs sont remplis
    if not url or not username:
        messagebox.showwarning("Champ manquant", "Tous les champs doivent être remplis.")
        return

    # Sauvegarder dans le fichier XML
    save_to_xml(url, username, password)
    
    # Effacer les champs d'entrée
    url_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)

# Fonction pour afficher le contenu du fichier XML
def display_data():
    global data_window  # Utiliser la variable globale

    if data_window is not None and data_window.winfo_exists():
        # Si la fenêtre est déjà ouverte, la fermer
        data_window.destroy()
        data_window = None
        return

    data = view_data()
    
    data_window = tk.Toplevel(root)
    data_window.title("Données sauvegardées")
    data_window.configure(bg="#fffbee")

    # Obtenir la position de la fenêtre principale
    root_x = root.winfo_x()
    root_y = root.winfo_y() + root.winfo_height()

    # Définir la largeur de la nouvelle fenêtre à celle de la fenêtre principale
    window_width = root.winfo_width()
    data_window.geometry(f"{window_width}x350+{root_x}+{root_y}")

    # Afficher les données dans un widget Text
    text_widget = tk.Text(data_window, wrap=tk.WORD, height=10, bg="#ffffff", font=font_style)
    text_widget.insert(tk.END, data)
    text_widget.pack(padx=10, pady=10)
    text_widget.config(state=tk.DISABLED)  # Rendre le texte non éditable

    # Champ d'entrée pour l'URL à supprimer
    url_to_delete_entry = tk.Entry(data_window, font=font_style, bg="#ffffff")
    url_to_delete_entry.pack(padx=10, pady=5)

    # Bouton pour supprimer l'URL
    delete_button = tk.Button(data_window, text="Supprimer l'URL", 
                            command=lambda: (
                                delete_from_xml(url_to_delete_entry.get()), 
                                url_to_delete_entry.delete(0, tk.END)  # Effacer le champ d'entrée ici
                            ), 
                            bg="#E3CD8B", fg="black", font=font_style)
    delete_button.pack(padx=10, pady=5)

    # Champ d'entrée pour l'URL à rechercher
    url_to_search_entry = tk.Entry(data_window, font=font_style, bg="#ffffff")
    url_to_search_entry.pack(padx=10, pady=5)

    # Bouton pour rechercher l'URL
    search_button = tk.Button(data_window, text="Rechercher l'URL", 
                    command=lambda: search_url_in_xml(url_to_search_entry.get(), text_widget, url_to_search_entry), 
                    bg="#E3CD8B", fg="black", font=font_style)
    search_button.pack(padx=10, pady=5)

    # Bouton pour mettre à jour les données
    update_button = tk.Button(data_window, text="Mettre à jour", command=lambda: update_data(text_widget), bg="#E3CD8B", fg="black", font=font_style)
    update_button.pack(padx=10, pady=5)
    

# Interface graphique
root = tk.Tk()
root.title("HEYRA")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))
root.attributes('-topmost', True)

root.configure(bg="#fffbee")

font_style = tkFont.Font(family="Helvetica", size=12)

# Créer les éléments de l'interface utilisateur
copy_button = tk.Button(root, text="Coller l'URL", command=lambda: paste_url(root, url_entry), width=30)
copy_button.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

url_entry = tk.Entry(root, font=font_style)
url_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nom d'utilisateur :", bg="#fffbee", font=font_style).grid(row=1, sticky=tk.W, padx=10, pady=5)
username_entry = tk.Entry(root, font=font_style)
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Longueur du mot de passe :", bg="#fffbee", font=font_style).grid(row=2, sticky=tk.W, padx=10, pady=5)

# Création du pad numérique
pad_frame = tk.Frame(root)
pad_frame.grid(row=2, column=1, pady=5)

for i in range(1, 10):
    btn = tk.Button(pad_frame, text=str(i), width=5, command=lambda i=i: password_length_entry.insert(tk.END, str(i)))
    btn.grid(row=(i-1)//3, column=(i-1)%3)

password_length_entry = tk.Entry(root, font=font_style, width=10, justify='center')
password_length_entry.grid(row=3, column=1, padx=10, pady=5)

validate_button = tk.Button(root, text="Valider", command=generate_and_save, bg="#E3CD8B", fg="black", font=font_style,
                             borderwidth=2)
validate_button.grid(row=4, columnspan=2, padx=10, pady=10)

display_button = tk.Button(root, text="Afficher données", command=display_data, bg="#E3CD8B", fg="black", font=font_style,
                           borderwidth=2)
display_button.grid(row=5, columnspan=2, padx=10, pady=10)
tk.Button(pad_frame, text="0", width=5, command=lambda: password_length_entry.insert(tk.END, '0')).grid(row=3, column=1)

password_length_entry = tk.Entry(root, font=font_style, width=10, justify='center')
password_length_entry.grid(row=3, column=1, padx=10, pady=5)

root.update_idletasks()
root.geometry(f"{root.winfo_width() + 40}x{root.winfo_height() + 40}")

root.mainloop()