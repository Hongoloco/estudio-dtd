# PRUEBA DE PRÁCTICA - MATERIAL ESTUDIO IP
## Llamados Técnicos 2025

**Instrucciones**: Selecciona la respuesta correcta para cada pregunta. Las respuestas se encuentran al final del documento.

---

## SECCIÓN 1: BERT - PRUEBAS DE TASA DE ERRORES DE BITS (20 preguntas)

### 1. ¿Qué significa BER?
a) Bit Error Recovery  
b) Bit Error Rate  
c) Binary Error Reduction  
d) Byte Error Rate

### 2. ¿Qué valor de BER se considera generalmente aceptable en telecomunicaciones?
a) 10⁻⁶  
b) 10⁻⁹  
c) 10⁻¹²  
d) 10⁻¹⁵

### 3. ¿Qué valor de BER se considera apropiado para transmisión de datos?
a) 10⁻⁹  
b) 10⁻¹³  
c) 10⁻⁶  
d) 10⁻³

### 4. ¿Qué significan las siglas BERT?
a) Bit Error Rate Testing  
b) Binary Error Rate Transmission  
c) Bit Error Recovery Test  
d) Binary Error Reduction Testing

### 5. ¿Qué es una secuencia PRBS?
a) Primary Rate Bit Sequence  
b) Pseudo-Random Bit Sequence  
c) Protocol Rate Bit System  
d) Primary Random Binary Signal

### 6. ¿Para qué se utiliza una secuencia PRBS en BERT?
a) Para reducir el tiempo de transmisión  
b) Para crear patrones que puedan generar errores y acelerar las pruebas  
c) Para cifrar los datos  
d) Para comprimir la información

### 7. La tasa de errores de bits (BER) se calcula como:
a) Bits totales / Bits con error  
b) Bits con error / Bits totales  
c) Bits correctos / Bits totales  
d) Tiempo total / Errores detectados

### 8. ¿Qué mide la PER (Packet Error Rate)?
a) La velocidad de transmisión de paquetes  
b) La relación de paquetes que no llegan a su destino  
c) El tamaño de los paquetes  
d) El tiempo de propagación de paquetes

### 9. ¿Cuál es una causa común de pérdida de paquetes?
a) Exceso de ancho de banda  
b) Congestión de red  
c) Baja latencia  
d) Alta ganancia de señal

### 10. La latencia se define como:
a) El ancho de banda disponible  
b) El número de paquetes perdidos  
c) El tiempo que tardan los datos en transmitirse de una ubicación a otra  
d) La velocidad de la fibra óptica

### 11. ¿Qué efecto tiene una latencia alta en aplicaciones VoIP?
a) Mejora la calidad de voz  
b) Reduce el consumo de ancho de banda  
c) Puede provocar cuellos de botella y calidad deficiente  
d) No tiene efecto

### 12. La fluctuación (jitter) se define como:
a) La velocidad promedio de transmisión  
b) La variación en el retraso de la recepción de paquetes  
c) El número de errores por segundo  
d) La potencia de la señal

### 13. ¿Qué tipo de transmisiones son más sensibles a la fluctuación excesiva?
a) Transferencias de archivos  
b) Email  
c) Voz y vídeo  
d) Texto

### 14. Las BERT son importantes porque:
a) Solo sirven para redes de baja velocidad  
b) Garantizan el rendimiento de redes de alta velocidad y mejoran la satisfacción del cliente  
c) Reemplazan a los protocolos de routing  
d) Solo se usan en laboratorios

### 15. ¿Pueden las rutinas de corrección de errores de Ethernet enmascarar problemas físicos de red?
a) No, siempre detectan todos los problemas  
b) Sí, pueden ocultar problemas inherentes a la red física  
c) Solo en redes inalámbricas  
d) Solo en redes de cobre

### 16. Los paquetes retransmitidos debido a errores de bits pueden:
a) Mejorar el rendimiento de la red  
b) Aumentar el ancho de banda disponible  
c) Mermar el rendimiento y contribuir a problemas de congestión  
d) Reducir la latencia

### 17. ¿Cuáles son posibles causas de errores de bits en redes de fibra óptica?
a) Solo la humedad  
b) Atenuación, dispersión y otras causas  
c) Solo la temperatura  
d) Solo interferencia electromagnética

### 18. Entre los KPI que se pueden medir con BERT están:
a) Solo la velocidad de transmisión  
b) Pérdida de paquetes, latencia y fluctuación  
c) Solo el voltaje  
d) Solo la temperatura

