# ALEX — ROADMAP DE IMPLEMENTACIÓN FASE 2
**Estado:** ✅ APROBADO — Implementación inmediata
**Fecha de aprobación:** 2026-06-23
**Responsable:** Daniel
**Tiempo total estimado:** 5 días hábiles

---

## DECISIONES BASE — CONFIRMADAS

| # | Decisión | Opción aprobada |
|---|---------|----------------|
| 1 | Plataforma Alex | Landing page actual + chat actual. Arquitectura futura: Voiceflow + VAPI |
| 2 | Integración | Zapier — sin API propia en esta fase |
| 3 | Calificación | Modelo humano asistido — vendedor llama, Alex genera datos |
| 4 | Score | Interno únicamente — el lead nunca ve el score |
| 5 | Activación | Inmediata — sprint de 5 días |

---

## ARQUITECTURA FASE 2 — CONFIRMADA

```
VISITANTE EN LANDING PAGE
         ↓
ALEX (chat actual — Fase 1, no cambia)
         ↓ (guía al formulario)
FORMULARIO (landing page actual)
         ↓ webhook
ZAP 1 — FORM → PIPEDRIVE
  · Crear deal automáticamente
  · Calcular LANDING_PRE_SCORE
  · Poblar campos personalizados
  · Clasificar PRE-A / PRE-B / PRE-C
         ↓
ZAP 2 — CLASIFICACIÓN → ALERTA
  · PRE-A → WhatsApp/Email URGENTE a Daniel (llamar en <2h)
  · PRE-B → WhatsApp/Email a Daniel (llamar en <4h)
  · PRE-C → Email resumen (llamar en <24h)
         ↓
PIPEDRIVE DEAL ACTIVO
  + PRE-SCORE visible para el equipo
  + GUÍA DE LLAMADA generada por Alex (template automático)
  + Todos los campos del formulario
         ↓
VENDEDOR LLAMA (humano)
  Usa: Guía de llamada de Alex en Pipedrive
  Registra: resultados de la llamada en Pipedrive
         ↓
CALL_QUALIFICATION_SCORE (entrada manual del vendedor)
         ↓
ALEX genera LEAD_INTELLIGENCE_REPORT
  → Enviado al vendedor antes de la visita
```

---

## LO QUE ALEX GENERA EN FASE 2

### 1. LANDING_PRE_SCORE (automático, calculado por Zapier)

Basado en los datos del formulario, Zapier calcula:

```
F1 Presupuesto declarado:
  > $25K → 25 pts | $15-25K → 20 | $8-15K → 14 | $3.5-8K → 8 | < $3.5K → 2

F2 Urgencia declarada:
  <30 días → 20 | 1-3 meses → 15 | 3-6 meses → 8 | Sin fecha → 3

F5 Tipo de proyecto:
  Piscine+Cour arrière/Cour arrière → 10 | Pavé-Uni → 9 | Cour avant/Balcon → 8
  Escalier/Clôture → 5 | No especificado → 3

Bonus:
  Referido → +5 | Combo 2+ proyectos → +3 | Formulario completo → +2

TOTAL / 60 × 100 = PRE-SCORE (0–100)
PRE-A ≥75 | PRE-B 55-74 | PRE-C <55
```

### 2. GUÍA DE LLAMADA (template automático en nota Pipedrive)

Zapier inserta automáticamente esta nota en el deal al crearlo:

```
GUÍA DE LLAMADA — [NOMBRE LEAD]
PRE-SCORE: [XX]/100 → [PRE-A/B/C]

DATOS YA CONFIRMADOS (del formulario):
  ✅ Proyecto: [TIPO]
  ✅ Presupuesto: [RANGO]
  ✅ Urgencia: [TIMING]
  ✅ Tel: [NÚMERO]

DATOS A CONFIRMAR EN LA LLAMADA (en este orden):
  □ 1. "Est-ce que vous prenez cette décision seul(e) ou avec votre conjoint(e)?"
        → Si couple: "Est-ce que vous deux pourriez être présents lors de la visite?"
  □ 2. "Vous êtes bien propriétaire de la propriété?"
  □ 3. "Avez-vous déjà reçu des soumissions pour ce projet?"
  □ 4. "Qu'est-ce qui vous a amené à nous contacter en particulier?"
  □ 5. "Avez-vous une date en tête pour que le projet soit terminé?"

OBJETIVO DE LA LLAMADA:
  → PRE-A: Confirmar visita para HOY o mañana
  → PRE-B: Confirmar visita en 48-72h
  → PRE-C: Calificar y decidir si agendar o nutrir

SEÑALES DE COMPRA A ANOTAR:
  (ver ALEX_OBJECTION_HANDLING.md Sección 3 para scripts)
```

