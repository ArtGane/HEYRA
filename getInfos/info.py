# Récupérer infos site
from user.rand import rand


def info():
    listInfos = []
    infos = []
    # get name
    name = "test nom"

    # get mail use
    mail = "test@mail.fr"

    # get password
    pwd = rand()

    # Put name and mail on list
    infos.append(name)
    infos.append(mail)
    infos.append(pwd)

    # Put object infos on list
    listInfos.append(infos)

    return listInfos

