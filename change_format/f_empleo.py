def format_empleo(l):
   if isinstance(l, str):
      if l == 'Temporal':
        return 1
      elif l == 'Medio tiempo':
        return 2
      elif l == 'Timepo completo':
         return 3
   else:
      return 0