# ALEX — CAMPOS PIPEDRIVE
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Propósito:** Definir exactamente qué campos crear en Pipedrive y cómo Alex los llena.

---

## ESTADO ACTUAL

```
⚠️ Estos campos NO existen aún en Pipedrive.
   Deben ser creados manualmente antes de activar la integración Alex Fase 2.
   Tiempo estimado de configuración: 1–2 horas.
```

---

## ESTRUCTURA DEL DEAL EN PIPEDRIVE

### CAMPOS ESTÁNDAR (ya existen en Pipedrive)

| Campo | Valor que Alex envía | Fuente |
|-------|---------------------|--------|
| Nom du deal | `[Prénom Nom] - [Type Projet] - [Ville]` | Formulario |
| Contacts > Nom | Nombre completo del lead | Formulario |
| Contacts > Téléphone | Número de teléfono | Formulario |
| Contacts > Email | Email del lead | Formulario |
| Valeur du deal | Midpoint del rango de presupuesto declarado | Formulario |
| Étape du pipeline | `Nouveau lead` (automático) | Sistema |
| Propriétaire | Asignado según regla (ver abajo) | Sistema |

**Regla de asignación de propietario:**
- PRE-A → asignar a Daniel directamente
- PRE-B/C → asignar al agente de ventas disponible

---

## CAMPOS PERSONALIZADOS A CREAR — FASE 2 (Formulario)

### SECCIÓN: ORIGEN Y CONTEXTO

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Source du lead` | Dropdown | Meta Ads / Landing Page / Google / Référé / Organique / Autre | Alex (automático) |
| `Medium de contact` | Dropdown | Chat / Formulaire web / Facebook Lead Form / Téléphone / WhatsApp | Alex (automático) |
| `URL de la page source` | Texto | URL completa | Alex (automático) |
| `Referido por` | Texto | Nombre del cliente que refirió (si aplica) | Alex o humano |
| `Date de contact initial` | Fecha | YYYY-MM-DD HH:MM | Alex (automático) |

---

### SECCIÓN: DATOS DEL PROYECTO

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Type de projet` | Dropdown | Cour avant / Cour arrière / Pavé-Uni / Balcon / Piscine / Escalier / Clôture / Mur de béton / Rénovation / Combo (2+) | Formulario / Alex |
| `Description du projet` | Texto largo | Descripción libre del cliente | Formulario |
| `Superficie estimée (pi²)` | Número | Sin opciones | Formulario o llamada |
| `Matériaux souhaités` | Texto | Libre (ej: "béton estampé, pas de tuiles") | Formulario o llamada |

---

### SECCIÓN: PRESUPUESTO Y URGENCIA

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Budget estimé (déclaré)` | Dropdown | Moins de $5,000 / $5,000–$10,000 / $10,000–$20,000 / $20,000–$40,000 / $40,000–$80,000 / $80,000+ / Non précisé | Formulario |
| `Budget confirmé (appel)` | Dropdown | Mêmes opciones | Llamada Fase 3 |
| `Budget: flexible ou fixe` | Dropdown | Flexible / Limite ferme / Non indiqué | Llamada Fase 3 |
| `Urgence déclarée` | Dropdown | Dans 30 jours / 1–3 mois / 3–6 mois / L'année prochaine / Sans date | Formulario |
| `Date cible du projet` | Fecha | YYYY-MM-DD | Formulario o llamada |
| `Événement déclencheur` | Texto | Ej: "fête en juillet", "vente de la maison" | Llamada Fase 3 |

---

### SECCIÓN: SCORES Y CLASIFICACIÓN

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Landing PRE-SCORE` | Número | 0–100 | Alex Fase 2 (automático) |
| `Landing PRE-Classification` | Dropdown | PRE-A / PRE-B / PRE-C / PRE-D | Alex Fase 2 (automático) |
| `Call Qualification Score` | Número | 0–100 | Alex Fase 3 (automático) |
| `Classification finale` | Dropdown | A+ / A / B / C / D | Alex Fase 3 |
| `Score F1 Presupuesto` | Número | 0–25 | Alex Fase 3 |
| `Score F2 Urgence` | Número | 0–20 | Alex Fase 3 |
| `Score F3 Autorité` | Número | 0–15 | Alex Fase 3 |
| `Score F4 Zone` | Número | 0–10 | Alex Fase 3 |
| `Score F5 Projet` | Número | 0–10 | Alex Fase 3 |
| `Score F6 Intérêt` | Número | 0–10 | Alex Fase 3 |
| `Score F7 Capacité fin.` | Número | 0–5 | Alex Fase 3 |
| `Score F8 Professionnalisme` | Número | 0–5 | Alex Fase 3 |

---