### 3. LEAD_INTELLIGENCE_REPORT (semi-automático, post-llamada)

Después de que el vendedor registra los resultados en Pipedrive, se puede generar el reporte completo usando el template en `ALEX_LEAD_REPORT_TEMPLATE.md`.

En Fase 2: el vendedor copia el template y lo llena manualmente (5 min).
En Fase 3: Alex lo genera automáticamente.

---

## SPRINT DE IMPLEMENTACIÓN — 5 DÍAS

### PRERREQUISITO — ANTES DE EMPEZAR (confirmar hoy)

```
□ Confirmar la plataforma del formulario actual:
  ¿Es Typeform / Tally / Webflow Form / Formulario HTML custom / Otro?
  → Esto determina cómo Zapier recibe los datos

□ Acceso a Pipedrive con permisos de administrador
  → Para crear campos personalizados

□ Cuenta Zapier activa
  → Si no existe: crear en zapier.com (plan gratuito suficiente para comenzar)

□ Número de WhatsApp o email de Daniel para las alertas
  → Definir canal preferido para notificaciones urgentes
```

---

### DÍA 1 — PIPEDRIVE: CREAR CAMPOS (estimado: 45 minutos)

**Quién lo hace:** Daniel o alguien con acceso admin a Pipedrive
**Referencia:** `ALEX_PIPEDRIVE_FIELDS.md` → sección "Campos a crear Fase 2"

Campos a crear en este orden:

```
SECCIÓN "ORIGEN":
  1. Source du lead (Dropdown)
     Opciones: Meta Ads / Landing Page / Google / Référé / Organique / Autre

SECCIÓN "PROYECTO":
  2. Type de projet (Dropdown)
     Opciones: Cour avant / Cour arrière / Pavé-Uni / Balcon / Piscine /
               Escalier / Clôture / Mur de béton / Combo (2+)
  3. Description du projet (Texto largo)

SECCIÓN "PRESUPUESTO Y URGENCIA":
  4. Budget estimé déclaré (Dropdown)
     Opciones: Moins de $5K / $5K–$10K / $10K–$20K / $20K–$40K / $40K–$80K / $80K+ / Non précisé
  5. Urgence déclarée (Dropdown)
     Opciones: Dans 30 jours / 1–3 mois / 3–6 mois / L'année prochaine / Sans date

SECCIÓN "SCORES ALEX":
  6. Landing PRE-SCORE (Número — entero 0 a 100)
  7. Landing PRE-Classification (Dropdown)
     Opciones: PRE-A / PRE-B / PRE-C / PRE-D

SECCIÓN "GUÍA DE LLAMADA":
  8. Guía de llamada Alex (Texto largo — campo para la nota generada)

VERIFICACIÓN FINAL DÍA 1:
  □ Los 8 campos están creados y visibles en el formulario de deal
  □ Los dropdowns tienen todas las opciones correctas
  □ El campo PRE-SCORE acepta números de 0 a 100
```

---

### DÍA 2 — ZAPIER: ZAP 1 — FORMULARIO → PIPEDRIVE (estimado: 2 horas)

**Quién lo hace:** Daniel o la persona técnica del equipo

