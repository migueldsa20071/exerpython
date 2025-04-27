letra = input('Informe uma letra: ')

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print('Vogal')
    case _:
        print('Consoante')