# AUTOMATIZACIONES — ALERTAS Y PIPELINE CRM
**Flujos para que ningún lead se pierda por silencio o inacción**

---

## Principio General
El CRM sin automatizaciones depende de que alguien recuerde revisar. Con automatizaciones, el sistema llama la atención cuando algo sale del camino correcto — sin que nadie tenga que estar vigilando.

---

## FLUJO 1 — Alerta: Lead sin contacto en 2 horas

```
DISPARADOR
└── Lead creado en CRM con etapa = NUEVO

CONDICIÓN
└── Han pasado 2 horas Y la etapa sigue siendo NUEVO

ACCIÓN
└── WhatsApp al equipo:
    "⚠️ LEAD SIN CONTACTAR (2h)
     Nombre: [Nombre]
     Tel: [Teléfono]
     Servicio: [Servicio]
     Entró: [Hora de entrada]
     → Contactar ahora"
```

**Herramienta:** CRM nativo (HubSpot Workflow / Pipedrive Automation) o Make.com con Google Sheets

---

## FLUJO 2 — Alerta crítica: Lead sin contacto en 24 horas

```
DISPARADOR
└── Lead en etapa NUEVO desde hace 24 horas

CONDICIÓN
└── Etapa no ha cambiado de NUEVO en 24h

ACCIÓN
├── WhatsApp urgente al equipo + a Daniel:
│   "🚨 ALERTA CRÍTICA — LEAD ABANDONADO 24h
│    Nombre: [Nombre] | Tel: [Teléfono]
│    Entró: [Fecha y hora]
│    → Contactar INMEDIATAMENTE"
└── Registrar en log de alertas
```

**Por qué es crítico:** Después de 24h, la tasa de conversión de un lead cae más del 50%. Esto es dinero perdido medible.

---

## FLUJO 3 — Alerta: Lead detenido más de 7 días

```
DISPARADOR
└── Cualquier lead en etapas CONTACTADO, CALIFICADO, o PROPUESTA ENVIADA

CONDICIÓN
└── La fecha del último cambio de etapa es hace >7 días

ACCIÓN
├── Notificación diaria (09:00 AM) al responsable:
│   "🟠 LEAD INACTIVO (7+ días)
│    Nombre: [Nombre]
│    Etapa actual: [Etapa]
│    Sin movimiento desde: [Fecha]
│    → Definir próxima acción hoy"
└── Aparecer en la vista "Leads que necesitan atención" del CRM
```

---

## FLUJO 4 — Recordatorio: Seguimiento de propuesta enviada

```
DISPARADOR
└── Lead cambia a etapa PROPUESTA ENVIADA

CONDICIÓN 1 — 7 días después sin cambio de etapa
└── ACCIÓN: Recordatorio al equipo:
    "📋 PROPUESTA SIN RESPUESTA (7 días)
     Cliente: [Nombre]
     Propuesta enviada el: [Fecha]
     Monto: [Valor] CAD
     → Hacer seguimiento hoy (plantilla 4.2 en 06_CRM)"

CONDICIÓN 2 — 14 días después sin cambio de etapa
└── ACCIÓN: Alerta de vencimiento próximo:
    "⏰ PROPUESTA VENCE EN 3 DÍAS
     Cliente: [Nombre]
     Válida hasta: [Fecha]
     → Contactar urgente o renovar la propuesta"

CONDICIÓN 3 — 17 días (propuesta vencida)
└── ACCIÓN: Notificación de decisión requerida:
    "❌ PROPUESTA VENCIDA — DECISIÓN REQUERIDA
     Cliente: [Nombre]
     → ¿Renovar propuesta? ¿Cerrar como perdido?"
```

---

## FLUJO 5 — Recordatorio automático de seguimiento programado

```
DISPARADOR
└── Se registra una fecha de "próximo seguimiento" en el CRM

CONDICIÓN
└── La fecha de seguimiento programado llega (día y hora)

ACCIÓN
└── Notificación WhatsApp:
    "📅 SEGUIMIENTO HOY
     Cliente: [Nombre]
     Etapa: [Etapa]
     Nota anterior: [Última nota del CRM]
     → Acción: [La que se registró]"
```