### 19. Las BERT en redes internas pueden:
a) Reducir la necesidad de mantenimiento  
b) Garantizar operaciones eficaces especialmente en circuitos de gran tamaño  
c) Eliminar la necesidad de switches  
d) Aumentar automáticamente el ancho de banda

### 20. ¿Qué puede indicar una pérdida significativa de paquetes?
a) Red óptima  
b) Servicio lento o interrupciones en la red, posibles ataques DOS  
c) Exceso de ancho de banda  
d) Configuración perfecta

---

## SECCIÓN 2: RFC 2544 (15 preguntas)

### 21. ¿En qué año se desarrolló el estándar RFC 2544?
a) 1995  
b) 1999  
c) 2004  
d) 2010

### 22. ¿Qué organización desarrolló RFC 2544?
a) IEEE  
b) ISO  
c) IETF (Internet Engineering Task Force)  
d) ITU-T

### 23. RFC 2544 fue diseñado originalmente para:
a) Pruebas de campo en producción  
b) Evaluación comparativa de equipos de red en laboratorio  
c) Configuración de routers  
d) Certificación de cables

### 24. ¿A qué capas del modelo OSI se enfoca RFC 2544?
a) Capa 1 únicamente  
b) Capa 2/3  
c) Capa 7  
d) Todas las capas

### 25. ¿Qué mide el "Throughput" en RFC 2544?
a) La latencia mínima  
b) La tasa máxima de transferencia sin pérdida de tramas  
c) El número de dispositivos conectados  
d) La temperatura del equipo

### 26. Los tamaños de trama estandarizados en RFC 2544 incluyen (en bytes):
a) 32, 64, 128, 256  
b) 64, 128, 256, 512, 1024, 1280, 1518  
c) 100, 200, 300, 400  
d) 512, 1024, 2048

### 27. ¿Qué significa "Back-to-Back" en RFC 2544?
a) Conexión de dos switches  
b) Capacidad para procesar ráfagas sucesivas sin pérdida  
c) Configuración redundante  
d) Backup de configuración

### 28. La latencia en RFC 2544 se puede medir como:
a) Solo one-way  
b) Solo RTT (Round Trip Time)  
c) RTT si no hay sincronización, o one-way con sincronización GPS/PTP  
d) No se mide latencia en RFC 2544

### 29. ¿Qué prueba de RFC 2544 evalúa la capacidad de manejar ráfagas de tramas?
a) Throughput  
b) Latency  
c) Back-to-Back  
d) System Reset

### 30. ¿Qué mide la prueba de "System Reset"?
a) La velocidad de transmisión  
b) El tiempo de recuperación del equipo tras un reinicio  
c) El número de puertos disponibles  
d) La temperatura de operación

### 31. Una limitación de RFC 2544 es que:
a) Es muy lento  
b) No modela múltiples servicios simultáneos  
c) Solo funciona en redes inalámbricas  
d) Requiere equipos muy costosos

### 32. ¿Qué estándar es más adecuado para escenarios multiservicio que RFC 2544?
a) RFC 1918  
b) ITU-T Y.1564  
c) IEEE 802.3  
d) RFC 791

### 33. Un criterio de aceptación típico para Throughput es:
a) ≥ 50% de line rate  
b) ≥ 99% de line rate a MTU estándar sin pérdida  
c) ≥ 25% de line rate  
d) ≥ 75% de line rate con 10% de pérdida

### 34. Para pruebas de latencia RTT a 10G, un valor típico aceptable es:
a) ≤ 10 ms  
b) ≤ 1 ms  
c) ≤ 300 µs  
d) ≤ 100 µs

### 35. ¿Qué debe hacerse antes de cada corrida de prueba RFC 2544?
a) Apagar todos los equipos  
b) Resetear contadores y verificar estado inicial  
c) Cambiar todos los cables  
d) Actualizar el firmware

---

## SECCIÓN 3: FIBRAS ÓPTICAS (20 preguntas)

### 36. Las fibras ópticas se clasifican en dos grandes tipos:
a) Cortas y largas  
b) Monomodo y Multimodo  
c) Rápidas y lentas  
d) Internas y externas

### 37. ¿Qué significa SM en fibras ópticas?
a) Small Mode  
b) Single Mode (Monomodo)  
c) Super Mode  
d) Standard Mode

### 38. ¿Qué significa MM en fibras ópticas?
a) Maximum Mode  
b) Mini Mode  
c) Multi Mode (Multimodo)  
d) Medium Mode

### 39. ¿De qué color suele ser la cubierta de fibras monomodo?
a) Verde o rojo  
b) Amarillo o azul  
c) Negro o blanco  
d) Violeta o rosa

