import os
from activeTab import get_active_tab_url
from generatorMdp import generate_password

url = get_active_tab_url()
mdp = generate_password(8)

# Créer un dossier pour sauvegarder le mot de passe
dossier = os.path.join(os.getcwd(), "MotsDePasse")
chemin_fichier = os.path.join(dossier, "mot_de_passe.txt")

# Créer un dossier pour sauvegarder le mot de passe
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Sauvegarder le mot de passe dans un fichier en ajoutant une nouvelle ligne
with open(chemin_fichier, "a") as fichier:
    fichier.write(f"Informations pour {url} :  - {mdp}\n")

print(f"Le mot de passe a été sauvegardé dans : {chemin_fichier}")
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Sauvegarder le mot de passe dans un fichier
chemin_fichier = os.path.join(dossier, "mot_de_passe.txt")
with open(chemin_fichier, "w") as fichier:
    fichier.write(f"Informations pour {url} : {mdp}")

print(f"Le mot de passe a été sauvegardé dans : {chemin_fichier}")