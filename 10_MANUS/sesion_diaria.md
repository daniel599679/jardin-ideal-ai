# SESIÓN DIARIA DE MANUS
**Script completo del día — qué cargar, qué pedir, qué esperar**

> Este documento es el guion de operación diaria de Manus. Seguirlo garantiza que el sistema funcione sin depender de memoria o improvisación.

---

## SESIÓN 1 — OPERACIONES (07:00 AM)
**Duración estimada: 10–15 minutos**

### Documentos a cargar:
- `02_PROMPTS/prompt_agente_operaciones.md`
- `09_CHECKLISTS/checklist_apertura_diaria.md`
- Lista de proyectos activos (copiar desde el CRM o tabla propia)

### Prompt de activación:
```
[PEGAR BLOQUE DE CONTEXTO PERMANENTE de guia_manus.md]

Rol: AGENTE OPERACIONES

Fecha: [FECHA DE HOY]
Hora actual: [HORA]

Proyectos activos hoy:
[Pegar lista de proyectos: nombre, etapa, equipo asignado, bloqueos conocidos]

Visitas programadas hoy:
[Pegar lista de visitas: hora, cliente, dirección, propósito]

Materiales esperados hoy:
[Pegar lista si la hay]

Tarea: Ejecuta el rol de Agente Operaciones completo.
Genera las prioridades del día y la agenda lista para la reunión de 09:00 AM.
Formato: el definido en el prompt del agente.
```

### Output esperado:
- Lista de prioridades del día (máximo 5, ordenadas por urgencia)
- Agenda de reunión de 09:00 AM (15 minutos, 4 bloques)
- Alertas de proyectos si hay bloqueos
- Coordinación del equipo por ubicación

### Qué hacer con el output:
- Copiar la agenda en WhatsApp para el grupo del equipo antes de las 08:50
- Si hay alerta roja → atender antes de la reunión

---

## SESIÓN 2 — CRM (07:30 AM)
**Duración estimada: 15–20 minutos**

### Documentos a cargar:
- `02_PROMPTS/prompt_agente_crm.md`
- `06_CRM/pipeline.md`
- `06_CRM/plantillas_mensajes.md`
- `06_CRM/secuencias_seguimiento.md`
- Datos actuales del CRM (exportar o copiar manualmente)

### Prompt de activación:
```
[PEGAR BLOQUE DE CONTEXTO PERMANENTE]

Rol: AGENTE CRM

Fecha: [FECHA]
Hora: [HORA]

Estado actual del pipeline:
NUEVO (sin contactar): [N leads — listar nombre, tel, hora de entrada, fuente]
CONTACTADO: [N leads — listar nombre, última acción, días sin avance]
CALIFICADO: [N leads — listar nombre, visita programada o pendiente]
PROPUESTA ENVIADA: [N leads — listar nombre, fecha envío, monto]
CERRADO GANADO esta semana: [N — valor total]
CERRADO PERDIDO esta semana: [N — razón]

Alertas conocidas:
[Cualquier lead urgente que ya sepas]

Tarea: Ejecuta el rol de Agente CRM completo.
Entrega el reporte en el formato definido.
Para los seguimientos del día, genera los mensajes listos para copiar y enviar.
```

### Output esperado:
- Reporte CRM completo con tabla del pipeline
- Mensajes de seguimiento listos en francés (copiar/pegar directo a WhatsApp)
- Alertas marcadas con nivel de urgencia
- Indicadores del día

### Qué hacer con el output:
- Copiar los mensajes de seguimiento y enviarlos uno por uno (siempre revisar antes)
- Actualizar el CRM con los cambios de etapa que correspondan
- Llevar las alertas rojas a la reunión de 09:00

---

## SESIÓN 3 — MARKETING (08:00 AM)
**Duración estimada: 15–20 minutos**

### Documentos a cargar:
- `02_PROMPTS/prompt_agente_marketing.md`
- `05_MARKETING/metricas_kpis.md`
- `05_MARKETING/estrategia_campanas.md`
- Datos de Meta Ads del día anterior (capturas o exportación)
- Datos de Google Ads del día anterior (si aplica)

