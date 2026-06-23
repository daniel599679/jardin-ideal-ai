# ALEX — AGENTE DE LANDING PAGE
**Jardín Ideal | Documentación de contexto y hoja de ruta**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Estado actual:** FASE 2 EN IMPLEMENTACIÓN — decisiones estratégicas aprobadas 2026-06-23

---

## REGLA FUNDAMENTAL DE LECTURA

```
⚠️ IMPORTANTE PARA CUALQUIER IA QUE LEA ESTE ARCHIVO:

Alex NO está conectado técnicamente a Pipedrive, Zapier, ni sistemas de llamadas.
La landing page está en FASE PROTOTIPO.
NO asumir integración existente.
Documentar el contexto → diseñar la integración progresiva → ejecutar por fases.
```

---

## 1. QUÉ ES ALEX

Alex es el agente de IA integrado dentro de la landing page de Jardín Ideal.

| Atributo | Valor |
|----------|-------|
| **Tipo** | Agente conversacional en landing page |
| **Estado** | Prototipo — funcional pero no integrado al ecosistema |
| **Idioma** | Francés (idioma del cliente en Quebec) |
| **Plataforma** | Landing page de Jardín Ideal |
| **Función inicial** | Guiar al visitante hacia el formulario correcto |

---

## 2. ESTADO ACTUAL — DIAGNÓSTICO HONESTO

### Lo que Alex SÍ puede hacer hoy
- Responder preguntas básicas sobre los servicios de Jardín Ideal
- Guiar al visitante hacia el formulario de contacto
- Reducir la fricción de navegación en la landing page
- Dar contexto sobre los tipos de proyectos y rangos de precio

### Lo que Alex NO puede hacer hoy
- Calificar un lead como A+, A, B, C o D (no tiene suficiente información)
- Enviar datos a Pipedrive automáticamente
- Conectar con Zapier para disparar workflows
- Gestionar ni asistir en llamadas telefónicas
- Generar un LEAD_INTELLIGENCE_REPORT completo

### Por qué no se puede calificar completamente un lead desde el formulario

Los formularios actuales (Facebook + Landing Page) capturan solo:

| Campo capturado | Permite calificar |
|----------------|-------------------|
| Tipo de proyecto | Factor 5 parcial (tipo de proyecto) |
| Tiempo estimado | Factor 2 parcial (urgencia) |
| Presupuesto estimado | Factor 1 parcial (presupuesto) |
| Datos de contacto (nombre, tel, email) | Factor 8 (profesionalismo) |

**Factores NO cubiertos por el formulario:**
- Factor 3 — Autoridad de decisión (¿quién decide realmente?)
- Factor 4 — Zona geográfica exacta (el formulario no siempre la captura)
- Factor 6 — Interés real demostrado (se infiere, no se confirma)
- Factor 7 — Capacidad financiera confirmada (propietario vs. inquilino)

**Conclusión:** Con el formulario actual solo se genera un PRE-SCORE, no un score completo.

---

## 3. SISTEMA DE PRE-SCORE — FORMULARIO

Cuando un lead entra por formulario (Facebook o Landing Page), aplicar este pre-score:

```
PRE-SCORE — JARDÍN IDEAL
(basado únicamente en datos del formulario)

FACTOR 1 — PRESUPUESTO DECLARADO:
  > $25,000 CAD       → 25 pts
  $15,000–$25,000     → 20 pts
  $8,000–$15,000      → 14 pts
  $3,500–$8,000       → 8 pts
  < $3,500 o no indica → 2 pts

FACTOR 2 — URGENCIA DECLARADA:
  Dentro de 30 días   → 20 pts
  1–3 meses           → 15 pts
  3–6 meses           → 8 pts
  Sin fecha / explorando → 3 pts

FACTOR 5 — TIPO DE PROYECTO:
  Cour arrière + Piscina → 10 pts
  Pavé-Uni grande        → 9 pts
  Cour avant/Balcon      → 8 pts
  Escalier/Clôture       → 5 pts
  No especificado        → 3 pts

SUBTOTAL FORMULARIO:  ___ / 55 pts máximos
PRE-SCORE ESTIMADO:   [SUBTOTAL / 55] × 100 = ___/100

PRE-CLASIFICACIÓN:
  ≥ 70 pts → PRE-A (requiere llamada urgente para confirmar)
  50–69    → PRE-B (requiere llamada para calificar)
  < 50     → PRE-C/D (requiere llamada para confirmar o descartar)

⚠️ NUNCA convertir el pre-score en clasificación final sin llamada.
   El pre-score solo define la URGENCIA de la llamada, no el perfil final.
```

