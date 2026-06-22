# AUTOMATIZACIONES — COMUNICACIÓN CON CLIENTES
**Mensajes automáticos, confirmaciones y secuencias sin intervención humana**

---

## Principio General
La comunicación automática no reemplaza al humano — lo libera de las tareas repetitivas y predecibles para que pueda enfocarse en las conversaciones que realmente importan (calificación, negociación, cierre).

---

## FLUJO 1 — Confirmación automática de visita técnica

```
DISPARADOR
└── Se agenda una visita técnica en el calendario / CRM

ACCIÓN INMEDIATA
└── WhatsApp automático al cliente:
    "Bonjour [Prénom] !
     
     Votre visite est confirmée :
     📅 [Jour] le [Date] à [Heure]
     📍 [Adresse]
     
     Notre technicien [Nombre] sera présent à l'heure convenue.
     Pour modifier ou annuler, contactez-nous au [Número].
     
     À bientôt ! — Jardín Ideal 🌿"

ACCIÓN 24H ANTES DE LA VISITA
└── WhatsApp recordatorio al cliente:
    "Bonjour [Prénom] !
     
     Rappel : votre visite est demain.
     📅 [Jour] à [Heure] | 📍 [Adresse]
     
     Des questions ? On est disponibles.
     [Nombre] | Jardín Ideal 📞 [Número]"

ACCIÓN INTERNA (notificación al equipo)
└── WhatsApp al responsable de la visita:
    "📍 VISITA MAÑANA
     Cliente: [Nombre] | Hora: [Hora]
     Dirección: [Dirección]
     Servicio a evaluar: [Servicio]
     Notas: [Notas del CRM]"
```

---

## FLUJO 2 — Secuencia de seguimiento post-visita

```
DISPARADOR
└── Lead cambia a etapa CALIFICADO (visita realizada)

DÍA 0 — mismo día (manual con trigger automático de recordatorio)
└── Recordatorio al equipo: "Enviar mensaje de agradecimiento post-visita
    (plantilla 3.3 de 06_CRM)"

DÍA 2 — si no se ha enviado la propuesta
└── Alerta interna: "⚠️ PROPUESTA PENDIENTE — [Nombre] — visita fue hace 2 días"

DÍA 4 — si no se ha enviado la propuesta
└── Alerta urgente: "🔴 PROPUESTA ATRASADA — [Nombre] — 4 días desde la visita
    → El cliente puede estar buscando otras opciones"
```

---

## FLUJO 3 — Secuencia automática después de enviar propuesta

```
DISPARADOR
└── Lead cambia a etapa PROPUESTA ENVIADA

HORA 0 — Inmediato
└── Email automático al cliente con la propuesta adjunta
    (el PDF lo adjunta el equipo manualmente, el email se dispara automático)

DÍA 1 — Verificación
└── Alerta interna: "¿Confirmaste que [Nombre] recibió la propuesta?"

DÍA 7 — Sin respuesta
└── WhatsApp automático al cliente:
    "Bonjour [Prénom],
     
     Je fais suite à la soumission envoyée le [Fecha].
     Avez-vous eu l'occasion d'en prendre connaissance ?
     
     Je reste disponible pour répondre à vos questions.
     [Nombre] | Jardín Ideal 📞 [Número]"

DÍA 14 — Propuesta por vencer
└── WhatsApp al cliente:
    "Bonjour [Prénom],
     
     Notre soumission du [Fecha] expire dans 3 jours.
     Si vous êtes toujours intéressé(e), contactez-nous
     pour confirmer la disponibilité de notre équipe.
     
     [Nombre] | Jardín Ideal"

DÍA 17 — Propuesta vencida
└── Alerta interna: "PROPUESTA VENCIDA — [Nombre] — Decidir: renovar o cerrar"
```

---

## FLUJO 4 — Notificación de inicio de proyecto

```
DISPARADOR
└── Proyecto marcado como "Inicio de obra" en Operaciones

ACCIÓN
└── WhatsApp automático al cliente:
    "Bonjour [Prénom] !
     
     Bonne nouvelle — votre projet commence demain ! 🎉
     
     Notre équipe sera sur place le [Fecha] à [Hora].
     N'hésitez pas à nous contacter si vous avez des questions.
     
     [Nombre] | Jardín Ideal 📞 [Número]"
```

