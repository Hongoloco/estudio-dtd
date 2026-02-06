# 📚 RESÚMENES DE ESTUDIO - Llamados Técnicos 2025

## Índice
1. [Material estudio Radio](#material-estudio-radio)
   - [MW Radio Propagation](#1-mw-radio-propagation)
   - [Configuraciones Ericsson Minilink](#2-configuraciones-ericsson-minilink)
   - [Manual Introducción Redes TCP/IP](#3-manual-introducción-redes-tcpip)
2. [Material estudio IP](#material-estudio-ip)
   - [BERT Manual](#4-bert-manual)
   - [RFC 2544 Manual](#5-rfc-2544-manual)
   - [Módulo 1 - Tipos de Fibras Ópticas](#6-módulo-1---tipos-de-fibras-ópticas)
   - [Transceptores Ópticos](#7-transceptores-ópticos)

---

# MATERIAL ESTUDIO RADIO

## 1. MW Radio Propagation

### 📡 **Conceptos Fundamentales**

#### **Relación entre Frecuencia y Longitud de Onda**
- **Fórmula clave**: λ (cm) = 30/f (GHz)
- A mayor frecuencia, menor longitud de onda

#### **Factor k (Earth Radius Factor)**
- En atmósfera estándar: **k ≈ 4/3 = 1.33**
- Radio efectivo de la Tierra: **≈ 8,500 km**
- Gradiente de refractividad típico: **-40 N units/km**

### 🌍 **Efectos en la Propagación**

#### **Efectos de Frecuencia**
- **< 10 GHz**: Efectos de terreno y tropósfera dominan
- **≥ 10 GHz**: Precipitación (lluvia) comienza a dominar
- **~ 23 GHz**: Pico de absorción de vapor de agua
- **50-70 GHz**: Pico de absorción de oxígeno (máximo a ~60 GHz)

#### **Mecanismos de Propagación**
1. **Propagación en Espacio Libre**: Pérdida básica (ABF)
2. **Refracción**: Curvatura del haz por variaciones atmosféricas
3. **Difracción**: Pérdidas por obstáculos (modelo knife-edge)
4. **Reflexión y Dispersión**: Coeficiente de reflexión (ρ)
5. **Absorción**: Por gases atmosféricos
6. **Fading**: Desvanecimiento (multipath, rain fading)

### 📏 **Zona de Fresnel**
- **Despejamiento mínimo requerido**: 60% de la primera zona de Fresnel
- **Fórmula del radio**: rF = 17.3√(d₁×d₂)/(f×d) [km]
- Una zona despejada evita pérdidas por difracción

### 🔍 **Criterio de Rayleigh**
- Determina si una superficie es **lisa** (reflexión especular) o **rugosa** (dispersión)
- Depende de la longitud de onda, rugosidad y ángulo de incidencia

### 📊 **Link Budget**
**Componentes principales:**
- Potencia de transmisión (EIRP)
- Pérdida en espacio libre (ABF)
- Ganancia de antenas (ΣG)
- Pérdida por obstáculos (Ao)
- Pérdida por reflexión (AL)
- Margen de desvanecimiento (hasta 40 dB típico)

### 🎯 **Etapas del Diseño de Red**
1. **Planning**: Capacidad, frecuencias, ubicaciones preliminares
2. **Survey**: Mapas y campo, verificación de sitios
3. **Engineering**: Cálculos de propagación e interferencia
4. **Test**: Mediciones y ajustes finales

---

## 2. Configuraciones Ericsson Minilink

### 🔧 **Familias de Equipos**

#### **Equipos TN (Traffic Node) - Configuración Split**
- **RAU**: Unidad exterior (junto a la antena)
- **AMM**: Unidad interior (con placas MMU)
- **Ventaja**: Pérdidas de RF muy bajas (guías de onda cortas)

#### **Equipos LH (Long Haul)**
- Todo en rack interior, conectado a antena por guía de onda
- Más sencillo para múltiples radiocanales

#### **Nueva Generación**
- **Familia 6300**: Reemplaza RAUs (modelos 6363, 6364, 6365)
- **Familia 6600**: Reemplaza AMMs (modelos 6651, 6692, 6694)

### 📻 **Bandas Radioeléctricas Utilizadas**

| Banda | Recomendación ITU | Ancho de Canal | Canales |
|-------|------------------|----------------|---------|
| **6L** | F.383 | 28 MHz (de 29.65 MHz) | 8 canales |
| **6U** | F.384 | 40 MHz | 8 canales |
| **7 GHz** | F.385 | 28 MHz / 56 MHz | 5 (28 MHz), 2 (56 MHz) |
| **8 GHz** | F.386 | 28/56/112 MHz | 8 (28 MHz) |
| **15 GHz** | F.636 | 28/56/112 MHz | Variable |

### ⚙️ **Configuraciones de Radiocanales**

#### **ACCP** (Adjacent Channel Co-Polarization)
- Canales adyacentes, misma polarización (ej: 1V, 2V)
- Antena de **simple polarización**

#### **ACAP** (Adjacent Channel Alternate Polarized)
- Canales adyacentes, polarizaciones alternadas (ej: 1V, 2H)
- Requiere antena de **doble polarización**

#### **CCDP** (Co-Channel Dual Polarized)
- Mismo canal, polarizaciones opuestas (ej: 1V, 1H)
- **Requiere XPIC** (Cross-Polar Interference Canceller)
- Antena de **doble polarización**

### 🛡️ **Configuraciones de Protección**

#### **1+1 Hot Standby sin Diversidad**
- 2 RAUs por extremo (working + standby)
- 1 antena por extremo
- Protección de **hardware solamente**

#### **1+1 Hot Standby con Diversidad de Espacio**
- 2 RAUs por extremo
- 2 antenas por extremo (principal + diversidad)
- Protección de **hardware + diversidad**
- Conmutación automática según tasa de error

#### **2×(1+0)**
- 2 RAUs por extremo
- 1 antena por extremo
- **Sin protección**, duplica capacidad

#### **MIMO 2×2**
- Multiplexación espacial para **duplicar capacidad**
- Separación óptima de antenas (función de distancia y frecuencia)
- Soportado por RAUs 6363, 6364, 6365

### 💻 **Placas Moduladoras MMU**

| Placa | Modulación Máxima | Anchos de Banda | Notas |
|-------|------------------|-----------------|-------|
| MMU2H | 512 QAM | 28, 40, 56 MHz | XPIC, modulación adaptativa |
| MMU3A | 1024 QAM | 28, 40, 56 MHz | XPIC, modulación adaptativa |
| MMU4A | 4096 QAM | **80, 112 MHz** | Compatible con 6600 |
| MMU 1001/1002 | **4096 QAM** | **80, 112 MHz** | Familia 6600 |

### 📡 **Potencias de Transmisión (PTx)**
- **RAUs Alta Potencia**: PTx ≤ 30 dBm
- **RAUs Potencia Media**: PTx ≤ 26 dBm
- Depende de la modulación utilizada

### 🎚️ **Modulación Adaptativa**
- **Concepto**: Varía modulación según condiciones del enlace
- **Ejemplo**: 128 QAM (mínima) ↔ 4096 QAM (máxima)
- **Ventaja**: Garantiza tráfico prioritario en modulación baja, escala capacidad cuando propagación es buena
- Ideal para tráfico con diferentes prioridades

### 🚀 **Tecnologías Avanzadas**

#### **Multi-band Booster**
- Combina 2 radioenlaces en bandas diferentes
- Banda baja: tráfico prioritario (mayor confiabilidad)
- Banda alta: mayor capacidad (variable según propagación)

#### **Carrier Aggregation**
- Suma ancho de banda de múltiples carriers
- Soportado por RAUs 6364, 6365

#### **Radio Link Bonding (hRLB)**
- Transporte de tramas Ethernet sobre múltiples links paralelos
- Aumenta capacidad agregada

### 📊 **Capacidades de Tráfico**

**Con XPIC se puede duplicar aproximadamente la capacidad**

Ejemplos con MMU 1002 (112 MHz):
- 128 QAM: ~400 Mbps
- 1024 QAM: ~1.6 Gbps
- **4096 QAM: ~2.4 Gbps**

---

## 3. Manual Introducción Redes TCP/IP

### 🌐 **Modelos de Capas**

#### **Modelo OSI (7 capas)** vs **Modelo Híbrido TCP/IP (5 capas)**

| OSI | TCP/IP Híbrido | Función |
|-----|---------------|---------|
| Aplicación | Aplicación | Servicios al usuario (HTTP, FTP, DNS) |
| Presentación | — | Formato de datos |
| Sesión | — | Gestión de sesiones |
| Transporte | Transporte | Control de flujo (TCP, UDP) |
| Red | Red | Direccionamiento y routing (IP) |
| Enlace | Enlace | Control de acceso al medio (Ethernet) |
| Física | Física | Transmisión de bits |

### 🔌 **Capa Física**

#### **Cables UTP (Par Trenzado No Apantallado)**
- **Más utilizados en redes LAN**
- **Categorías principales**:
  - Cat 5e: 1 Gbps
  - Cat 6: 10 Gbps (hasta 55m)
  - Cat 6A: 10 Gbps (hasta 100m)

#### **Conectores**
- **RJ-45**: Estándar para Ethernet
  - Pines 1-2: Transmisión (Tx)
  - Pines 3-6: Recepción (Rx)
- **Cable Cruzado**: Para conectar PC-PC o Hub-Hub
- **Cable Directo**: Para conectar PC-Switch

#### **Fibra Óptica**
- **Monomodo (SM)**: Largas distancias (>100 km, >50 Gbps)
- **Multimodo (MM)**: Distancias cortas (hasta pocos km)
- **Conectores comunes**: ST, SC, LC

### 🔗 **Capa de Enlace - Ethernet**

#### **Dirección MAC**
- **Longitud**: 48 bits (6 bytes)
- **Formato**: XX:XX:XX:XX:XX:XX
- **OUI**: Primeros 3 bytes = fabricante
- **Broadcast**: FF:FF:FF:FF:FF:FF

#### **Dispositivos**
- **Hub**: Capa 1, repite señal a todos los puertos, topología lógica de **bus**
- **Switch**: Capa 2, aprende MACs, reenvío selectivo, segmenta **dominios de colisión**
- **Router**: Capa 3, enruta entre redes, detiene **broadcasts**

#### **Protocolo CSMA/CD**
- **Carrier Sense Multiple Access with Collision Detection**
- Escucha el medio antes de transmitir
- Detecta colisiones y reenvía tras espera aleatoria

#### **Trama Ethernet**
- **Tamaño mínimo**: 64 bytes
- **Tamaño máximo**: 1518 bytes
- **Campo de datos**: hasta 1500 bytes (MTU)
- **Estructura**:
  - Preámbulo (7 bytes) + SFD (1 byte)
  - MAC destino (6 bytes)
  - MAC origen (6 bytes)
  - Tipo/Longitud (2 bytes)
  - Datos (46-1500 bytes)
  - FCS/CRC (4 bytes)

### 🌍 **Capa de Red - IP**

#### **Direccionamiento IPv4**
- **Longitud**: 32 bits (4 bytes)
- **Formato**: XXX.XXX.XXX.XXX (0-255)
- **Notación CIDR**: /XX (número de bits de red)

**Máscaras comunes:**
- /8 = 255.0.0.0
- /16 = 255.255.0.0
- /24 = 255.255.255.0

**Red 192.168.10.0/24:**
- Dirección de red: 192.168.10.0
- Broadcast: 192.168.10.255
- IPs utilizables: 192.168.10.1 - 192.168.10.254 (**254 IPs**)

#### **Direcciones Privadas (RFC 1918)**
- Clase A: 10.0.0.0/8
- Clase B: 172.16.0.0/12
- Clase C: 192.168.0.0/16

#### **Protocolos de Soporte**
- **ARP**: Resuelve IP → MAC
- **ICMP**: Mensajes de error y control (ping, traceroute)
- **NAT**: Traduce IPs privadas ↔ públicas

#### **Protocolos de Routing**

**RIP (Distance Vector)**
- Métrica: número de saltos
- Máximo: 15 saltos
- Simple pero limitado

**OSPF (Link State)**
- Métrica: costo (basado en ancho de banda)
- Escalable, convergencia rápida
- Divide red en áreas
- Tipos de routers: ABR, ASBR, Internal

### 🚚 **Capa de Transporte**

#### **TCP (Transmission Control Protocol)**
- **Orientado a conexión** (3-way handshake)
- **Confiable**: ACKs, retransmisión
- **Control de flujo**: Ventana deslizante
- **Segmentación**: Divide datos en segmentos
- Ideal para: HTTP, FTP, Email

#### **UDP (User Datagram Protocol)**
- **No orientado a conexión**
- **No confiable**: Sin ACKs
- **Bajo overhead**: Más rápido
- Ideal para: DNS, VoIP, streaming

#### **Puertos**
- **Rango**: 0-65535
- **Conocidos (0-1023)**:
  - HTTP: 80
  - HTTPS: 443
  - FTP: 21
  - DNS: 53
  - TELNET: 23

### 📱 **Capa de Aplicación**

- **HTTP**: Transferencia de hipertexto (Web)
- **FTP**: Transferencia de archivos
- **DNS**: Resolución de nombres
- **TELNET**: Acceso remoto (texto plano)

#### **DNS**
- **Consulta recursiva**: Servidor resuelve completamente
- **Consulta no recursiva**: Servidor devuelve referencia
- Jerarquía de dominios: raíz → TLD → dominios

---

# MATERIAL ESTUDIO IP

## 4. BERT Manual

### 🎯 **Conceptos Fundamentales**

#### **BER (Bit Error Rate)**
- **Definición**: Bits erróneos / Bits totales transmitidos
- **BER aceptable en telecomunicaciones**: 10⁻⁹
- **BER apropiado para datos**: 10⁻¹³
- Indicador de integridad de señales de telecomunicaciones

#### **BERT (Bit Error Rate Testing)**
- **Propósito**: Medir BER en redes de fibra, Ethernet, etc.
- **Método**: Enviar flujo de datos predefinido, analizar salida
- **PRBS**: Secuencia Binaria Pseudoaleatoria
  - Crea patrones variados para inducir errores
  - Acelera pruebas (solo en líneas fuera de servicio)

### 📊 **Métricas de Rendimiento (KPIs)**

#### **1. Pérdida de Paquetes (PER - Packet Error Rate)**
- Relación de paquetes que no llegan a destino
- **Causas**:
  - Congestión de red
  - Sobreutilización de dispositivos
  - Problemas de hardware
  - Ataques DOS (posible indicador)

#### **2. Latencia**
- **Definición**: Tiempo de transmisión de datos entre ubicaciones
- **Impacto**: Latencia alta → cuellos de botella → calidad deficiente VoIP
- **Factores**:
  - Longitud de fibra
  - Retrasos en almacenamiento
  - Errores de switches/routers

#### **3. Fluctuación (Jitter)**
- **Definición**: Variación en el retraso de recepción de paquetes
- **Impacto crítico**: Transmisiones de voz y vídeo
- Jitter excesivo → pérdidas de señal acústica, vídeo pixelado
- DSP (Procesador de Señales Digitales) debe compensar

### 🔍 **Importancia de las BERT**

#### **Para Redes Internas**
- Garantiza operaciones eficaces
- Especialmente importante en circuitos de gran tamaño
- Visibilidad del rendimiento del sistema

#### **Para Clientes**
- Certificación de redes de alta velocidad
- Mejora satisfacción del cliente
- Garantía de rendimiento desde el primer día

#### **En Redes de Fibra Óptica**
- Rutinas de Ethernet pueden **enmascarar problemas físicos**
- Paquetes retransmitidos **merman rendimiento**
- Contribuyen a **congestión inadvertida**
- **Causas de errores**: atenuación, dispersión, otros factores

### ⚠️ **Consideraciones Importantes**

**Las BERT son vitales porque:**
1. La demanda de ancho de banda y rendimiento crece constantemente
2. Permiten medir BER en canales de fibra óptica
3. Generan confianza en activación de servicios de alta velocidad
4. Evitan problemas antes de la activación

**Consecuencias de omitir BERT:**
- Falta de visibilidad del rendimiento
- Oportunidades perdidas de correcciones
- Problemas no detectados durante activación

### 📋 **Metodología de Pruebas**

1. **Configurar flujo de datos** (puede usar PRBS)
2. **Transmitir por período determinado**
3. **Analizar salida** en extremo receptor
4. **Calcular BER**: Errores/Total de bits
5. **Evaluar KPIs**: Pérdida, latencia, jitter
6. **Documentar resultados**

### ✅ **Recomendaciones**

- Realizar BERT en **activación de servicios**
- Verificar rendimiento de red propia
- Certificar funcionamiento de nuevas redes
- Medir tanto en **redes internas como externas**
- Considerar BERT parte esencial del proceso de calidad

---

## 5. RFC 2544 Manual

### 📖 **Contexto del Estándar**

#### **Origen y Alcance**
- **Desarrollado**: IETF, 1999
- **Nombre**: "Benchmarking Methodology for Network Interconnect Devices"
- **Diseño original**: Evaluación de equipos en **laboratorio**
- **Uso actual**: Extendido a validaciones de campo y pruebas de aceptación
- **Enfoque**: Capa 2/3 del modelo OSI

#### **Limitación Principal**
- Centrado en **flujo único**
- **NO contempla** escenarios multiservicio nativamente
- Para multiservicio → **ITU-T Y.1564** es más adecuado

### 📏 **Métricas Clave del RFC 2544**

#### **1. Throughput**
- **Definición**: Tasa máxima de transferencia **sin pérdida** de tramas
- **Método**: Búsqueda binaria de carga por cada tamaño de trama
- **Criterio típico**: ≥ 99% de line rate a MTU estándar

#### **2. Latencia**
- **RTT** (Round Trip Time): Si no hay sincronización
- **One-way**: Con sincronización GPS/PTP
- Aumenta con tamaño de trama y carga
- **Criterio típico**:
  - 1G: ≤ 1 ms
  - 10G: ≤ 300 µs

#### **3. Pérdida de Tramas (Frame Loss)**
- Porcentaje de tramas no recibidas
- Caracteriza buffers y colas
- **Criterio típico**: ≤ 0.01% hasta 90% de carga

#### **4. Back-to-Back (Ráfagas)**
- Capacidad de procesar ráfagas sucesivas sin pérdida
- Evalúa buffers y mecanismos de control de congestión
- **Criterio**: Sin pérdida hasta N tramas (definir por plataforma)

#### **5. System Reset**
- Tiempo de recuperación tras reinicio/failover
- Incluye estabilidad de plano de control
- **Criterio típico**: < 60 s

#### **6. Responsividad (Response Time)**
- Tiempo para aplicar cambios de configuración
- Medir bajo distintas cargas

### 🔧 **Tamaños de Trama Estandarizados**

**Obligatorios**: 64, 128, 256, 512, 1024, 1280, 1518 bytes
**Opcional**: 9000 bytes (Jumbo Frames - NO parte oficial de RFC 2544)

### 🏗️ **Arquitectura de Prueba**

#### **Componentes Típicos**
- **Tester**: Generador/analizador (IXIA, Spirent, Viavi)
- **DUT**: Device Under Test
- **Cables y ópticas** adecuadas
- **Sincronización**: GPS/PTP (para latencia one-way)
- **Entorno** que minimice pérdidas ajenas

#### **Verificaciones de Cableado**
- Modos: breakout, autonegociación, FEC
- Transceptores compatibles
- Parámetros de interfaz: MTU, VLAN, pausas

### 📋 **Preparación Metodológica**

1. **Definir alcance** y criterios de aceptación
2. **Seleccionar tamaños** de trama y cargas objetivo
3. **Establecer duración** por punto (ej: 60s) y repeticiones
4. **Documentar configuraciones**: versiones, QoS, policing/shaping
5. **Asegurar condiciones constantes** entre corridas

### ⚙️ **Consideraciones de Configuración**

- **MTU/Jumbo**: Alinear entre tester y DUT
- **VLAN/EVPN/MPLS**: Etiquetado correcto
- **QoS**: Colas, scheduling, WRED, policers, shapers
- **PFC/PAUSE**: Cuidado con propagación de congestión
- **Rutas estáticas/VRF**: Verificar ARP/ND y next-hops
- **Seguridad**: ACLs/CoPP pueden afectar resultados

### 🔄 **Procedimiento Paso a Paso**

1. Configurar interfaces (speed/duplex, MTU, VLAN/L3)
2. **Verificar conectividad** (ARP/ND, ping)
3. **Resetear contadores** a cero
4. Ejecutar **Throughput** (búsqueda binaria por tamaño)
5. Medir **latencia** a diferentes cargas (25/50/75/100%)
6. Realizar **pérdida vs carga** (rampa 10→100%)
7. Ejecutar **Back-to-Back** con ráfagas crecientes
8. (Opcional) **Reset** y **responsividad**
9. **Exportar resultados** y generar informe

### ⚠️ **Buenas Prácticas**

✅ **HACER:**
- Llevar DUT a estado de régimen
- Asegurar estabilidad de reloj y temperatura
- Registrar versiones de software/firmware
- Usar puertos dedicados
- Automatizar recolección de KPIs
- Validar con repeticiones y controles

❌ **EVITAR:**
- Probar carga bidireccional sin aclarar
- Ignorar impacto de tamaño de trama
- No resetear contadores entre corridas
- Tomar valores "pico" únicos sin estadísticas
- Desalinear QoS/encapsulados

### 📊 **Comparación RFC 2544 vs ITU-T Y.1564**

| Aspecto | RFC 2544 | ITU-T Y.1564 |
|---------|---------|--------------|
| **Servicios** | Flujo único | Multiservicio simultáneo |
| **SLA** | No | Sí (CIR/EIR por clase) |
| **KPIs** | Básicos | Por flujo (latencia, jitter, pérdida) |
| **Uso** | Laboratorio, campo básico | Activación de servicios |
| **Rampa** | No nativo | Sí (prueba de rampa) |

### 📈 **Criterios de Aceptación Típicos**

- **Throughput**: ≥ 99% de line rate sin pérdida
- **Latencia RTT**:
  - 1G: ≤ 1 ms
  - 10G: ≤ 300 µs
- **Pérdida**: ≤ 0.01% hasta 90% carga
- **Back-to-Back**: Sin pérdida hasta N tramas
- **Reset**: Recuperación < 60s

### 🗂️ **Plantilla de Plan de Pruebas**

1. Objetivo y alcance
2. Topología y equipamiento
3. Matriz de casos (tamaños, cargas, duración, repeticiones)
4. Procedimiento paso a paso
5. KPIs a recolectar
6. Criterios de aceptación
7. Gestión de riesgos y retrocesos
8. Evidencia (capturas, logs, archivos)

---

## 6. Módulo 1 - Tipos de Fibras Ópticas

### 🔬 **Clasificación Principal**

#### **Fibras Monomodo (SM - Single Mode)**
- **Núcleo**: 8-10 μm
- **Cladding**: 125 μm
- **Buffer primario**: 250 μm
- **Color cubierta**: Amarillo o Azul
- **Uso**: Largas distancias

#### **Fibras Multimodo (MM - Multi Mode)**
- **Núcleo**: 50-62.5 μm
- **Cladding**: 125 μm
- **Buffer primario**: 250 μm
- **Color cubierta**: Naranja
- **Uso**: Distancias cortas (hasta pocos km)

### 🏗️ **Estructura de la Fibra Óptica**

De dentro hacia fuera:
1. **Core (Núcleo)**: Transporta la luz
2. **Cladding (Revestimiento)**: Vidrio con índice de refracción menor
3. **Buffer (Recubrimiento Primario)**: 250 μm, protección primaria
4. **Protección Secundaria**: Ajustada u holgada
5. **Elemento de tracción**: Kevlar
6. **Cubierta externa**: Protección mecánica

### 🛡️ **Protecciones Secundarias**

#### **Estructura Holgada (Loose)**
- **Fibras sueltas** dentro de tubos con gel
- **Gel anticongelante**: No se escurre fácilmente
- Protege contra efectos mecánicos y temperatura
- Uso común en **exterior**

**Componentes típicos:**
1. Elemento central de soporte
2. Fibras con recubrimiento de 250 μm
3. Tubos de plástico con gel
4. Cinta protectora contra humedad
5. Cubierta interna + hilo de rasgado
6. Kevlar (protección mecánica)
7. Cubierta externa + hilo de rasgado

#### **Estructura Ajustada (Tight)**
- **Fibra adherida** al tubo protector
- **Tubo**: 2-3 mm de diámetro
- **Protección 900 μm** sobre buffer 250 μm
- **Cable para exterior**: 8-36 fibras
- Se recomienda en **ducto**

**Características:**
- Cubierta resistente a intemperie
- Protección contra roedores
- Menor tamaño que estructura holgada

### ⚡ **Principio de Funcionamiento**

**Reflexión Total Interna:**
- Dos capas de vidrio con **índices de refracción distintos**
- Núcleo con índice mayor que cladding
- La luz queda **atrapada** en el núcleo
- Viaja por reflexiones sucesivas (MM) o línea recta (SM)

### 🔍 **Diferencias Fundamentales SM vs MM**

| Característica | Monomodo (SM) | Multimodo (MM) |
|----------------|--------------|----------------|
| **Núcleo** | 8-10 μm | 50-62.5 μm |
| **Color** | Amarillo/Azul | Naranja |
| **Distancia** | Largas (>100 km) | Cortas (≤ pocos km) |
| **Aplicación** | WAN, Metro, Long Haul | LAN, Datacenter |
| **Velocidad** | >50 Gbps | Variable |

### 🔌 **Conectores de Fibra Óptica**

**Más utilizados:**
- **ST** (Straight Tip): Bayoneta
- **SC** (Subscriber Connector): Push-pull
- **LC** (Lucent Connector): Pequeño, push-pull

### ⚠️ **Consideraciones Prácticas**

**Manipulación del Gel:**
- Es anticongelante
- No se escurre fácilmente
- Requiere cuidado al retirar
- Protege fibras contra temperatura

**Selección de Cable:**
- **Exterior**: Considerar protección contra roedores, intemperie
- **Ducto**: Preferible para cables ajustados
- **Número de fibras**: Según necesidad (8-36 típico en ajustados)

---

## 7. Transceptores Ópticos

### 🔌 **Definición y Función**

#### **¿Qué es un Transceptor Óptico?**
- Dispositivo que **convierte señales eléctricas ↔ ópticas**
- Combina **transmisor (Tx) + receptor (Rx)**
- Opera en **Capa 1 (Física)** del modelo OSI
- Función: **Conversión fotoeléctrica**

#### **Aplicaciones Críticas**
- Centros de datos
- Redes troncales ISP
- Sistemas de transporte óptico
- Enlaces de larga distancia
- Requiere: rendimiento sostenido, baja latencia, alta confiabilidad

### 🧩 **Componentes Básicos**

1. **Láser o LED (Tx)**: Genera señal óptica
2. **Fotodiodo (Rx)**: Detecta señal óptica entrante
3. **Circuito de control**: Regula potencia, temperatura, conversión
4. **Conector óptico**: LC, SC, MPO para conexión de fibra
5. **EEPROM**: Almacena info de fabricante, modelo, configuración

### 📊 **Clasificaciones**

#### **Por Tipo de Fibra**
- **SMF (Single Mode Fiber)**: Largas distancias
- **MMF (Multi Mode Fiber)**: Distancias cortas (hasta 5 km)

#### **Por Formato**
- **SFP** (Small Form-Factor Pluggable): Versátil
- **SFP+**: Velocidades mayores que SFP
- **SFP28**: Para mayores velocidades
- **QSFP** (Quad SFP): 40G, 100G
- **QSFP28**: Versión mejorada de QSFP

#### **Por Alcance**
- **SR** (Short Reach): Corto alcance
- **LR** (Long Reach): Hasta 10 km
- **ER** (Extended Reach): Hasta 40 km
- **ZR** (ZR Reach): 80 km o más

#### **Por Velocidad**
- 100 Base
- 1000 Base (1G)
- 10G
- 40G
- 100G

### 💡 **Presupuesto Óptico (Power Budget)**

#### **Concepto Fundamental**
- **Definición**: Cantidad de luz necesaria para transmisión exitosa
- **Fórmula**: Power Budget = Tx mínimo - Rx sensibilidad mínima

#### **Componentes del Cálculo**

**1. Datos del Módulo:**
- Potencia de emisión mínima (**Tx mínimo**) en dBm
- Sensibilidad del receptor (**Rx mínimo**) en dBm

**2. Pérdidas del Enlace:**
- **Atenuación de fibra**: 0.22 - 0.5 dB/km (típico)
  - Ejemplo: 20 km × 0.3 dB/km = **6 dB**
- **Empalmes**: ~0.1 dB cada uno
  - Ejemplo: 4 empalmes = **0.4 dB**
- **Conectores**: ~0.75 dB cada uno (estándar TIA)
  - Ejemplo: 6 conectores = **4.5 dB**
- **Margen de seguridad**: **1.7 - 3 dB**

#### **Ejemplo de Cálculo**

**Datos:**
- Tx mínimo = -5 dBm
- Rx sensibilidad = -28 dBm
- Distancia = 20 km
- Fibra = 0.3 dB/km
- Empalmes = 4 × 0.1 dB
- Conectores = 6 × 0.75 dB

**Cálculo:**
1. Power Budget = -5 - (-28) = **23 dB**
2. Pérdida fibra = 20 × 0.3 = **6 dB**
3. Pérdida empalmes = 4 × 0.1 = **0.4 dB**
4. Pérdida conectores = 6 × 0.75 = **4.5 dB**
5. Pérdidas totales = 6 + 0.4 + 4.5 = **10.9 dB**
6. Margen = 23 - 10.9 = **12.1 dB**
7. Margen de seguridad objetivo = **2 dB**
8. **Margen real = 12.1 - 2 = 10.1 dB ✓ VIABLE**

### ✅ **Criterio de Viabilidad**

**Para que el enlace funcione:**
```
Power Budget ≥ Pérdidas totales del enlace
```

**Power Margin (Margen de Potencia):**
```
Power Margin = Power Budget - Pérdidas totales
```

- **Margen positivo y holgado**: ✓ Buena calidad
- **Margen negativo**: ✗ Enlace no funcionará

### 🔧 **Soluciones si Power Budget Insuficiente**

1. Usar módulo con **mayor potencia de salida (Tx)**
2. Usar módulo con **mejor sensibilidad (Rx)**
3. **Reducir pérdidas**:
   - Mejorar calidad de empalmes
   - Reducir número de conectores
   - Usar fibra de menor atenuación
4. **Agregar amplificación óptica**

### ⚠️ **Consideraciones de Uso**

- **Compatibilidad**: Tipo de transceptor debe coincidir con puerto
- **Temperatura**: Módulos industriales soportan rangos térmicos mayores
- **Limpieza**: Suciedad en conectores afecta severamente transmisión
- **Factores ambientales**: Temperatura extrema afecta potencia óptica

### 📝 **Información Almacenada (EEPROM)**

- Fabricante
- Modelo
- Número de serie
- Tipo de fibra soportado
- Alcance máximo
- Longitud de onda
- Potencia de transmisión
- Sensibilidad de recepción

### 🎯 **Pasos para Diseño de Enlace**

1. Obtener especificaciones del módulo (Tx, Rx)
2. Calcular Power Budget
3. Estimar pérdidas del enlace
4. Incluir margen de seguridad
5. Verificar: Power Budget ≥ Pérdidas totales
6. Calcular Power Margin
7. Si es inadecuado, ajustar componentes

---

## 📚 **Apéndices**

### **Fórmulas Importantes**

**Propagación Radio:**
- λ (cm) = 30/f (GHz)
- rF = 17.3√(d₁×d₂)/(f×d) [km]

**IP:**
- IPs utilizables = 2^(32-prefix) - 2
- Ejemplo /24: 2^8 - 2 = 254

**Óptica:**
- Power Budget = Tx mín - Rx sens
- Pérdida fibra = Atenuación × Distancia
- Power Margin = Budget - Pérdidas

### **Conversiones Útiles**

- 1 byte = 8 bits
- 1 Gbps = 1000 Mbps
- dBm: Potencia referenciada a 1 mW
- dB: Relación entre potencias

---

**FIN DE LOS RESÚMENES**

*Documento creado para estudio de Llamados Técnicos 2025 - Antel*
*Última actualización: Febrero 2026*
