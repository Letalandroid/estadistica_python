def format_flexible(l):
   if isinstance(l, str):
      if l == 'No':
        return 1
      elif l == 'A veces':
        return 2
      elif l == 'Si':
        return 3
   else:
      return 0