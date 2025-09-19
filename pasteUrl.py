import tkinter as tk
from tkinter import messagebox

def paste_url(root, url_entry):
    try:
        # Lire le texte du presse-papiers
        url = root.clipboard_get()
        url_entry.delete(0, tk.END)  # Effacer le champ d'entrée
        url_entry.insert(0, url)      # Coller l'URL dans le champ d'entrée
    except tk.TclError:
        messagebox.showerror("Erreur", "Le presse-papiers est vide ou ne contient pas de texte.")