### Prompt de activación:
```
[PEGAR BLOQUE DE CONTEXTO PERMANENTE]

Rol: AGENTE MARKETING

Fecha: [FECHA]

Datos de campañas de ayer:
META ADS:
- Campaña [Nombre]: Gasto [X CAD] | Leads [N] | CPL [X CAD] | CTR [X%]
- Campaña [Nombre]: Gasto [X CAD] | Leads [N] | CPL [X CAD] | CTR [X%]
[repetir por cada campaña activa]

GOOGLE ADS:
- Campaña [Nombre]: Gasto [X CAD] | Leads [N] | CPL [X CAD] | CTR [X%]

Gasto total ayer: [X CAD] de [presupuesto diario] CAD
Leads totales ayer: [N]

Contenido publicado ayer: [descripción breve o "ninguno"]
DMs pendientes: [N]

Tarea: Ejecuta el rol de Agente Marketing completo.
Entrega el reporte con estado de campañas, problemas detectados y el contenido del día listo para publicar.
```

### Output esperado:
- Tabla de estado de campañas con semáforo
- Problemas detectados con soluciones priorizadas
- Publicación del día completa (texto + hashtags + CTA en francés)
- Indicadores de la semana si es lunes

### Qué hacer con el output:
- Revisar la publicación generada y ajustar si es necesario
- Programar la publicación en Meta Business Suite
- Aplicar las correcciones de campaña sugeridas si tienen sentido
- Llevar problemas críticos a la reunión de 09:00

---

## PREPARACIÓN REUNIÓN 09:00 AM
**No es sesión de Manus — es síntesis de las 3 sesiones anteriores**

Antes de la reunión tener a mano:
- Output de Sesión 1 (prioridades + agenda)
- Alertas del CRM (Sesión 2)
- Problemas de campañas (Sesión 3)

La agenda ya la generó Manus en la Sesión 1. Solo completarla con los datos de CRM y Marketing.

---

## SESIÓN 4 — REPORTE DIARIO (17:00)
**Duración estimada: 10–15 minutos**

### Documentos a cargar:
- `08_REPORTES/reporte_diario.md` (plantilla)
- Datos consolidados del día (leads, campañas, proyectos)

### Prompt de activación:
```
[PEGAR BLOQUE DE CONTEXTO PERMANENTE]

Tarea: Completar el reporte diario de Jardín Ideal.

Datos del día:
LEADS:
- Meta Ads: [N leads]
- Google Ads: [N leads]
- Orgánico/DM: [N leads]
- Referidos: [N leads]
- CPL del día: [X CAD]
- Gasto total: [X CAD]

CRM:
- Leads contactados hoy: [N]
- Contactados en <2h: [N]
- Seguimientos realizados: [N]
- Leads que avanzaron de etapa: [N]
- Cerrados ganados: [N] (valor: [X CAD])

CAMPAÑAS:
- Gasto Meta: [X CAD] / [presupuesto] CAD
- CTR Meta: [X%]
- Problema detectado: [si hay alguno]

OPERACIONES:
- Proyectos con avance: [N]
- Proyectos con bloqueo: [descripción si hay]
- Fotografías tomadas: [N]

CONTENIDO:
- Publicaciones realizadas: [N]
- DMs respondidos: [N]

Completar la plantilla del reporte diario con estos datos.
Incluir el semáforo del día y las 3 prioridades para mañana.
```

### Output esperado:
- Reporte diario completo en el formato de la plantilla
- Listo para copiar al archivo `reporte_YYYY-MM-DD.md` y compartir por WhatsApp

### Qué hacer con el output:
- Revisar rápidamente que los números cuadren
- Guardar como `reporte_YYYY-MM-DD.md` en `08_REPORTES/`
- Compartir en el grupo de WhatsApp del equipo

---

## Registro Diario de Sesiones

```
FECHA: _______________

Sesión 1 Operaciones:  ✅ / ⏭️ Omitida  |  Duración: ___  |  Alertas: ___
Sesión 2 CRM:          ✅ / ⏭️ Omitida  |  Duración: ___  |  Leads:   ___
Sesión 3 Marketing:    ✅ / ⏭️ Omitida  |  Duración: ___  |  CPL:     ___
Sesión 4 Reporte:      ✅ / ⏭️ Omitida  |  Duración: ___

Total tiempo con Manus: ___ minutos
Acciones ejecutadas desde outputs de Manus: ___
```