### 40. ¿De qué color suele ser la cubierta de fibras multimodo?
a) Amarillo  
b) Azul  
c) Naranja  
d) Verde

### 41. El núcleo (core) de una fibra monomodo típica tiene un diámetro de:
a) 50-62.5 μm  
b) 125 μm  
c) 8-10 μm  
d) 250 μm

### 42. ¿Qué es el "cladding" en una fibra óptica?
a) La cubierta externa de plástico  
b) El revestimiento de vidrio alrededor del núcleo  
c) El gel protector  
d) El cable de kevlar

### 43. ¿Qué es el "buffer" o recubrimiento primario?
a) El núcleo de la fibra  
b) La protección primaria alrededor del cladding  
c) El gel anticongelante  
d) El elemento de tracción

### 44. Las protecciones secundarias en fibras ópticas pueden ser:
a) Solo rígidas  
b) Ajustadas u holgadas  
c) Solo flexibles  
d) Solo metálicas

### 45. ¿Qué contienen los tubos en la estructura holgada?
a) Aire comprimido  
b) Un gel anticongelante que protege las fibras  
c) Agua destilada  
d) Aceite mineral

### 46. ¿Cuál es el diámetro del recubrimiento primario estándar de una fibra?
a) 125 μm  
b) 250 μm  
c) 500 μm  
d) 900 μm

### 47. En un cable de fibra óptica, ¿qué material se usa comúnmente como elemento de tracción?
a) Cobre  
b) Aluminio  
c) Kevlar  
d) Titanio

### 48. Los cables de fibra óptica ajustados típicamente se usan:
a) Solo en interiores  
b) En exterior, se recomienda en ducto  
c) Sumergidos en agua  
d) Solo para conexiones temporales

### 49. ¿Cuántas fibras puede contener típicamente un cable ajustado de exterior?
a) 1-4 fibras  
b) 8-36 fibras  
c) 100-200 fibras  
d) 500+ fibras

### 50. La diferencia fundamental entre fibras monomodo y multimodo es:
a) El color de la cubierta  
b) Su estructura y diseño, tienen distintos usos  
c) El fabricante  
d) El precio

### 51. ¿Qué permite la reflexión total en el núcleo de la fibra?
a) El gel anticongelante  
b) Dos capas de vidrio con distintos índices de refracción  
c) El kevlar  
d) La cubierta de plástico

### 52. En una estructura holgada, las fibras están:
a) Pegadas al tubo  
b) Sueltas dentro del tubo con gel  
c) Comprimidas  
d) Soldadas al cable central

### 53. ¿Por qué se debe ser cauteloso al retirar el gel de los tubos?
a) Es tóxico  
b) Es explosivo  
c) Es anticongelante y no se escurre fácilmente  
d) Es muy caliente

### 54. El diámetro del tubo en protección ajustada es típicamente:
a) 0.5-1 mm  
b) 2-3 mm  
c) 5-10 mm  
d) 15-20 mm

### 55. ¿Para qué distancias son más adecuadas las fibras multimodo?
a) Más de 100 km  
b) Distancias cortas (hasta unos pocos km)  
c) Solo para enlaces intercontinentales  
d) No hay diferencia de distancia

---

## SECCIÓN 4: TRANSCEPTORES ÓPTICOS (25 preguntas)

### 56. ¿Qué es un transceptor óptico?
a) Un cable especial  
b) Un dispositivo que convierte señales eléctricas en ópticas y viceversa  
c) Un tipo de fibra  
d) Un router óptico

### 57. ¿En qué capa del modelo OSI trabaja un transceptor óptico?
a) Capa 7 (Aplicación)  
b) Capa 4 (Transporte)  
c) Capa 3 (Red)  
d) Capa 1 (Física)

### 58. Las funciones principales del transceptor son:
a) Solo transmitir  
b) Solo recibir  
c) Transmitir (Tx) y Recibir (Rx)  
d) Enrutar paquetes

### 59. ¿Qué componente genera la señal óptica en el transmisor?
a) Fotodiodo  
b) Láser o LED  
c) Amplificador  
d) Condensador

### 60. ¿Qué componente detecta la señal óptica en el receptor?
a) Láser  
b) LED  
c) Fotodiodo  
d) Transistor

### 61. SMF en transceptores significa:
a) Small Mode Fiber  
b) Single Mode Fiber (fibra monomodo)  
c) Super Mode Fiber  
d) Standard Mode Fiber

### 62. MMF en transceptores significa:
a) Maximum Mode Fiber  
b) Multi Mode Fiber (fibra multimodo)  
c) Medium Mode Fiber  
d) Mini Mode Fiber

