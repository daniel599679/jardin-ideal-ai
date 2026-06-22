# AUTOMATIZACIONES — CAPTURA DE LEADS
**Flujos desde el primer clic hasta el registro en CRM**

---

## Principio General
Cada lead que entra debe, en menos de 5 minutos:
1. Estar registrado en el CRM
2. Haber generado una notificación al equipo
3. Haber recibido un mensaje automático de bienvenida

Sin automatización, estos 3 pasos dependen de que alguien esté mirando la pantalla. Con automatización, ocurren solos a las 3am.

---

## FLUJO A — Lead desde Meta Ads (Formulario instantáneo)

```
DISPARADOR
└── Cliente completa formulario de Meta Lead Ads

PASOS AUTOMÁTICOS
├── 1. Meta envía datos del lead (nombre, tel, email, servicio)
│       ↓
├── 2. Make/Zapier recibe los datos
│       ↓
├── 3. [PARALELO]
│   ├── 3a. Crea registro en CRM (etapa: NUEVO)
│   ├── 3b. Envía notificación WhatsApp al equipo:
│   │       "🔔 NUEVO LEAD
│   │        Nombre: [Nombre]
│   │        Tel: [Teléfono]
│   │        Servicio: [Servicio]
│   │        Fuente: Meta Ads
│   │        Hora: [HH:MM]
│   │        → Contactar en <2h"
│   └── 3c. Envía mensaje automático al cliente (WhatsApp o SMS):
│           "Bonjour [Prénom] ! Merci pour votre intérêt.
│            Un membre de notre équipe vous contactera
│            sous peu. — Jardín Ideal 🌿"
│       ↓
└── 4. Si en 2h nadie marcó el lead como "Contactado"
        → Segunda notificación al equipo: "⚠️ LEAD SIN CONTACTAR [Nombre] — 2h"
```

**Herramientas:**
- Meta Lead Ads (formulario nativo) → Make.com o Zapier
- CRM destino: HubSpot Free / Pipedrive / Google Sheets
- Notificación: WhatsApp Business API o Twilio
- Mensaje auto al cliente: WhatsApp Business API o ManyChat

**Prioridad de implementación:** 🔴 Alta — es el flujo más crítico del negocio

---

## FLUJO B — Lead desde Google Ads (Formulario web)

```
DISPARADOR
└── Cliente completa formulario en el sitio web

PASOS AUTOMÁTICOS
├── 1. Formulario web (Gravity Forms / Typeform / formulario nativo) envía datos
│       ↓
├── 2. Make/Zapier recibe los datos
│       ↓
├── 3. [PARALELO]
│   ├── 3a. Crea registro en CRM (etapa: NUEVO, fuente: Google Ads)
│   ├── 3b. Notificación WhatsApp al equipo (mismo formato que Flujo A)
│   └── 3c. Email automático de confirmación al cliente:
│           Asunto: "Votre demande a bien été reçue — Jardín Ideal"
│           Cuerpo: (ver plantilla en 06_CRM/plantillas_mensajes.md)
│       ↓
└── 4. Alerta de seguimiento a las 2h si no hay contacto
```

**Herramientas:**
- Formulario web → Make.com o Zapier
- Email automático: Gmail / Mailchimp / SendGrid
- Notificación WhatsApp: igual que Flujo A

---

## FLUJO C — Lead desde DM de Instagram o Facebook

```
DISPARADOR
└── Cliente envía mensaje directo en Instagram o Facebook

PASOS AUTOMÁTICOS
├── 1. ManyChat o Meta Business Suite detecta el DM
│       ↓
├── 2. Respuesta automática inmediata:
│       "Bonjour ! Merci pour votre message. 🌿
│        Nous vous répondrons dans les plus brefs délais.
│        Pour une réponse plus rapide, vous pouvez aussi
│        nous appeler au [Número]."
│       ↓
├── 3. Notificación al equipo en WhatsApp:
│       "💬 NUEVO DM [Instagram/Facebook]
│        De: [Usuario]
│        Mensaje: [Primeras palabras del mensaje]
│        → Responder en <2h"
│       ↓
└── 4. Si el cliente responde al auto-mensaje → crear lead en CRM manualmente
    (DMs requieren calificación humana antes de entrar al CRM)
```

**Herramientas:**
- ManyChat (conecta Instagram/Facebook DMs con respuestas automáticas)
- Meta Business Suite (alternativa nativa, menos potente)
- Notificación: Zapier → WhatsApp

---

## FLUJO D — Lead por Llamada Telefónica

```
Este flujo no es automatizable en el primer contacto.
Requiere acción humana.

PROTOCOLO MANUAL:
├── 1. Recibir llamada, hacer calificación rápida
├── 2. Al terminar la llamada (máx. 5 min después):
│       → Crear lead en CRM manualmente
│       → Registrar fuente: "Llamada directa"
│       → Asignar próxima acción y fecha
└── 3. Si se instaló Google Call Tracking:
        → Las llamadas desde Google Ads se registran automáticamente
        → Make puede crear el lead en CRM desde Google Analytics
```

---

## Configuración Recomendada de Make.com

### Escenario básico (Meta Lead → CRM + WhatsApp):
```
[Meta Lead Ads]
      ↓
[Make: Trigger "Watch Lead Ads"]
      ↓
[Router] ──── [Google Sheets / HubSpot: Create Row/Contact]
         ├─── [WhatsApp Business: Send Message al equipo]
         └─── [WhatsApp Business: Send Message al cliente]
```

**Costo estimado Make.com:** Plan gratuito (1,000 operaciones/mes) suficiente para empezar. Plan Básico a 9 USD/mes para volumen mayor.

---

## Campos Mínimos a Capturar en el Formulario de Meta

```
Campo obligatorio:   Teléfono celular
Campo obligatorio:   Nombre completo
Campo recomendado:   Email
Campo recomendado:   Servicio de interés (lista desplegable)
Campo recomendado:   Ciudad (si la zona es amplia)
Campo opcional:      Mensaje libre / descripción del proyecto
```

> Regla: Cada campo extra reduce la tasa de conversión del formulario. Con nombre + teléfono + servicio es suficiente para arrancar.

---

## Registro de Automatizaciones Implementadas

```
FLUJO A — Meta Lead Ads
Estado: ⬜ No implementado | ⚙️ En desarrollo | ✅ Activo
Fecha implementación: ___________
Herramienta: ___________________
Notas: _________________________

FLUJO B — Google Ads / Web
Estado: ⬜ No implementado | ⚙️ En desarrollo | ✅ Activo
Fecha implementación: ___________
Herramienta: ___________________
Notas: _________________________

FLUJO C — DM Social
Estado: ⬜ No implementado | ⚙️ En desarrollo | ✅ Activo
Fecha implementación: ___________
Herramienta: ___________________
Notas: _________________________
```