```
PASO 1 — Crear nuevo Zap en zapier.com

TRIGGER: "New Submission" en [plataforma del formulario]
  (Typeform / Tally / Webflow / etc. — según el resultado del prerrequisito)
  → Conectar la cuenta de la plataforma del formulario
  → Seleccionar el formulario de contacto de Jardín Ideal
  → Probar con una respuesta de prueba

PASO 2 — ACCIÓN 1: Formatter by Zapier
  (Calcular el LANDING_PRE_SCORE)

  Sub-acción: "Numbers — Perform Math"
  Fórmula para calcular el score:

  SCORE_F1:
    IF budget = ">$25,000" → 25
    IF budget = "$15,000–$25,000" → 20
    IF budget = "$8,000–$15,000" → 14
    IF budget = "$3,500–$8,000" → 8
    IF budget = "<$3,500" OR empty → 2

  SCORE_F2:
    IF urgency = "Dans 30 jours" → 20
    IF urgency = "1–3 mois" → 15
    IF urgency = "3–6 mois" → 8
    ELSE → 3

  SCORE_F5:
    IF project = "Piscine" OR "Cour arrière" → 10
    IF project = "Pavé-Uni" → 9
    IF project = "Cour avant" OR "Balcon" → 8
    IF project = "Escalier" OR "Clôture" → 5
    ELSE → 3

  PRE_SCORE = ((SCORE_F1 + SCORE_F2 + SCORE_F5) / 55) × 100 → redondear al entero

  PRE_CLASS:
    IF PRE_SCORE ≥ 75 → "PRE-A"
    IF PRE_SCORE ≥ 55 → "PRE-B"
    ELSE → "PRE-C"

  NOTA: En Zapier, esto se hace con pasos "Formatter → Numbers" o con el paso
        "Code by Zapier" (JavaScript) si los condicionales son complejos.
        Código JavaScript de ejemplo para el paso Code:

        const budget_map = {">25000":25,"15000-25000":20,"8000-15000":14,"3500-8000":8};
        const urgency_map = {"30jours":20,"1-3mois":15,"3-6mois":8};
        const project_map = {"piscine":10,"cour_arriere":10,"pave":9,"cour_avant":8,"balcon":8,"escalier":5,"cloture":5};

        const f1 = budget_map[inputData.budget] || 2;
        const f2 = urgency_map[inputData.urgency] || 3;
        const f5 = project_map[inputData.project] || 3;
        const raw = f1 + f2 + f5;
        const score = Math.round((raw / 55) * 100);
        const classif = score >= 75 ? "PRE-A" : score >= 55 ? "PRE-B" : "PRE-C";

        return {prescore: score, preclassif: classif, raw_f1:f1, raw_f2:f2, raw_f5:f5};

PASO 3 — ACCIÓN 2: Pipedrive — Create Deal
  Campos a mapear:
    Deal name: [Prénom] [Nom] - [Type de projet] - [Ville si disponible]
    Pipeline: Lead Pipeline
    Stage: "Nouveau lead"
    Contact name: [Prénom] + [Nom]
    Contact phone: [Téléphone]
    Contact email: [Email]
    Source du lead: "Landing Page" (valor fijo para este Zap)
    Type de projet: [Campo tipo proyecto del formulario]
    Description du projet: [Campo descripción]
    Budget estimé déclaré: [Campo presupuesto]
    Urgence déclarée: [Campo urgencia]
    Landing PRE-SCORE: [Score calculado en Paso 2]
    Landing PRE-Classification: [PRE-A/B/C calculado en Paso 2]

PASO 4 — ACCIÓN 3: Pipedrive — Create Note
  Deal ID: [ID del deal creado en Paso 3]
  Note content: [Template de Guía de Llamada — ver sección anterior]
  (Usar texto fijo del template + variables del formulario interpoladas)

VERIFICACIÓN FINAL DÍA 2:
  □ El Zap se activa con una prueba de formulario
  □ El deal aparece en Pipedrive con todos los campos
  □ El PRE-SCORE está calculado correctamente
  □ La nota "Guía de llamada" aparece en el deal
```

---

### DÍA 3 — ZAPIER: ZAP 2 — ALERTA A DANIEL (estimado: 1 hora)

```
TRIGGER: "Deal Updated" en Pipedrive
  Filtro: Campo "Landing PRE-Classification" cambia a cualquier valor

PASO 1 — FILTRO: Only continue if...
  PRE-Classification is any of: PRE-A, PRE-B, PRE-C
  (Esto asegura que solo corre cuando hay un score calculado)

PASO 2 — ACCIÓN: Enviar alerta (elegir según canal preferido de Daniel)

OPCIÓN A — Email (más simple, disponible en Zapier gratis):
  To: daniel@groupe-ideal.com
  Subject: [PRE-A/B/C] Nouveau lead — [Nom] — [Projet]
  Body:
    "🆕 NOUVEAU LEAD — [PRE-Classification]
     Nom: [Nom]
     Projet: [Type de projet]
     Budget: [Budget]
     Urgence: [Urgence]
     Téléphone: [Tel]
     Score Alex: [PRE-SCORE]/100

     ⏰ PRE-A → Appeler dans les 2 heures
     ⏰ PRE-B → Appeler dans les 4 heures
     ⏰ PRE-C → Appeler dans les 24 heures

     Voir Pipedrive pour la Guía de llamada complète."

OPCIÓN B — SMS via Twilio (si tienen cuenta Twilio activa):
  To: +1 514-XXX-XXXX
  Message: "🆕 [PRE-A] [Nom] — [Projet] — [Tel] — Alex score: [XX]/100"

OPCIÓN C — WhatsApp Business API (si está configurado):
  Mismo mensaje que la opción B pero por WhatsApp

RECOMENDACIÓN INMEDIATA: Comenzar con Email (Opción A) — no requiere setup adicional.
Migrar a WhatsApp cuando el volumen lo justifique.

VERIFICACIÓN FINAL DÍA 3:
  □ El Zap 2 envía la alerta cuando se crea un deal PRE-A
  □ El Zap 2 envía la alerta cuando se crea un deal PRE-B
  □ El Zap 2 NO envía alerta para PRE-D (leads descalificados)
  □ El mensaje de alerta tiene todos los datos necesarios para que Daniel pueda llamar
```

---

### DÍA 4 — TEST COMPLETO CON LEAD FALSO (estimado: 1 hora)

