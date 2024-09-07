def format_carrera(l):
   if isinstance(l, str):
      if l == 'No':
        return 1
      elif l == 'Si':
        return 2
   else:
      return 0