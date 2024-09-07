def format_rendimiento(l):
   if isinstance(l, str):
      if l == 'Sí, de manera negativa':
        return 1
      elif l == 'No tiene efecto':
        return 2
      elif l == 'Sí, de manera positiva':
        return 3
   else:
      return 0