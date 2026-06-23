# PROTOCOLO DE CAPTURA DE IDEAS
**Cómo capturar ideas desde cualquier lugar y sincronizarlas al ecosistema**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Principio:** Una idea que no está capturada no existe. El proceso de captura debe ser tan fácil como hablar.

---

## LOS 4 CANALES DE CAPTURA

### CANAL 1 — VOZ (el más rápido, campo y desplazamiento)

```
CUÁNDO USAR:
  - En el auto camino al trabajo o de regreso
  - En obra cuando surge una observación
  - Cuando la idea viene mientras haces otra cosa

HERRAMIENTA: Notas de voz de WhatsApp → enviarse a uno mismo
  O: Siri/Google Assistant: "Recuérdame [idea]"
  O: Nota de voz de iPhone/Android

PROCESO:
  1. Grabar la nota de voz (máximo 2 minutos)
  2. Enviarla a la carpeta Drive: INBOX_IDEAS/ o al número propio en WhatsApp
  3. Al final del día (o a la mañana siguiente): transcribir y pegar en IDEA_INBOX.md

FORMATO DE TRANSCRIPCIÓN:
  "Idea de voz [fecha]: [transcripción literal o resumen fiel]"
  No mejorar ni filtrar — transcribir lo más cercano posible a lo hablado
```

---

### CANAL 2 — CLAUDE DESKTOP / CLAUDE WEB (casa y oficina)

```
CUÁNDO USAR:
  - Sesión de trabajo con un agente cuando surge una idea paralela
  - Revisión matutina cuando aparece algo nuevo

PROCESO:
  1. Durante la sesión, decirle a Claude: 
     "Antes de continuar, captura esta idea en IDEA_INBOX.md: [idea]"
  2. Claude agrega la idea con el formato correcto
  3. Al final de la sesión, Claude actualiza el DAILY_IDEA_REVIEW con las ideas capturadas

VENTAJA: Claude puede hacer la conexión inicial con los sistemas automáticamente
FORMATO: Claude usa la plantilla de IDEA_INBOX.md directamente
```

---

### CANAL 3 — CLAUDE CODE (en el sistema de archivos)

```
CUÁNDO USAR:
  - Mientras trabajas en el sistema de producción
  - Al revisar archivos y encontrar algo que mejorar

PROCESO:
  1. Dar la instrucción: "Agrega esta idea al IDEA_INBOX: [idea]"
  2. Claude Code edita IDEA_INBOX.md directamente (tiene acceso al filesystem)
  3. Si la idea es urgente: "Agrégala como P1 en IDEAS_PRIORIZADAS también"

VENTAJA: Acceso directo al sistema de archivos → cero fricción
```

---

### CANAL 4 — TEXTO / WHATSAPP (móvil, cualquier momento)

```
CUÁNDO USAR:
  - Idea en mitad de la noche
  - Conversación con cliente que genera insight
  - Reunión interna

PROCESO OPCIÓN A (tiempo real):
  1. Abrir Claude en el móvil
  2. Decir: "Captura esta idea: [idea]"
  3. Claude la formatea y la agrega al IDEA_INBOX

PROCESO OPCIÓN B (batch):
  1. Enviar la idea a uno mismo por WhatsApp con el prefijo "IDEA:"
  2. Ejemplo: "IDEA: hacer un reel de time-lapse de instalación completa de pavé-uni, 60 segundos"
  3. Al día siguiente, en la revisión matutina, procesar todas las ideas marcadas con "IDEA:"

BÚSQUEDA RÁPIDA EN WHATSAPP:
  - Abrir el chat con uno mismo o un grupo personal
  - Buscar "IDEA:" → aparecen todas las ideas pendientes
```

---

## EL FLUJO COMPLETO — DE CAPTURA A EJECUCIÓN

```
PASO 1: CAPTURAR (inmediato — segundos)
  Cualquier canal → idea bruta depositada en IDEA_INBOX.md o anotada en WhatsApp/voz

PASO 2: PROCESAR (diario — máximo 15 minutos)
  DAILY_IDEA_REVIEW.md → revisar el inbox y las notas de voz del día anterior
  → Transcribir voces
  → Agregar al IDEA_INBOX.md con la plantilla correcta

PASO 3: CLASIFICAR (semanal — máximo 30 minutos, lunes por la mañana)
  Revisar todo el IDEA_INBOX.md
  → Para cada idea nueva: identificar conexiones con los 6 sistemas
  → Clasificar: P1 / P2 / P3 / BACKLOG / DESCARTAR
  → Mover al nivel correspondiente en IDEAS_PRIORIZADAS.md

PASO 4: EJECUTAR (según prioridad)
  P1 → esta semana, en el sistema correspondiente
  P2 → este mes, asignar fecha y responsable
  P3 → agendar para el trimestre
```

