import os
import xml.etree.ElementTree as ET
import tkinter as tk
from flask import Flask, request
from tkinter import messagebox
from flask_cors import CORS
from generatorMdp import generate_password

# Fonction pour sauvegarder les données dans un fichier XML
def save_to_xml(url, username, password):
    chemin_fichier = "data.xml"
    
    # Créer ou charger le fichier XML
    if not os.path.exists(chemin_fichier) or os.path.getsize(chemin_fichier) == 0:
        root = ET.Element("credentials")
        tree = ET.ElementTree(root)
        tree.write(chemin_fichier)

    # Ajouter les nouvelles informations
    tree = ET.parse(chemin_fichier)
    root = tree.getroot()

    new_entry = ET.SubElement(root, "entry")
    url_element = ET.SubElement(new_entry, "url")
    url_element.text = url
    username_element = ET.SubElement(new_entry, "username")
    username_element.text = username
    password_element = ET.SubElement(new_entry, "password")
    password_element.text = password

    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            for child in elem:
                indent(child, level+1)
            if not child.tail or not child.tail.strip():
                child.tail = i
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

    indent(root)
    password_element.text = password

    tree.write(chemin_fichier)

    messagebox.showinfo("Succès", f"Données sauvegardées.")
    
def delete_from_xml(url):
    chemin_fichier = "data.xml"

    # Vérifier si le fichier existe
    if not os.path.exists(chemin_fichier):
        messagebox.showerror("Erreur", "Le fichier data.xml n'existe pas.")
        return

    # Charger le fichier XML
    tree = ET.parse(chemin_fichier)
    root = tree.getroot()

    # Trouver et supprimer l'entrée correspondante
    entries_to_remove = []
    for entry in root.findall('entry'):
        url_element = entry.find('url')
        if url_element is not None and url_element.text is not None and url in url_element.text:
            entries_to_remove.append(entry)

    # Suppression des entrées trouvées
    for entry in entries_to_remove:
        root.remove(entry)

    # Écrire les modifications dans le fichier XML
    tree.write(chemin_fichier)

    if entries_to_remove:
        messagebox.showinfo("Succès", f"{len(entries_to_remove)} entrée(s) supprimée(s).")
    else:
        messagebox.showinfo("Information", "Aucune URL trouvée, vérifiez qu'elle soit complète.")

        
def search_url_in_xml(url_to_search, text_widget, url_to_search_entry):
    chemin_fichier = "data.xml"

    # Vérifier si le fichier existe
    if not os.path.exists(chemin_fichier):
        messagebox.showerror("Erreur", "Le fichier data.xml n'existe pas.")
        return

    # Charger le fichier XML
    tree = ET.parse(chemin_fichier)
    root = tree.getroot()

    # Rechercher l'URL dans les entrées
    found = False
    for entry in root.findall('entry'):
        url_element = entry.find('url')
        if url_element is not None and url_to_search in url_element.text:
            found = True

            # Mettre en évidence l'URL trouvée
            text_widget.config(state=tk.NORMAL)
            start_index = text_widget.search(url_element.text, "1.0", stopindex=tk.END)
            if start_index:
                end_index = f"{start_index}+{len(url_element.text)}c"
                text_widget.tag_add("highlight", start_index, end_index)
                text_widget.tag_config("highlight", background="yellow")
            text_widget.config(state=tk.DISABLED)
            break

    if not found:
        messagebox.showinfo("Non trouvé", f"Aucune entrée trouvée pour l'URL '{url_to_search}'.")

    # Effacer le champ d'entrée
    url_to_search_entry.delete(0, tk.END)
    
def update_data(new_username, new_password):
    chemin_fichier = "data.xml"

    if not os.path.exists(chemin_fichier):
        print("Le fichier data.xml n'existe pas.")
        return

    tree = ET.parse(chemin_fichier)
    root = tree.getroot()

    # Parcourir les entrées pour mettre à jour l'identifiant
    for entry in root.findall('entry'):
        username_element = entry.find('username')
        password_element = entry.find('password')
        url_element = entry.find('url')
        
        if username_element is not None and username_element.text != new_username:
            # Si l'identifiant a changé, mettre à jour l'identifiant
            username_element.text = new_username
            
            # Générer un nouveau mot de passe basé sur la longueur actuelle
            if password_element is not None:
                current_password = password_element.text
                new_password_length = len(current_password)
                new_password = generate_password(new_password_length)
                password_element.text = new_password  # Mettre à jour le mot de passe

            print(f"Identifiant mis à jour pour l'URL: {url_element.text} avec nouveau mot de passe.")

    # Sauvegarder les modifications dans le fichier XML
    tree.write(chemin_fichier)