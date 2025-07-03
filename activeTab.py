import pygetwindow as gw
import pyautogui
from pytesseract import image_to_string, pytesseract

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

## Navigateur Brave (ou peut être Google Chrome ce sont les mêmes drivers)

def get_active_tab_url():
    windows = gw.getWindowsWithTitle("Brave")
    if not windows:
        return "Erreur : Impossible de trouver une fenêtre Brave active."
    
    # Activer la première fenêtre Brave trouvée
    window = windows[0]
    window.activate()

    # Définir une région pour capturer la barre d'adresse (ajustez les dimensions selon votre écran)
    left, top, width, height = window.left, window.top, window.width, 100  # Capture uniquement le haut de la fenêtre
    try:
        # Prendre une capture d'écran de la région spécifiée
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save("barre_adresse.png")  # Sauvegarde pour débogage
        url = image_to_string(screenshot, lang='eng')  # Utilisez 'eng' pour l'anglais
        return url.strip()
    except Exception as e:
        return f"Erreur lors de la capture de l'URL : {e}"
