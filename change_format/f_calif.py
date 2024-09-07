def format_calif(l):
    if 'Menos de 10' in l:
        return 9

    elif '-' in l:
        limites = l.split('-')
        inferior = int(limites[0])
        superior = int(limites[1])
        return (inferior + superior) // 2