def format_desplazamiento(l):
   if isinstance(l, str):
      if '-' in l:
         l = l.replace(' minutos', '')
         l1 = l.split('-')

         inferior = int(l1[0])
         superior = int(l1[1])

         return (inferior + superior) // 2
      elif 'Menos de 30 minutos' in l:
         return 29
   else:
      return 0