### 63. ¿Qué significa SFP?
a) Super Fast Protocol  
b) Small Form-Factor Pluggable  
c) Single Fiber Protocol  
d) Standard Fiber Port

### 64. ¿Qué significa QSFP?
a) Quick Small Form Protocol  
b) Quad Small Form-Factor Pluggable  
c) Quality Standard Fiber Port  
d) Quantum Single Fiber Protocol

### 65. SR en transceptores significa:
a) Super Reach  
b) Short Reach (corto alcance)  
c) Standard Reach  
d) Slow Rate

### 66. LR en transceptores significa:
a) Low Reach  
b) Long Reach (alcance largo, hasta 10 km)  
c) Light Reach  
d) Limited Rate

### 67. ER en transceptores significa:
a) Extra Rate  
b) Extended Reach (alcance extendido, hasta 40 km)  
c) Extreme Reach  
d) Efficient Rate

### 68. ZR en transceptores significa:
a) Zero Reach  
b) ZR reach (alcance extendido, 80 km o más)  
c) Zone Reach  
d) Zenith Rate

### 69. ¿Qué almacena la EEPROM en un transceptor?
a) Los datos de usuario  
b) Información de fabricante, modelo y configuración  
c) El sistema operativo  
d) Las claves de encriptación

### 70. Los conectores ópticos comunes en transceptores incluyen:
a) RJ45, USB  
b) LC, SC, MPO  
c) HDMI, DVI  
d) BNC, F-Type

### 71. ¿Qué es el "power budget" o presupuesto óptico?
a) El costo del transceptor  
b) La cantidad de luz necesaria para transmitir señales exitosamente  
c) El consumo eléctrico del módulo  
d) El precio de la instalación

### 72. El presupuesto óptico se calcula como:
a) Tx máximo - Rx máximo  
b) Tx mínimo - Rx sensibilidad mínima  
c) Solo la potencia del transmisor  
d) La distancia del cable

### 73. Para que un enlace funcione correctamente, las pérdidas del enlace deben ser:
a) Mayores que el power budget  
b) Menores o iguales al power budget  
c) Exactamente iguales al power budget  
d) No importa la relación

### 74. ¿Qué factores contribuyen a las pérdidas en un enlace óptico?
a) Solo la fibra  
b) Fibra, conectores, empalmes y factores ambientales  
c) Solo los conectores  
d) Solo la temperatura

### 75. La atenuación típica de un cable de fibra está entre:
a) 0.01 - 0.1 dB/km  
b) 0.22 - 0.5 dB/km  
c) 1 - 2 dB/km  
d) 5 - 10 dB/km

### 76. Una pérdida típica por empalme es aproximadamente:
a) 0.01 dB  
b) 0.1 dB  
c) 1 dB  
d) 10 dB

### 77. Según el estándar TIA, la pérdida típica por conector es:
a) 0.1 dB  
b) 0.75 dB  
c) 1.5 dB  
d) 3 dB

### 78. El margen de seguridad recomendado en un enlace óptico es:
a) 0.1 - 0.5 dB  
b) 1.7 - 3 dB  
c) 5 - 10 dB  
d) 15 - 20 dB

### 79. Si el Power Margin (margen de potencia) es negativo, significa que:
a) El enlace funcionará perfectamente  
b) No hay suficiente potencia para que la red funcione correctamente  
c) Hay exceso de potencia  
d) Es el valor ideal

### 80. ¿Qué medida se puede tomar si el presupuesto óptico es insuficiente?
a) Ignorar el problema  
b) Usar un módulo con mayor potencia, mejor sensibilidad, o agregar amplificación  
c) Reducir la velocidad de la red  
d) Cambiar el color de los cables

---

# RESPUESTAS CORRECTAS

## SECCIÓN 1: BERT - PRUEBAS DE TASA DE ERRORES DE BITS
1. **b)** Bit Error Rate
2. **b)** 10⁻⁹
3. **b)** 10⁻¹³
4. **a)** Bit Error Rate Testing
5. **b)** Pseudo-Random Bit Sequence
6. **b)** Para crear patrones que puedan generar errores y acelerar las pruebas
7. **b)** Bits con error / Bits totales
8. **b)** La relación de paquetes que no llegan a su destino
9. **b)** Congestión de red
10. **c)** El tiempo que tardan los datos en transmitirse de una ubicación a otra
11. **c)** Puede provocar cuellos de botella y calidad deficiente
12. **b)** La variación en el retraso de la recepción de paquetes
13. **c)** Voz y vídeo
14. **b)** Garantizan el rendimiento de redes de alta velocidad y mejoran la satisfacción del cliente
15. **b)** Sí, pueden ocultar problemas inherentes a la red física
16. **c)** Mermar el rendimiento y contribuir a problemas de congestión
17. **b)** Atenuación, dispersión y otras causas
18. **b)** Pérdida de paquetes, latencia y fluctuación
19. **b)** Garantizar operaciones eficaces especialmente en circuitos de gran tamaño
20. **b)** Servicio lento o interrupciones en la red, posibles ataques DOS

