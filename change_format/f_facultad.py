def format_facultad(l):
   if isinstance(l, str):
      if l == 'Economía':
        return 1
      elif l == 'Ingeniería':
        return 2
      elif l == 'Ciencias':
        return 3
      elif l == 'Ciencias de la Salud':
        return 4
      elif l == 'Derecho':
        return 5
      elif l == 'Agronomia':
        return 6
      elif l == 'Educación':
        return 7
      elif l == 'Ciencias de la comunicación':
        return 8
      elif l == 'Ciencias Administrativas':
        return 9
      elif l == 'Contabilidad ':
        return 10
   else:
      return 0