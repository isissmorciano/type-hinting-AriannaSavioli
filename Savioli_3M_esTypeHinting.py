#Savioli Arianna 3M
#esercizio type hinting
import random
#es 1
def descrizione(nome: str, eta: int) -> str:
    return f"{nome} ha {eta} anni."
print(descrizione("Pippo", 23))
#es 2
def numero_casuale() -> int:
    return random.randint(0, 99)
print(numero_casuale())
#es 3
def descrizione_eta_casuale(nome: str) -> str:
    eta = random.randint(0, 99)
    return f"{nome} ha {eta} anni."
print(descrizione_eta_casuale("Pippo"))
#es 4
def descrizione_casuale() -> str:
    nomi = ["Mario", "Luigi", "Giacomo", "Paolo", "Matteo"]
    nome = random.choice(nomi)
    eta = random.randint(0, 99)
    return f"{nome} ha {eta} anni."
print(descrizione_casuale())