---

## FLUJO 5 — Solicitud automática de reseña (48h post-entrega)

```
DISPARADOR
└── Proyecto marcado como "Entregado" en Operaciones

ESPERA
└── 48 horas

ACCIÓN — Versión A (recordatorio interno si no hay WhatsApp API)
└── Notificación al equipo:
    "⭐ SOLICITAR RESEÑA AHORA
     Cliente: [Nombre]
     Proyecto: [Servicio] en [Ciudad]
     Entregado: [Fecha]
     → Usar plantilla 6.2 de 06_CRM/plantillas_mensajes.md"

ACCIÓN — Versión B (si hay WhatsApp Business API)
└── WhatsApp directo al cliente:
    "Bonjour [Prénom] !
     
     J'espère que vous profitez de votre nouveau [espace] !
     
     Si vous êtes satisfait(e), votre avis Google nous aiderait
     énormément à aider d'autres familles :
     👉 [Link Google Reviews]
     
     Merci ! — [Nombre] | Jardín Ideal"
```

---

## FLUJO 6 — Reactivación estacional (batch automático)

```
DISPARADOR (programado)
└── 1 de marzo a las 08:00 AM (inicio de pre-temporada)
└── 1 de junio a las 08:00 AM (inicio de temporada alta)
└── 1 de septiembre a las 08:00 AM (cierre de temporada)

ACCIÓN
└── Make genera lista de leads fríos y clientes pasados
└── Reporte a Daniel con la lista + instrucción:
    "🔄 CAMPAÑA DE REACTIVACIÓN — [Mes]
     Leads fríos a reactivar: [N]
     Clientes pasados a contactar: [N]
     → Usar secuencias C y D de 06_CRM/secuencias_seguimiento.md"
```

---

## FLUJO 7 — Notificación de nueva reseña en Google

```
DISPARADOR
└── Nueva reseña aparece en Google Business Profile

CONDICIÓN A — Reseña positiva (4–5 estrellas)
└── Notificación WhatsApp al equipo:
    "⭐⭐⭐⭐⭐ NUEVA RESEÑA POSITIVA
     De: [Nombre del cliente]
     '[Extracto de la reseña]'
     → Responder en Google en <24h + compartir en redes"

CONDICIÓN B — Reseña negativa (1–3 estrellas)
└── Notificación urgente a Daniel:
    "🚨 RESEÑA NEGATIVA
     De: [Nombre]
     Calificación: [N]/5
     '[Extracto]'
     → Responder con calma en <4h | NO ignorar"
```

**Herramienta para detectar nuevas reseñas:** Google Alerts + Make o GrowthBar / ReviewTrackers.

---

## Herramientas Recomendadas por Flujo

| Flujo | Herramienta primaria | Alternativa | Costo |
|---|---|---|---|
| Mensajes WhatsApp automáticos | WhatsApp Business API (360Dialog) | Twilio | ~15–30 CAD/mes |
| Conexión Meta → CRM | Make.com | Zapier | 0–20 CAD/mes |
| Programación de mensajes | Make.com | HubSpot Workflows | incluido |
| Detección reseñas Google | Google Alerts gratuito | ReviewTrackers | 0 |
| Recordatorios de calendario | Google Calendar | Calendly | 0 |

**Costo total estimado del stack de comunicación:** ~50–80 CAD/mes para automatización completa.

---

## Reglas de Automatización de Comunicación

1. **Todo mensaje automático debe parecer humano** — sin "Este es un mensaje automático"
2. **Siempre incluir nombre del responsable real** al final del mensaje
3. **Nunca automatizar respuestas a objeciones o quejas** — esas deben ser humanas
4. **Registrar en CRM qué mensajes se enviaron automáticamente** — para que el equipo tenga contexto
5. **Revisar las automatizaciones cada mes** — los mensajes se desactualizan

---

## Registro de Flujos Implementados

```
FLUJO 1 — Confirmación de visita
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 2 — Seguimiento post-visita
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 3 — Secuencia post-propuesta
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 4 — Notificación inicio de proyecto
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 5 — Solicitud de reseña
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 6 — Reactivación estacional
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 7 — Alerta nueva reseña Google
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___
```
