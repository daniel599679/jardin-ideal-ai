# SESIONES ESPECIALES DE MANUS
**Tareas no diarias: reportes, análisis, contenido en bloque, reactivaciones**

---

## SESIÓN E1 — REPORTE SEMANAL (cada lunes AM)
**Duración estimada: 20–30 minutos**

### Cuándo: Lunes entre 08:00 y 08:30 (antes de la reunión)

### Documentos a cargar:
- `08_REPORTES/reporte_semanal.md` (plantilla)
- Los 5 reportes diarios de la semana anterior
- Exportación semanal de Meta Ads y Google Ads

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Generar el reporte semanal de Jardín Ideal.

Semana del [fecha inicio] al [fecha fin].

Datos de los 5 días:
[Pegar o adjuntar los 5 reportes diarios]

Datos de campañas de la semana:
Meta Ads — Total gasto: [X CAD] | Total leads: [N] | CPL promedio: [X CAD]
Google Ads — Total gasto: [X CAD] | Total leads: [N] | CPL promedio: [X CAD]

Proyectos cerrados esta semana: [N] | Valor: [X CAD]
Proyectos entregados: [N]

Completar la plantilla del reporte semanal.
Incluir el análisis de qué funcionó, qué no funcionó, y el plan para la semana que inicia.
```

### Output esperado:
- Reporte semanal completo con todos los bloques llenos
- Análisis de tendencias vs. semana anterior
- Plan de prioridades para la semana nueva
- Listo para guardar como `reporte_semana_YYYY-WNN.md`

---

## SESIÓN E2 — REPORTE MENSUAL (primer lunes del mes)
**Duración estimada: 45–60 minutos**

### Documentos a cargar:
- `08_REPORTES/reporte_mensual.md` (plantilla)
- Los 4–5 reportes semanales del mes
- Exportaciones mensuales de Meta Ads y Google Ads
- Listado de proyectos cerrados del mes con montos

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Generar el reporte mensual de Jardín Ideal para [MES] 2026.

[Pegar los reportes semanales del mes]

Resumen del mes:
- Total leads: [N]
- Gasto total en publicidad: [X CAD]
- Proyectos cerrados: [N] | Facturación: [X CAD]
- Ticket promedio: [X CAD]

Objetivo mensual: [X CAD según la tabla de metricas_kpis.md]
Objetivo anual: 7,000,000 CAD
Acumulado año hasta este mes: [X CAD]

Completar la plantilla del reporte mensual completa.
Incluir el scorecard, el análisis estratégico y el plan del próximo mes.
Calcular si estamos en camino al objetivo anual de 7M CAD.
```

---

## SESIÓN E3 — BLOQUE DE CONTENIDO SEMANAL (cada miércoles 10:00)
**Duración estimada: 30–40 minutos**
**Produce: 5 publicaciones listas para programar la semana siguiente**

### Documentos a cargar:
- `05_MARKETING/contenido_organico.md`
- `05_MARKETING/guia_creatividades.md`
- Lista de fotos disponibles (describir qué fotos hay en el inventario)

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Crear el contenido orgánico para la semana del [fecha inicio] al [fecha fin].

Fotos disponibles esta semana:
1. [Descripción foto 1: tipo de proyecto, etapa (antes/durante/después), servicio, ciudad]
2. [Descripción foto 2]
3. [Descripción foto 3]
[listar todas las fotos disponibles]

Generar 5 publicaciones completas siguiendo el calendario semanal:
- Lunes: Antes/Después
- Martes: Consejo técnico
- Miércoles: Proyecto en proceso
- Jueves: Testimonio (usar esta reseña real: "[pegar reseña]")
- Viernes: Inspiración

