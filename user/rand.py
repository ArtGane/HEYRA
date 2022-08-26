import random


def rand():
    x = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$^&*()-_'+%"

    lenghtAsk = int(input("Taille : "))
    generate = random.sample(x, lenghtAsk)
    pwd = "".join(generate)

    return pwd
