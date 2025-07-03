import random
import os    
    
def generate_password(Length):   
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
    mdp = "".join(random.choice(letters) for i in range(Length))
    print(f"Mot de passe ok")
    return mdp