Para cada publicación entregar:
- Tipo y plataforma
- Qué foto usar (de las disponibles)
- Texto completo en francés québécois
- Hashtags (10–14)
- CTA
```

### Output esperado:
- 5 publicaciones completas listas para copiar en Meta Business Suite
- Con opciones para ajustar si una foto no encaja con el texto sugerido

---

## SESIÓN E4 — ANÁLISIS DE CAMPAÑAS (cada lunes o cuando hay problema)
**Duración estimada: 20–30 minutos**
**Activar cuando el CPL supera el objetivo o hay anomalía notable**

### Documentos a cargar:
- `05_MARKETING/estrategia_campanas.md`
- `05_MARKETING/metricas_kpis.md`
- `05_MARKETING/guia_creatividades.md`
- Exportación de datos de Meta Ads (últimos 14–30 días)

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Análisis profundo de campañas de Meta Ads.

Período: [fecha inicio] al [fecha fin]

Datos por campaña:
[Pegar exportación o tabla con: campaña, presupuesto, gasto, alcance, impresiones, clics, CTR, leads, CPL, frecuencia]

Problema detectado (si hay uno específico):
[Describir el problema — ej: "El CPL subió de 65 a 140 CAD en los últimos 7 días"]

Analizar:
1. ¿Qué campaña tiene el mejor y peor rendimiento?
2. ¿Hay señales de agotamiento de audiencia (frecuencia alta)?
3. ¿El problema es de creatividad, audiencia, presupuesto o página de destino?
4. ¿Qué campañas pausar, escalar o modificar?

Entregar:
- Diagnóstico del problema principal con causa probable
- Plan de acción concreto con 3–5 cambios específicos
- Qué medir la semana siguiente para verificar mejora
```

---

## SESIÓN E5 — REACTIVACIÓN DE LEADS FRÍOS (mensual)
**Duración estimada: 20–25 minutos**
**Activar: primer lunes de cada mes, o cuando hay baja temporada**

### Documentos a cargar:
- `06_CRM/secuencias_seguimiento.md`
- `06_CRM/plantillas_mensajes.md`
- Lista de leads fríos del CRM (nombre, servicio, última interacción, fecha)

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Generar mensajes de reactivación para los leads fríos de este mes.

Mes actual: [MES] | Temporada: [Alta / Baja / Pre-temporada]

Leads fríos a reactivar:
[Pegar lista: Nombre | Servicio | Última interacción | Días inactivo | Notas]

Para cada lead:
1. Determinar si es candidato a reactivar (según criterios de secuencia C del CRM)
2. Seleccionar el mensaje correcto según el tiempo de inactividad y la temporada
3. Personalizar el mensaje con el nombre y el servicio de interés
4. Indicar el canal recomendado (WhatsApp o llamada)

Entregar lista ordenada por prioridad de reactivación + mensajes listos.
Todos los mensajes en francés québécois.
```

---

## SESIÓN E6 — PREPARACIÓN DE VISITA TÉCNICA
**Duración estimada: 10 minutos**
**Activar: la tarde antes de una visita importante**

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Preparar la visita técnica de mañana.

Cliente: [Nombre]
Dirección: [Dirección]
Servicio solicitado: [Descripción del proyecto]
Notas del CRM: [Pegar notas de las conversaciones previas]
Presupuesto aproximado del cliente: [Si lo mencionó]
Fecha deseada del proyecto: [Si la mencionó]

Preparar:
1. Preguntas clave a hacer durante la visita
2. Puntos técnicos a verificar en sitio (según el tipo de servicio)
3. Materiales de referencia a llevar (fotos de proyectos similares)
4. Rango de precio aproximado a tener en mente
5. Posibles objeciones y cómo responderlas

Entregar: briefing de visita de una página, listo para imprimir o leer antes de salir.
```

---

## SESIÓN E7 — INVESTIGACIÓN DE COMPETIDORES (trimestral)
**Duración estimada: 30–45 minutos**
**Activar: inicio de temporada (marzo) y mitad de temporada (julio)**

### Prompt:
```
[BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Análisis competitivo de empresas de aménagement paysager en Montreal.

Buscar y analizar los 5 competidores principales de Jardín Ideal en el Gran Montreal.
Para cada uno investigar:
- Presencia en redes sociales (seguidores, frecuencia de publicación, tipo de contenido)
- Servicios que ofrecen vs. los que ofrece Jardín Ideal
- Posicionamiento de precio (si es visible)
- Reseñas de Google (calificación, cantidad, temas recurrentes)
- Campañas de publicidad visibles en Meta (si se pueden identificar)

Entregar:
1. Tabla comparativa de los 5 competidores
2. Oportunidades que Jardín Ideal no está aprovechando
3. Amenazas o competidores que están creciendo rápido
4. 3 recomendaciones concretas de diferenciación
```

---

## Calendario de Sesiones Especiales 2026

| Frecuencia | Sesión | Mes/Semana |
|---|---|---|
| Semanal (miércoles) | E3 — Bloque de contenido | Todas las semanas activas |
| Mensual (1er lunes) | E1 + E2 + E5 | Todos los meses |
| Por necesidad | E4 — Análisis campañas | Cuando CPL >objetivo |
| Por necesidad | E6 — Prep visita | Noche anterior a visita importante |
| Trimestral | E7 — Competidores | Marzo, julio, octubre |
