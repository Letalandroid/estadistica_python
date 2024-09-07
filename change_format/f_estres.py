def format_estres(l):
   if isinstance(l, str):
      if l == '1 (Muy poco estrés)':
        return 1
      elif l == '2 (Poco estrés)':
        return 2
      elif l == '3 (Estrés moderado)':
        return 3
      elif l == '4 (Mucho estrés)':
        return 4
      elif l == '5 (Extremo estrés)':
        return 5
   else:
      return 0