---

## 4. TRES FASES DE EVOLUCIÓN DE ALEX

### FASE 1 — LANDING PAGE GUIDE (estado actual → estabilizar)

**Objetivo:** Que el visitante entienda los servicios y llegue al formulario sin fricción.

```
Funciones de Alex en Fase 1:
  1. Bienvenida al visitante en francés
  2. Explicar los 9 servicios de forma simple (→ qué es un pavé-uni, etc.)
  3. Mostrar rangos de precio orientativos
  4. Responder preguntas frecuentes:
     - "Combien ça coûte?"
     - "Combien de temps ça prend?"
     - "Est-ce que vous faites des piscines?"
     - "Comment ça marche pour avoir une soumission?"
  5. Guiar hacia el formulario correcto según el tipo de proyecto
  6. Si el visitante abandona: trigger de remarketing (futuro — no hoy)

Limitaciones aceptadas en Fase 1:
  - Alex NO califica. Solo guía.
  - Alex NO tiene acceso a datos del CRM.
  - Alex NO dispara ningún webhook.
```

**Indicadores de éxito Fase 1:**
- Tasa de completación del formulario ≥ 40%
- Tiempo promedio en landing page ≥ 2 minutos
- Leads que llegan al formulario con datos completos

---

### FASE 2 — FORM ASSISTANT (próximo paso — integración básica)

**Objetivo:** Alex ayuda durante el llenado del formulario y genera el pre-score al enviarlo.

```
Funciones de Alex en Fase 2:
  1. Asistir al visitante mientras llena el formulario
     - Explicar qué significa cada campo
     - Sugerir rangos de presupuesto según el tipo de proyecto
     - Confirmar que el tipo de proyecto que eligió es el correcto
  2. Al enviar el formulario:
     - Calcular el PRE-SCORE (ver sección 3)
     - Enviar a Pipedrive: datos del lead + pre-score como nota
     - (Opcional) Enviar confirmación por email al lead

Integraciones requeridas para Fase 2:
  [ ] Webhook o API con Pipedrive → crear deal automáticamente
  [ ] Zapier: formulario → Pipedrive → notificación a Daniel/agente
  [ ] Campo personalizado en Pipedrive: "Pre-Score Alex" (número 0–100)
  [ ] Campo personalizado: "Pre-Clasificación" (PRE-A / PRE-B / PRE-C)

Tiempo estimado de implementación: 2–4 horas técnicas (Zapier + Pipedrive)
Requiere: acceso a Pipedrive API + Zapier cuenta activa
```

---

### FASE 3 — CALL QUALIFICATION AGENT (futuro — post integración)

**Objetivo:** Alex (o un agente telefónico asistido) completa la calificación después de que el lead entra a Pipedrive.

```
Funciones de Alex en Fase 3:
  1. Después de que el lead entra a Pipedrive:
     a. Enviar mensaje de WhatsApp / SMS de confirmación al lead
     b. Ofrecer posibilidad de hablar con alguien ahora
     c. Si el lead responde → transferir a agente humano o llamar automáticamente
  
  2. Durante o después de la llamada de calificación:
     a. Completar los factores faltantes del ICS:
        - Factor 3: Autoridad de decisión (¿ambos pueden venir a la visita?)
        - Factor 4: Zona exacta (para optimizar logística)
        - Factor 6: Interés real (¿ya pidió otra cotización?)
        - Factor 7: Capacidad financiera (¿propietario?)
     b. Calcular CALL_QUALIFICATION_SCORE completo (ver LEAD_REVIEW_ENGINE.md)
     c. Crear nota estructurada en Pipedrive con todos los factores
  
  3. Antes de la visita del vendedor:
     a. Generar LEAD_INTELLIGENCE_REPORT automáticamente
     b. Enviar al vendedor por WhatsApp: briefing de 5 puntos
     c. Confirmar hora de visita por mensaje al lead

Integraciones requeridas para Fase 3:
  [ ] Pipedrive → Zapier → WhatsApp Business API o Twilio
  [ ] Agente de llamada (Bland.AI, VAPI, Retell AI, o similar)
  [ ] Pipedrive campos personalizados completos (todos los factores ICS)
  [ ] Plantilla de nota estructurada en Pipedrive
  [ ] Sistema de briefing pre-visita automático

Tiempo estimado: 2–4 semanas de implementación técnica
Requiere: decidir plataforma de agente de voz + presupuesto
```