---

## FLUJO 6 — Trigger de reseña post-entrega

```
DISPARADOR
└── Lead cambia a etapa CERRADO GANADO

ESPERA
└── 48 horas

ACCIÓN
└── Recordatorio al equipo:
    "⭐ SOLICITAR RESEÑA
     Cliente: [Nombre]
     Proyecto: [Servicio]
     Entregado el: [Fecha]
     → Enviar plantilla 6.2 de 06_CRM/plantillas_mensajes.md"
```

> **Versión avanzada (si hay WhatsApp API):** enviar el mensaje de solicitud de reseña directamente al cliente de forma automática, sin intervención humana.

---

## FLUJO 7 — Reactivación de leads fríos (batch mensual)

```
DISPARADOR
└── Primer lunes de cada mes a las 08:00 AM

CONDICIÓN
└── Leads en estado LEAD FRÍO con fecha de última acción >30 días

ACCIÓN
└── Reporte automático a Daniel:
    "🔄 LEADS FRÍOS PARA REACTIVAR ESTE MES
     Total: [N] leads
     ─────────────────
     1. [Nombre] — frío desde [fecha] — servicio: [X]
     2. [Nombre] — frío desde [fecha] — servicio: [X]
     ...
     → Ver secuencia C en 06_CRM/secuencias_seguimiento.md"
```

---

## FLUJO 8 — Dashboard diario automático (09:00 AM)

```
DISPARADOR
└── Todos los días a las 08:55 AM (antes de la reunión)

ACCIÓN
└── Mensaje WhatsApp al equipo con estado del pipeline:
    "📊 PIPELINE HOY — [Fecha]
     
     NUEVO (sin contactar): [N]
     CONTACTADO: [N]
     CALIFICADO: [N]
     PROPUESTA ENV.: [N] (valor: [X] CAD)
     
     ⚠️ ALERTAS:
     • Sin contactar >2h: [N]
     • Detenidos >7 días: [N]
     • Propuestas >7 días: [N]"
```

**Esta automatización reemplaza parte de la preparación manual de la reunión de las 09:00.**

---

## Stack Técnico Recomendado

### Opción A — Make.com + Google Sheets (bajo costo, flexible)
```
CRM:           Google Sheets (hoja estructurada como pipeline)
Automatización: Make.com (escenarios)
Notificaciones: WhatsApp Business API (Twilio o 360Dialog)
Costo estimado: ~30–50 CAD/mes
Tiempo de setup: 4–8 horas
```

### Opción B — HubSpot Free (más potente, sin código)
```
CRM:           HubSpot CRM (gratuito)
Automatización: HubSpot Workflows (gratuito hasta cierto nivel)
Notificaciones: Email nativo + integración WhatsApp via Make
Costo estimado: 0–50 CAD/mes
Tiempo de setup: 2–4 horas
```

### Opción C — Pipedrive (CRM orientado a ventas)
```
CRM:           Pipedrive (~25 CAD/usuario/mes)
Automatización: Pipedrive Automations (nativo)
Notificaciones: Integración WhatsApp via Make
Costo estimado: ~50–80 CAD/mes
Tiempo de setup: 3–6 horas
```

**Recomendación para Jardín Ideal:** Empezar con **Make.com + Google Sheets** para validar el proceso. Migrar a HubSpot o Pipedrive cuando el volumen de leads justifique la inversión.

---

## Registro de Flujos Implementados

```
FLUJO 1 — Alerta 2h sin contacto
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 2 — Alerta crítica 24h
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 3 — Lead detenido 7 días
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 4 — Seguimiento propuesta
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 5 — Recordatorio seguimiento
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 6 — Trigger reseña post-entrega
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 7 — Reactivación leads fríos
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 8 — Dashboard diario 09:00
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___
```
