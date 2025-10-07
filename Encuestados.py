import matplotlib.pyplot as plt
# =====================================================
# GRÁFICO DE LÍNEAS: ¿Cuántas horas dormiste anoche?
# =====================================================
personas = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10']
HorasDormidas = [4, 5, 6, 6, 7, 7, 7, 6, 5, 6]  # Limpiado

plt.figure(figsize=(8, 5))
plt.plot(personas, HorasDormidas, marker='o', color='blue', linewidth=2)
plt.title('Horas de sueño anoche (10 participantes)')
plt.xlabel('Personas')
plt.ylabel('Horas dormidas')
plt.grid(True)
plt.show()

# =====================================================
# GRÁFICO DE BARRAS: ¿Cuántas tazas de café tomas al día?
# =====================================================
TazasCafe = [0, 0, 0, 1, 1, 2, 3, 4, 1, 0]

# Contar cuántas personas respondieron cada cantidad
opciones = sorted(list(set(TazasCafe)))
frecuencias = [TazasCafe.count(x) for x in opciones]

plt.figure(figsize=(8, 5))
plt.bar(opciones, frecuencias, color='orange', edgecolor='black')
plt.title('Tazas de café por día (10 participantes)')
plt.xlabel('Tazas de café')
plt.ylabel('Número de personas')
plt.xticks(opciones)
plt.show()

# =====================================================
# GRÁFICO DE PASTEL: ¿Qué red social usas más?
# =====================================================
redes = ['Facebook', 'Instagram', 'TikTok', 'TikTok', 'Instagram', 'Facebook', 'TikTok', 'WhatsApp', 'YouTube', 'TikTok']

# Contar cuántas veces se repite cada red social
labels = sorted(list(set(redes)))
valores = [redes.count(x) for x in labels]

plt.figure(figsize=(7, 7))
plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Red social más usada (10 participantes)')
plt.show()

# =====================================================
# HISTOGRAMA: ¿Cuánto tiempo tardas en llegar a la universidad?
# =====================================================
# Datos en minutos (limpiados)
tiempos = [10, 15, 15, 20, 25, 30, 30, 40, 60, 120]

plt.figure(figsize=(8, 5))
plt.hist(tiempos, bins=6, color='green', edgecolor='black')
plt.title('Tiempo para llegar a la universidad (10 participantes)')
plt.xlabel('Minutos')
plt.ylabel('Número de personas')
plt.show()
