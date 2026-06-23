# SISTEMA DE CLIENTE IDEAL (ICS)
**ICS:** Ideal Customer System
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Objetivo:** El vendedor llega a la visita con el nivel de preparación de un consultor.

---

## PERFILES DE CLIENTE

| Perfil | Score | Presupuesto típico | Acción |
|--------|-------|--------------------|--------|
| **A+** | ≥85 pts | >$25,000 | Visita inmediata. Máxima atención. |
| **A** | 70–84 pts | $10,000–$25,000 | Visita dentro de 48h |
| **B** | 55–69 pts | $3,500–$10,000 | Visita si hay espacio en agenda |
| **C** | <55 pts | <$3,500 o no propietario | No visitar. Redirigir con respeto. |

**Señal de A+:** El cliente pregunta "¿Cuándo pueden empezar?" — no "¿Cuánto cuesta?"

---

## SISTEMA DE PUNTUACIÓN — 4 BLOQUES (100 pts)

### Bloque 1 — Capacidad Financiera (40 pts)
| Indicador | Puntos |
|-----------|--------|
| Presupuesto >$40K | 40 |
| Presupuesto $25–39K | 35 |
| Presupuesto $15–24K | 28 |
| Presupuesto $10–14K | 22 |
| Presupuesto $6–9K | 14 |
| Presupuesto $3.5–5K | 8 |
| Presupuesto <$3.5K | 0 |

**Modificadores:** +3 si menciona proyecto adicional futuro / +8 si pagó en efectivo proyectos previos / -5 si exige precio más bajo antes de ver el trabajo

### Bloque 2 — Urgencia (25 pts)
| Urgencia declarada | Puntos |
|-------------------|--------|
| "Dès que possible" / trabajo activo | 25 |
| Fecha concreta en menos de 45 días | 22 |
| "Cet été" (verano) | 16 |
| "Automne" (otoño) | 10 |
| "L'année prochaine" | 4 |
| Sin fecha definida | 0 |

### Bloque 3 — Autoridad de Decisión (20 pts)
| Situación | Puntos |
|-----------|--------|
| Único tomador — decide solo | 20 |
| Pareja — ambos disponibles para visita | 18 |
| Pareja — uno presente, otro disponible | 8 |
| Pareja — uno presente, otro indisponible | 4 |
| Tercero (arrendatario, inquilino) | 0 |

### Bloque 4 — Perfil de Propiedad (15 pts)
| Condición | Puntos |
|-----------|--------|
| Propietario + unifamilial + zona premium | 15 |
| Propietario + unifamilial + zona estándar | 12 |
| Propietario + condo/plex | 8 |
| Propietario — tipo no confirmado | 5 |
| Arrendatario | 0 |

---

## REGLA ABSOLUTA

> **NUNCA agendar visita sin que ambos tomadores de decisión puedan estar presentes.**

Si solo puede venir uno → reagendar. Sin excepción.

---

## 8 PREGUNTAS DE CALIFICACIÓN (francés)

1. "Qu'est-ce qui vous a amené à nous contacter aujourd'hui?"
2. "Avez-vous une idée du budget que vous souhaitez investir?"
3. "Avez-vous un délai en tête pour réaliser ce projet?"
4. "Êtes-vous propriétaire de la propriété?"
5. "Est-ce que votre conjoint(e) sera présent(e) lors de la visite?"
6. "Avez-vous déjà eu des soumissions pour ce projet?"
7. "Qu'est-ce qui est le plus important pour vous dans ce projet?"
8. "Comment avez-vous entendu parler de nous?"

---

## 5 OBJECIONES CON SCRIPTS

### "C'est trop cher"
**Script:** "Je comprends. Permettez-moi de vous expliquer ce qui est inclus dans ce prix... [desglosar valor]. La question n'est pas combien ça coûte, mais combien ça rapporte en valeur à votre propriété."

### "On veut réfléchir"
**Script:** "Bien sûr. Qu'est-ce qui vous empêche de prendre la décision maintenant? Est-ce une question de budget, de timing, ou autre chose?" → Identificar objeción real.

### "J'ai eu un prix plus bas"
**Script:** "C'est possible. Pouvez-vous me partager ce qui était inclus dans cette soumission? Souvent les prix varient selon les matériaux et la garantie offerte."

### "On va le faire l'année prochaine"
**Script:** "Je comprends. Je dois vous mentionner que nos prix augmentent en moyenne 8–12% par année et notre carnet de commandes se remplit rapidement au printemps. Voulez-vous qu'on bloque une date maintenant?"

### "Je veux parler à mon conjoint"
**STOP:** No continuar. Reagendar con ambos presentes. "Bien sûr — quand est-ce qu'on pourrait se rencontrer tous les deux?"

---

## PRE-SCORE — DESDE FORMULARIO (sin llamada)

Cuando un lead entra por Meta Ads o Landing Page, el formulario solo captura 3–4 datos.
Con esos datos se calcula un PRE-SCORE parcial. **No es el score final. No define el perfil.**

| Dato del formulario | Factor ICS | Pts posibles |
|---------------------|-----------|-------------|
| Presupuesto estimado | Factor 1 | 0–25 |
| Urgencia declarada | Factor 2 | 0–20 |
| Tipo de proyecto | Factor 5 | 0–10 |
| **SUBTOTAL FORMULARIO** | | **0–55** |

**PRE-CLASIFICACIÓN (solo para definir urgencia de llamada):**

| Pre-Score | Pre-Clase | Acción |
|-----------|-----------|--------|
| ≥ 38 / 55 | PRE-A | Llamar HOY — puede ser un A o A+ |
| 27–37 / 55 | PRE-B | Llamar dentro de 4 horas |
| < 27 / 55 | PRE-C | Llamar en 24h para confirmar o descartar |

**Agente responsable del pre-score:** ALEX (Fase 2 — no activo aún)
**Referencia técnica:** `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_LANDING_PAGE_CONTEXT.md`

---

## LEAD INTELLIGENCE REPORT — ESTRUCTURA

Antes de cada visita, preparar:

```
LEAD INTELLIGENCE REPORT
Fecha: [FECHA]
Lead: [NOMBRE] — [CIUDAD]

1. Street View research: [observaciones de la propiedad]
2. Valor propiedad (Centris): [valor estimado]
3. Perfil cliente: [redes sociales, estilo de vida]
4. Resumen del proyecto solicitado
5. Score ICS: [X]/100 pts — Perfil [A+/A/B/C]
6. 3 proyectos del portfolio a mostrar
7. Objeción anticipada: [más probable]
8. Pregunta de apertura: [elegir según perfil]
```

---

## SEÑALES DE COMPRA

- Pregunta "¿Cuándo pueden empezar?"
- Menciona otros proyectos futuros
- Pregunta sobre garantía y mantenimiento
- Tiene fotos de referencia preparadas
- Habla en plural "nosotros lo haríamos"

## SEÑALES DE RIESGO

- Solo da presupuesto cuando se le presiona
- "Mi cuñado es contratista"
- Ha pedido 5+ cotizaciones
- Quiere empezar pero "después de las vacaciones" (sin fecha)
- No puede confirmar quién toma la decisión

---

**Referencia completa:** `JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md`
