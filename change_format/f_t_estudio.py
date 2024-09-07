def format_t_estudio(l):
   if isinstance(l, str):
      if l == 'No':
        return 1
      elif l == 'Si':
        return 2
   else:
      return 0