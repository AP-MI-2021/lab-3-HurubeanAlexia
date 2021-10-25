import sys

def citireLista():
    lst = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        lst.append(float(x))
    return lst


def is_palindrome(n):
    """
    verifica daca un nr este palindrom
    :param n: un nr intreg
    :return: True, daca nr este palindrom, False in caz contrar
    """
    inverse = 0
    copy = n
    while copy > 0:
        inverse = inverse * 10 + copy % 10
        copy = copy // 10
    if inverse == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(12421) is True
    assert is_palindrome(9887) is False
    assert is_palindrome(1234321) is True
    assert is_palindrome(7) is True
    assert is_palindrome(6760) is False


def all_is_palindrome(lst):
    """
    :param lst: lista de numere
    verifica daca toate elementele dintr-o lista sunt palindroame
    :return: True, daca toate elementele din lista sunt palindroame
             False daca se gaseste cel putin un numar daca nu respecta conditia
    """
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True


def get_longest_all_palindromes(lst: list[int]):
    """
    returneaza cea mai lunga secventa din lista cu numere consecutive de tip palindrom
    :param lst: lista de numere
    :return: secventa cea mai lunga cu numere de tip palindrom daca aceasta exista
             False in caz ca nu exista niciun numar palindrom
    """
    longestsequence = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if all_is_palindrome (lst[i:j + 1]) and len(lst[i:j + 1]) > len(longestsequence):
                longestsequence = lst[i:j + 1]
    return longestsequence


def test_get_longest_all_palindromes() -> list:
    assert get_longest_all_palindromes([3, 7, 23]) == [3, 7]
    assert get_longest_all_palindromes([56, 937, 100, 890, 9]) == [9]
    assert get_longest_all_palindromes([898, 66566, 3882, 191]) == [898, 66566]
    assert get_longest_all_palindromes([7834, 920, 856, 229]) == []


def is_power_k(n, k: int) -> bool:
    """
    determina daca un nr n poate fi scris ca x^k unde x este un numar intreg pozitiv
    :param n: numarul caruia ii verificam radacina de ordin k
    :param k: puterea la care il ridicam pe x
    :return: True, daca poate fi scris ca un nr intreg x la puterea k si false daca nu
    """

    if n ** (1 / k) == int(n ** (1 / k)):
        return True
    else:
        return False


def get_longest_powers_of_k(lst: list, k: int) -> bool:
    """
    determina cea mai lunga subsecventa formata din numere cu radacini de ordin k
    :param lst: lista de numere intregi
    :param k: ordinul radacinii pe care numerele trebuie sa o aiba
    :return: subsecventa cea mai lunga care are numere cu radacini de ordin k
    """
    start = -1
    subsecventa_max = []
    for i in range(len(lst)):
        if is_power_k(lst[i], k):
            if start == -1:
                start = i
            if len(subsecventa_max) < i - start + 1:
                subsecventa_max = lst[start:i + 1]
        else:
            start = -1
    return subsecventa_max


def test_is_power_k():
    assert is_power_k(8, 3) is True
    assert is_power_k(27, 4) is False
    assert is_power_k(81, 4) is True


def test_get_longest_power_of_k():
    assert get_longest_powers_of_k([3, 25, 7, 36, 49, 16], 2) == [36, 49, 16]
    assert get_longest_powers_of_k([8, 27, 17, 18, 9, 4, 64], 5) == []
    assert get_longest_powers_of_k([16, 81, 17, 18, 9, 4, 64], 4) == [16, 81]


def main():
    lst = []
    test_get_longest_all_palindromes()
    test_is_palindrome()
    test_is_power_k()
    test_get_longest_power_of_k()
    print("Testele au trecut cu succes")
    while True:
        print("1. Citire lista")
        print("2. Cea mai lunga secventa de numere palindrom")
        print("3. Cea mai lunga secventa de numere cu radacini de ordin k")
        print("4. Iesire")

        optiune = input("Alege optiunea: ")

        if optiune == '1':
            lst = citireLista()
        elif optiune == '2':
            print(get_longest_all_palindromes(lst))
        elif optiune == '3':
            k = int(input("Dati valoarea k: "))
            print(get_longest_powers_of_k(lst, k))
        elif optiune == '4':
            sys.exit()
        else:
            print("optiune invalida")


main()
