import tkinter as tk
import xml.etree.ElementTree as ET
import os

def view_data():
    xml_path = "data.xml"
    
    if not os.path.exists(xml_path):
        return "Aucune donnée trouvée."
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    output = ""
    
    for entry in root.findall('entry'):
        url = entry.find('url').text
        username = entry.find('username').text
        password = entry.find('password').text
        output += f"URL: {url}\nUsername: {username}\nPassword: {password}\n\n"
    
    return output

if __name__ == '__main__':
    print(view_data())