### SECCIÓN: CALIFICACIÓN FASE 3

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Propriétaire confirmé` | Dropdown | Oui / Non / Non confirmé | Llamada Fase 3 |
| `Autorité de décision` | Dropdown | Seul / Couple — les deux disponibles / Couple — un seul / Non confirmé | Llamada Fase 3 |
| `Conjoint(e) à la visite` | Dropdown | Oui / Non / À confirmer | Llamada Fase 3 |
| `Adresse exacte` | Texto | Dirección completa | Llamada Fase 3 |
| `Zone classifiée` | Dropdown | Westmount/TMR/Outremont / Montréal / Laval / Rive-Nord / Rive-Sud / Autre | Alex (calculado) |
| `Autres soumissions` | Dropdown | Aucune / 1 / 2–3 / 4+ / Non confirmé | Llamada Fase 3 |
| `Entendu parler via` | Dropdown | Pub Facebook / Instagram organique / Google / Référé client / Bouche-à-oreille / Panneau / Autre | Llamada Fase 3 |

---

### SECCIÓN: SEÑALES Y REPORTE

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Signaux d'achat détectés` | Texto largo | Lista de señales detectadas en texto | Alex Fase 3 |
| `Signaux de risque détectés` | Texto largo | Lista de riesgos detectados | Alex Fase 3 |
| `Note pré-visite Alex` | Texto largo | Reporte completo pre-visita | Alex Fase 3 |
| `Objection principale anticipée` | Dropdown | Prix / Timing / Comparaison concurrents / Autorité décision / Budget / Autre | Alex Fase 3 |
| `Question ouverture suggérée` | Texto | 1 frase concreta para el vendedor | Alex Fase 3 |
| `Projets portfolio à montrer` | Texto | 2–3 proyectos sugeridos para la visita | Alex Fase 3 |

---

### SECCIÓN: SEGUIMIENTO

| Nombre del campo | Tipo | Opciones / Formato | Quién lo llena |
|-----------------|------|-------------------|---------------|
| `Date de visite proposée` | Fecha | YYYY-MM-DD | Alex Fase 3 |
| `Date de visite confirmée` | Fecha | YYYY-MM-DD | Humano |
| `Heure de visite` | Texto | HH:MM | Humano |
| `Vendeur assigné` | Texto | Nombre del vendedor | Sistema / Daniel |
| `Date de follow-up` | Fecha | YYYY-MM-DD | Alex / Humano |
| `Raison de perte` | Dropdown | Prix / Timing / Concurrence / Hors critères / Non réponse / Changement de plan | Humano |

---

## ESTRUCTURA DEL PIPELINE PIPEDRIVE

```
ÉTAPES DU PIPELINE ALEX → JARDÍN IDEAL:

1. Nouveau lead          ← Alex Fase 2 crea el deal aquí
2. PRE-A (Contact urgent) ← Alex mueve si PRE-SCORE ≥75
3. En qualification       ← Llamada de calificación en progreso
4. Classifié A/B          ← Call score calculado, visita a confirmar
5. Visite confirmée       ← Visita agendada
6. Soumission envoyée     ← Post-visita, cotización enviada
7. Négociation            ← Objeciones de cierre
8. Gagné ✅               ← Proyecto firmado y con depósito
9. Nurturing C            ← Seguimiento largo plazo
10. Perdu ❌              ← No convertido (con razón de pérdida)
```

---

## AUTOMATIZACIONES ZAPIER — DISEÑO

### ZAP 1 — Formulario → Pipedrive

```
TRIGGER: Nueva respuesta en formulario web (Typeform / Webflow / etc.)

ACCIONES EN ORDEN:
  1. Crear deal en Pipedrive (etapa: "Nouveau lead")
  2. Crear contacto en Pipedrive (o actualizar si ya existe)
  3. Poblar todos los campos del formulario (sección PROYECTO + PRESUPUESTO)
  4. Calcular LANDING_PRE_SCORE con la fórmula del ÁRBOL 3
  5. Actualizar campo "Landing PRE-SCORE" en Pipedrive
  6. Actualizar campo "Landing PRE-Classification" en Pipedrive
  7. Enviar notificación WhatsApp a Daniel:
     "🆕 Lead [NOMBRE] - [TIPO_PROYECTO] - PRE-[SCORE] - [ZONA]
      📞 [TELÉFONO]
      🏡 Presupuesto: [PRESUPUESTO]
      ⏰ Urgencia: [URGENCIA]"
  8. SI PRE-A: → alerta adicional + mover a etapa "PRE-A (Contact urgent)"
  9. Enviar email de confirmación automático al lead
```

### ZAP 2 — Clasificación A+ → Alerta Daniel

```
TRIGGER: Campo "Classification finale" en Pipedrive = "A+"

ACCIONES:
  1. Enviar WhatsApp a Daniel: "🚨 A+ DETECTADO: [Nombre] - [Proyecto]
     Score: [X]/100 | Visita sugerida: HOY o mañana
     Ver reporte completo en Pipedrive."
  2. Asignar deal directamente a Daniel
  3. Crear actividad en Pipedrive: "Llamar AHORA" con vencimiento en 2 horas
```

### ZAP 3 — Visita confirmada → Briefing vendedor

```
TRIGGER: Campo "Date de visite confirmée" en Pipedrive tiene valor

ACCIONES:
  1. Generar y enviar LEAD_INTELLIGENCE_REPORT al vendedor (por WhatsApp)
  2. Enviar confirmación de visita al lead (WhatsApp o SMS)
  3. Crear recordatorio 30 min antes de la visita al vendedor
```

---

## INSTRUCCIONES PARA CREAR LOS CAMPOS EN PIPEDRIVE

```
Paso 1: Settings → Data Fields → Deals → Add new field
Paso 2: Crear cada campo de las tablas de arriba
Paso 3: Organizarlos en secciones (como en las tablas)
Paso 4: Marcar como obligatorios los campos clave:
        - Type de projet
        - Budget estimé (déclaré)
        - Urgence déclarée
        - Landing PRE-SCORE
        - Landing PRE-Classification
Paso 5: Compartir la estructura con el técnico que configure Zapier
```

**Tiempo estimado de creación de campos:** 1.5–2 horas
**Prerrequisito:** Acceso de administrador a Pipedrive