```
PROTOCOLO DE PRUEBA:

TEST 1 — Lead PRE-A (debería disparar alerta urgente):
  Formulario: Piscine + Cour arrière | Budget: $40K+ | Urgence: Dans 30 jours
  Resultado esperado:
    □ Deal creado en Pipedrive
    □ PRE-SCORE ≥ 75 → PRE-A
    □ Nota "Guía de llamada" creada
    □ Alerta enviada a Daniel en <2 minutos

TEST 2 — Lead PRE-B (alerta estándar):
  Formulario: Cour avant | Budget: $10-20K | Urgence: 1-3 mois
  Resultado esperado:
    □ Deal creado en Pipedrive
    □ PRE-SCORE 55-74 → PRE-B
    □ Nota creada
    □ Alerta enviada

TEST 3 — Lead PRE-C (alerta de baja prioridad):
  Formulario: Clôture | Budget: <$5K | Urgence: L'année prochaine
  Resultado esperado:
    □ Deal creado en Pipedrive
    □ PRE-SCORE < 55 → PRE-C
    □ Nota creada
    □ Alerta enviada (pero con indicación de baja prioridad)

TEST 4 — Lead formulario incompleto:
  Formulario: Solo nombre y teléfono, sin proyecto ni presupuesto
  Resultado esperado:
    □ Deal creado en Pipedrive (no bloquear el proceso)
    □ PRE-SCORE = valor mínimo (presupuesto no indicado + urgencia no indicada)
    □ PRE-C por defecto
    □ Alerta enviada con indicación "Datos incompletos"

APROBACIÓN PARA SIGUIENTE PASO:
  Todos los 4 tests pasados → Día 5: Go Live
  Algún test fallido → Corregir en Zapier y repetir
```

---

### DÍA 5 — GO LIVE + MONITOREO (estimado: 30 minutos + seguimiento)

```
CHECKLIST DE ACTIVACIÓN:
  □ Activar ambos Zaps en Zapier (toggle ON)
  □ Eliminar los deals de prueba de Pipedrive
  □ Confirmar que el formulario de la landing page está activo y recibiendo tráfico
  □ Enviar un formulario real de prueba final desde el dispositivo de Daniel
  □ Confirmar que llegó el email de alerta correctamente
  □ Avisar al equipo: "Desde hoy todos los leads del formulario aparecen en Pipedrive automáticamente"

MONITOREO PRIMERA SEMANA:
  Día 1-3: Revisar cada lead manualmente para confirmar que el score es correcto
  Día 4-7: Solo revisar alertas — el sistema funciona solo

SEÑALES DE QUE ALGO FALLA:
  🔴 Un lead llena el formulario y NO aparece en Pipedrive → revisar Zap 1
  🔴 El PRE-SCORE siempre da el mismo número → revisar el paso de cálculo
  🔴 No llegan alertas → revisar Zap 2 y el filtro de PRE-Classification
  🔴 La nota "Guía de llamada" no aparece → revisar Acción 3 del Zap 1

PRIMERA REVISIÓN POST-ACTIVACIÓN:
  Al final del Día 5: revisar los primeros leads reales procesados
  Ajustar el script de cálculo si los scores no se corresponden con la realidad observada
```

---

## MÉTRICAS DE ÉXITO — FASE 2

| Métrica | Objetivo | Cómo medir |
|---------|---------|-----------|
| % leads que aparecen en Pipedrive automáticamente | 100% | Comparar formularios vs. deals |
| Tiempo medio de creación del deal tras formulario | < 2 minutos | Timestamp en Pipedrive vs. formulario |
| Tiempo de llamada del vendedor post PRE-A | < 2 horas | Log de llamadas vs. timestamp Pipedrive |
| Precisión del PRE-SCORE (correlación con clasificación final) | Calibrar en semana 2 | Comparar PRE-SCORE vs. CALL_SCORE después de 20 leads |
| Tasa de leads PRE-A que convierten en visita | ≥ 60% | Pipeline Pipedrive |

---

## SIGUIENTE PASO DESPUÉS DE FASE 2 ACTIVA

Una vez que la Fase 2 lleva 2 semanas funcionando:

1. **Migrar Alex a Voiceflow** — rediseñar el chat con los flujos de `ALEX_CONVERSATION_FLOW.md`
2. **Agregar campo Zona** al formulario — mejorar el Factor 4 del pre-score
3. **WhatsApp Business** — reemplazar el email de alerta por WhatsApp al vendedor
4. **Calibrar el PRE-SCORE** — ajustar los pesos según la correlación observada en los primeros 30 leads
5. **Fase 3 — VAPI** — cuando el volumen de leads supere la capacidad humana de llamar

**Referencia:** `ALEX_LANDING_PAGE_CONTEXT.md` Sección 4 — Fase 3