---

## 5. ARQUITECTURA DE DATOS — FLUJO COMPLETO (futuro)

```
VISITANTE
    ↓
LANDING PAGE + ALEX (Fase 1 — guía)
    ↓
FORMULARIO (Fase 2 — asistencia)
    ↓ (webhook)
PIPEDRIVE DEAL CREADO
  + Pre-Score Alex (0–100)
  + Pre-Clasificación (PRE-A/B/C)
    ↓ (Zapier trigger)
NOTIFICACIÓN A DANIEL/AGENTE (WhatsApp)
    ↓
LLAMADA DE CALIFICACIÓN (Fase 3)
  + CALL_QUALIFICATION_SCORE completo
  + Nota estructurada en Pipedrive
    ↓
CLASIFICACIÓN FINAL: A / B / C / D
    ↓
LEAD_INTELLIGENCE_REPORT generado
    ↓
VENDEDOR PREPARADO → VISITA
```

---

## 6. CAMPOS REQUERIDOS EN PIPEDRIVE (diseño futuro)

Para que el sistema funcione en Fase 2 y 3, Pipedrive necesita estos campos personalizados:

```
CAMPOS OBLIGATORIOS (Fase 2 — formulario):
  □ Tipo de proyecto (dropdown: Cour arrière, Pavé-Uni, Piscine, etc.)
  □ Presupuesto estimado (rango: <$5K / $5-15K / $15-25K / >$25K)
  □ Urgencia (dropdown: Dès que possible / 1-3 mois / 3-6 mois / L'année prochaine)
  □ Pre-Score Alex (número 0–100)
  □ Pre-Clasificación (texto: PRE-A / PRE-B / PRE-C)
  □ Fuente (Meta Ads / Landing Page / Google / Referido / Orgánico)

CAMPOS DE CALIFICACIÓN (Fase 3 — llamada):
  □ Zona exacta (texto libre)
  □ Ambos tomadores de decisión disponibles (Sí / No / Por confirmar)
  □ Propietario confirmado (Sí / No)
  □ Otras cotizaciones pedidas (Sí / No / Cuántas)
  □ Call Qualification Score (número 0–100)
  □ Clasificación final (A / B / C / D)
  □ Notas pre-visita (texto largo)
  □ Fecha propuesta de visita (fecha)
```

---

## 7. DECISIONES ESTRATÉGICAS — ✅ APROBADAS 2026-06-23

| # | Decisión | Opción aprobada | Estado |
|---|---------|----------------|--------|
| 1 | Plataforma de Alex | Landing page actual + chat actual (hoy). Arquitectura futura: **Voiceflow + VAPI** | ✅ Aprobada |
| 2 | Herramienta de integración | **Zapier** — sin API propia en Fase 2 | ✅ Aprobada |
| 3 | Modelo de calificación Fase 3 | **Humano asistido** — vendedor llama, Alex genera pre-score + guía de llamada + reporte | ✅ Aprobada |
| 4 | Visibilidad del Pre-Score | **Interno únicamente** — el lead nunca ve el score ni la clasificación | ✅ Aprobada |
| 5 | Activación Fase 2 | **Inmediata** — sprint de 5 días hábiles | ✅ Aprobada |

**Roadmap de implementación:** `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_FASE2_IMPLEMENTATION_ROADMAP.md`

---

## 8. IMPLEMENTACIÓN FASE 2 — SPRINT ACTIVO

```
PRERREQUISITO (hoy): Confirmar plataforma del formulario actual
DÍA 1 (45 min):  Crear 8 campos en Pipedrive
DÍA 2 (2 horas): Configurar Zap 1 — Formulario → Pipedrive + PRE-SCORE
DÍA 3 (1 hora):  Configurar Zap 2 — Alerta a Daniel por email/WhatsApp
DÍA 4 (1 hora):  Test completo con 4 leads falsos (PRE-A/B/C + incompleto)
DÍA 5 (30 min):  Go live + monitoreo
```

**Plan detallado día a día:** `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_FASE2_IMPLEMENTATION_ROADMAP.md`

**Referencia del sistema de calificación completo:** `10_MEMORIA_EMPRESARIAL/SISTEMA_CLIENTE_IDEAL.md`
**Motor de calificación diaria:** `10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/LEAD_REVIEW_ENGINE.md`
