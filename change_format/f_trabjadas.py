def format_trabajadas(l):
   if isinstance(l, str):
      if '-' in l:
         l = l.replace(' horas', '')
         l1 = l.split('-')

         inferior = int(l1[0])
         superior = int(l1[1])

         return (inferior + superior) // 2
      elif 'Menos de 10 horas' in l:
         return 9
   else:
      return 0