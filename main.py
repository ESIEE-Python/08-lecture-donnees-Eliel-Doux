"""
lecture des données contenues dans le fichier
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        l=[[int(val) for val in ll.split(";")] for ll in f.readlines()]
    return l

def get_list_k(data, k):
    """
    une fonction secondaire get_list_k() qui retourne la kième liste.
    """
    return data[k]

def get_first(l):
    """
    une fonction secondaire get_first() qui prend en argument une liste et 
    retourne le premier élément de cette liste
    """
    return l[0]

def get_last(l):
    """
    une fonction secondaire get_last() qui prend en argument une liste et 
    retourne le dernier élément de cette liste
    """
    return l[-1]

def get_max(l):
    """
    une fonction secondaire get_max() qui prend en argument une liste et 
    retourne le maximum de cette liste
    """
    return max(l)

def get_min(l):
    """
    une fonction secondaire get_min() qui prend en argument une liste et 
    retourne le minimum de cette liste
    """
    return min(l)

def get_sum(l):
    """
    une fonction secondaire get_sum() qui prend en argument une liste et 
    retourne la somme de cette liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    la fonction principale main() dont 
    le rôle est de faire appel aux fonctions secondaires pour vérifier leur bon fonctionnement
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