## SECCIÓN 2: RFC 2544
21. **b)** 1999
22. **c)** IETF (Internet Engineering Task Force)
23. **b)** Evaluación comparativa de equipos de red en laboratorio
24. **b)** Capa 2/3
25. **b)** La tasa máxima de transferencia sin pérdida de tramas
26. **b)** 64, 128, 256, 512, 1024, 1280, 1518
27. **b)** Capacidad para procesar ráfagas sucesivas sin pérdida
28. **c)** RTT si no hay sincronización, o one-way con sincronización GPS/PTP
29. **c)** Back-to-Back
30. **b)** El tiempo de recuperación del equipo tras un reinicio
31. **b)** No modela múltiples servicios simultáneos
32. **b)** ITU-T Y.1564
33. **b)** ≥ 99% de line rate a MTU estándar sin pérdida
34. **c)** ≤ 300 µs
35. **b)** Resetear contadores y verificar estado inicial

## SECCIÓN 3: FIBRAS ÓPTICAS
36. **b)** Monomodo y Multimodo
37. **b)** Single Mode (Monomodo)
38. **c)** Multi Mode (Multimodo)
39. **b)** Amarillo o azul
40. **c)** Naranja
41. **c)** 8-10 μm
42. **b)** El revestimiento de vidrio alrededor del núcleo
43. **b)** La protección primaria alrededor del cladding
44. **b)** Ajustadas u holgadas
45. **b)** Un gel anticongelante que protege las fibras
46. **b)** 250 μm
47. **c)** Kevlar
48. **b)** En exterior, se recomienda en ducto
49. **b)** 8-36 fibras
50. **b)** Su estructura y diseño, tienen distintos usos
51. **b)** Dos capas de vidrio con distintos índices de refracción
52. **b)** Sueltas dentro del tubo con gel
53. **c)** Es anticongelante y no se escurre fácilmente
54. **b)** 2-3 mm
55. **b)** Distancias cortas (hasta unos pocos km)

## SECCIÓN 4: TRANSCEPTORES ÓPTICOS
56. **b)** Un dispositivo que convierte señales eléctricas en ópticas y viceversa
57. **d)** Capa 1 (Física)
58. **c)** Transmitir (Tx) y Recibir (Rx)
59. **b)** Láser o LED
60. **c)** Fotodiodo
61. **b)** Single Mode Fiber (fibra monomodo)
62. **b)** Multi Mode Fiber (fibra multimodo)
63. **b)** Small Form-Factor Pluggable
64. **b)** Quad Small Form-Factor Pluggable
65. **b)** Short Reach (corto alcance)
66. **b)** Long Reach (alcance largo, hasta 10 km)
67. **b)** Extended Reach (alcance extendido, hasta 40 km)
68. **b)** ZR reach (alcance extendido, 80 km o más)
69. **b)** Información de fabricante, modelo y configuración
70. **b)** LC, SC, MPO
71. **b)** La cantidad de luz necesaria para transmitir señales exitosamente
72. **b)** Tx mínimo - Rx sensibilidad mínima
73. **b)** Menores o iguales al power budget
74. **b)** Fibra, conectores, empalmes y factores ambientales
75. **b)** 0.22 - 0.5 dB/km
76. **b)** 0.1 dB
77. **b)** 0.75 dB
78. **b)** 1.7 - 3 dB
79. **b)** No hay suficiente potencia para que la red funcione correctamente
80. **b)** Usar un módulo con mayor potencia, mejor sensibilidad, o agregar amplificación

---

## PUNTUACIÓN
- **80 preguntas totales**
- Sección 1 (BERT): 20 preguntas
- Sección 2 (RFC 2544): 15 preguntas
- Sección 3 (Fibras Ópticas): 20 preguntas
- Sección 4 (Transceptores Ópticos): 25 preguntas

**Escala de calificación sugerida:**
- 72-80 correctas (90-100%): Excelente
- 64-71 correctas (80-89%): Muy bien
- 56-63 correctas (70-79%): Bien
- 48-55 correctas (60-69%): Aprobado
- Menos de 48 (< 60%): Necesita repasar

---

**¡Buena suerte en tu preparación!** 🎯