---

## CONEXIÓN CON LOS 6 SISTEMAS — GUÍA DE CLASIFICACIÓN

### ¿Conecta con FLOAT?
```
SEÑALES:
  - Menciona fotografía, video, reel, música, composición visual
  - Menciona calidad de contenido, score visual, producción
  - Menciona un formato nuevo de contenido

ACCIÓN:
  → Verificar si ya existe un módulo en 05_MARKETING/FLOAT_V2_PREMIUM/
  → Si no existe: P2 (nuevo módulo FLOAT)
  → Si existe: P1 si mejora directamente el revenue de contenido
```

### ¿Conecta con Marketing?
```
SEÑALES:
  - Menciona Meta Ads, CTR, CPL, alcance, engagement
  - Menciona un ángulo de copy nuevo
  - Menciona una audiencia nueva o segmento no explorado
  - Menciona una campaña, boost, retargeting

ACCIÓN:
  → P1 si directamente genera más leads
  → P2 si mejora la infraestructura de marketing (calendario, templates)
  → Asignar al AGENTE_MARKETING para implementar
```

### ¿Conecta con Ventas?
```
SEÑALES:
  - Menciona calificación de leads, ICS, scripts, objeciones
  - Menciona el proceso de visita, cotización, cierre
  - Menciona comportamiento del cliente en el proceso de venta

ACCIÓN:
  → Siempre P1 — las ventas son el core del negocio
  → Actualizar JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md si es cambio al ICS
  → Compartir con el equipo de ventas en la próxima reunión
```

### ¿Conecta con Automatizaciones?
```
SEÑALES:
  - Menciona "automáticamente", "cuando pase X que pase Y"
  - Menciona Make.com, Zapier, notificaciones, webhooks
  - Menciona reducir trabajo manual repetitivo

ACCIÓN:
  → P1 si ahorra >2 horas/semana de trabajo manual
  → P2 si mejora la velocidad sin impacto directo en revenue
  → Documentar en 07_AUTOMATIZACIONES/ cuando se ejecute
```

### ¿Conecta con Cliente Ideal?
```
SEÑALES:
  - Menciona un tipo de cliente nuevo o diferente
  - Menciona objeciones recurrentes no documentadas
  - Menciona comportamiento de compra observado en campo

ACCIÓN:
  → P1 si cambia fundamentalmente el criterio de calificación
  → P2 si es un ajuste al ICS (nuevo script, nueva pregunta de calificación)
  → Actualizar JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md
```

### ¿Conecta con Operaciones?
```
SEÑALES:
  - Menciona el equipo de obra, logística, materiales, proveedores
  - Menciona eficiencia en campo, tiempo de instalación, incidencias
  - Menciona protocolos de fotografía o captura en sitio

ACCIÓN:
  → P1 si reduce costos o tiempo de instalación directamente
  → P2 si mejora la calidad del trabajo o la captura de material
  → Documentar en 09_CHECKLISTS/ cuando se ejecute
```

---

## REGLAS ANTI-DISPERSIÓN

```
REGLA 1 — La idea más brillante en el peor momento no se ejecuta
  Si surge una idea P1 en mitad de una sesión crítica, capturarla y TERMINAR lo que se está haciendo.
  La idea ya no se pierde. Terminar la tarea actual.

REGLA 2 — Máximo 3 ideas P1 simultáneas
  Si hay más de 3 P1, las adicionales esperan en P2 hasta que se complete alguna P1.
  Demasiadas prioridades = ninguna prioridad.

REGLA 3 — Una idea no es un proyecto hasta que tiene fecha y responsable
  Una idea en IDEAS_PRIORIZADAS sin fecha límite y sin responsable no es P1 — es un deseo.
  Asignar ambos o bajarla de nivel.

REGLA 4 — El inbox se procesa en menos de 15 minutos diarios
  Si el proceso de revisar el inbox toma más de 15 minutos, el inbox tiene demasiadas ideas sin procesar.
  Señal: hay que hacer una sesión de limpieza masiva (30-45 min una vez y dejar el sistema limpio).

REGLA 5 — Una idea descartada no es un fracaso
  Muchas ideas son buenas en abstracto pero no para este momento o este negocio.
  Descartar con razón documentada es una decisión inteligente, no una derrota.
```

---

*PROTOCOLO DE CAPTURA DE IDEAS v1.0 — Jardín Ideal*
*10_MEMORIA_EMPRESARIAL/CAPTURA_IDEAS/PROTOCOLO_CAPTURA_IDEAS.md*
