def format_estudio(l):
   if '-' in l:
      l = l.replace(' horas', '')
      l1 = l.split('-')

      inferior = int(l1[0])
      superior = int(l1[1])

      return (inferior + superior) // 2
   elif 'Menos de 18' in l:
        return 17