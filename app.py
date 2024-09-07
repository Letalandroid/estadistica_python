print('\n[!] Realizando calculos, esto podria demorar un poco...')

import pandas as pd
from change_format import f_edad, f_gen, f_ciclo, f_n_socioeco, f_estado, f_resp, f_calif, f_h_estudio, f_extras, f_academico, f_chamba, f_trabjadas, f_empleo, f_carrera, f_flexible, f_desplazamiento, f_rendimiento, f_facultad, f_estres, f_t_estudio
import calc

archivo = "RESPUESTAS.xlsx"
df = pd.read_excel(archivo)
print(f'Calculo realizado en {len(df)} filas/columnas.')

edad = df['Edad'].apply(f_edad.format_edad)
calc.calcular(edad, 'edad')

genero = df['Género'].apply(f_gen.format_gen)
# Masculino: 0
# Femenino: 1
calc.calcular(genero, 'genero')

ciclo = df['Año de estudio'].apply(f_ciclo.format_ciclo)
calc.calcular(ciclo, 'ciclo')

n_socioeco = df['Nivel socioeconómico (según tu percepción)'].apply(f_n_socioeco.format_socioeco)
# 0: Bajo
# 1: Medio
# 2: Alto
calc.calcular(n_socioeco, 'Nivel socioeconomico')

e_civil = df['Estado civil'].apply(f_estado.format_estado)
calc.calcular(e_civil, 'Estado Civil')

responsabilidades = df['¿Tienes responsabilidades familiares (ej. cuidado de hijos, familiares mayores)?'].apply(f_resp.format_respon)
# 1: No
# 2: Si
calc.calcular(responsabilidades, 'Responsabilidades')

p_calificaciones = df['Promedio general de calificaciones'].apply(f_calif.format_calif)
calc.calcular(p_calificaciones, 'Calificaciones')

h_estudio = df['¿Cuántas horas dedicas al estudio fuera del horario de clases por semana?'].apply(f_h_estudio.format_estudio)
calc.calcular(h_estudio, 'Horas de estudio')

a_extras = df['¿Participas en actividades extracurriculares (deporte, cultura, etc.)?'].apply(f_extras.format_extras)
# 1: No
# 2: Si
calc.calcular(a_extras, 'Horas extras')

r_academico = df['¿Cómo calificarías tu rendimiento académico actual?'].apply(f_academico.format_academic)
# 0: Bajo
# 1: Regular
# 2: Alto
calc.calcular(r_academico, 'Rendimiento academico')

chamba = df['¿Trabajas actualmente?'].apply(f_chamba.format_chamba)
# 1: No
# 2: Si
calc.calcular(chamba, '¿Chamba o no chamba?')

h_trabajadas = df['¿Cuántas horas trabajas en promedio por semana?'].apply(f_trabjadas.format_trabajadas)
calc.calcular(h_trabajadas, 'Horas trabajadas')

empleo = df['¿Qué tipo de empleo tienes?'].apply(f_empleo.format_empleo)
# 1: Temporal
# 2: Medio tiempo
# 3: Tiempo completo
calc.calcular(empleo, 'Tipo de empleo')

t_carrera = df['¿El trabajo que realizas está relacionado con tu carrera de estudios?'].apply(f_carrera.format_carrera)
# 1: Si
# 2: No
calc.calcular(t_carrera, 'Trabajo relacionado con carrera')

h_flexible = df['¿Tu trabajo actual tiene un horario flexible?'].apply(f_flexible.format_flexible)
# 1: No
# 2: A veces
# 3: Si
calc.calcular(h_flexible, 'Horario flexible')

h_desplazamiento = df['¿Cuánto tiempo te toma desplazarte hacia tu trabajo (ida y vuelta)?'].apply(f_desplazamiento.format_desplazamiento)
calc.calcular(h_desplazamiento, 'Horas de desplazamiento')

t_rendimiento = df['¿Consideras que trabajar afecta tu rendimiento académico?'].apply(f_rendimiento.format_rendimiento)
# 1: Sí, de manera negativa
# 2: No tiene efecto
# 3: Sí, de manera positiva
calc.calcular(t_rendimiento, 'Rendimiento academico')

c_estudio = df['En una escala del 1 al 5, ¿cuánto estrés sientes al combinar trabajo y estudio?'].apply(f_estres.format_estres)
calc.calcular(c_estudio, 'Combinar trabajo + estudio')

t_conocimientos = df['¿Consideras que el trabajo te ayuda a aplicar los conocimientos adquiridos en tus estudios?'].apply(f_t_estudio.format_t_estudio)
# 1: No
# 2: Si
calc.calcular(t_conocimientos, 'Aplicar trabajo en estudio')

#! [!] Sin terminar
# e_equilibrar = df['¿Qué estrategias utilizas para equilibrar el trabajo y el estudio? (puedes seleccionar más de una opción)']
#! [!] Sin terminar

facultad = df['Facultad'].apply(f_facultad.format_facultad)
# Economía: 1
# Ingeniería: 2
# Ciencias: 3
# Ciencias de la Salud: 4
# Derecho: 5
# Agronomia: 6
# Educación: 7
# Ciencias de la comunicación: 8
# Ciencias Administrativas: 9
# Contabilidad : 10
calc.calcular(facultad, 'Facultad')

print('')