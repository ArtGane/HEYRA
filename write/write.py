from xml.dom import minidom

from write.save import save


def write(listInfos):

    for info in listInfos:
        root = minidom.Document()

        xml = root.createElement('heyra')
        root.appendChild(xml)

        productChild = root.createElement('')
        productChild.setAttribute('nom', 'nom site')
        productChild.setAttribute('mail', 'mail utilise')
        productChild.setAttribute('pwd', 'mdp genere')

        xml.appendChild(productChild)
        xml_str = root.toprettyxml(indent="\t")

        save(xml_str)

        return xml_str
