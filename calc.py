from scipy import stats

def calcular(data, name):
    media = data.mean()
    mediana = data.median()
    moda = data.mode()[0]
    media_geometrica = stats.gmean(data)
    media_armonica = stats.hmean(data)

    varianza = data.var()
    desviacion_estandar = data.std()
    coeficiente_variacion = desviacion_estandar / media

    print(f'\n-> Estadítica para: {name}')
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Media Geométrica: {media_geometrica}")
    print(f"Media Armónica: {media_armonica}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacion_estandar}")
    print(f"Coeficiente de Variación: {coeficiente_variacion}")