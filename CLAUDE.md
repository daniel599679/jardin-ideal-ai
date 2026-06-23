# CLAUDE.md — Contexto de sesión para Jardín Ideal AI System

**Leer este archivo primero. Siempre.**

---

## EMPRESA

| Campo | Dato |
|-------|------|
| Empresa activa | Jardín Ideal |
| Empresa hermana | Groupe Ideal |
| Objetivo 2026 | $7,000,000 CAD |
| Teléfono CTA | 514-266-2504 |
| Idioma clientes | **Francés (Quebec)** |
| Idioma interno | **Español** |
| Reunión diaria | 09:00 AM — inamovible |

---

## AL INICIAR CUALQUIER SESIÓN

Leer en este orden exacto:

```
1. CLAUDE.md (este archivo)
2. 10_MEMORIA_EMPRESARIAL/MEMORIA_GLOBAL.md
3. 10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md
4. 10_MEMORIA_EMPRESARIAL/PROXIMO_SPRINT.md
```

Si Daniel escribe `ejecutar START_DAY_ENGINE`:
→ Leer los 4 archivos de arriba + `10_MEMORIA_EMPRESARIAL/REUNIONES_DIARIAS.md`
→ Generar el DAILY_BRIEF según el formato de `OPERACIONES_DIARIAS/START_DAY_ENGINE.md`
→ Entregar en <5 minutos sin preguntar nada

---

## SISTEMAS ACTIVOS (estado 2026-06-23)

| Sistema | Estado | Archivo principal |
|---------|--------|-------------------|
| FLOAT V2 Premium | ✅ Completo | `05_MARKETING/FLOAT_V2_PREMIUM/` |
| TEST_OPERATIVO_FLOAT_V2 | ✅ Listo para usar | `10_MEMORIA_EMPRESARIAL/TEST_OPERATIVO_FLOAT_V2.md` |
| Alex Fase 2 | 🔵 Sprint activo (5 días) | `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_FASE2_IMPLEMENTATION_ROADMAP.md` |
| Daily Operations Engine | ✅ Completo | `10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/` |
| ICS Lead Scoring | ✅ Completo | `JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md` |

---

## SPRINT ACTIVO — 24 AL 30 JUNIO 2026

**Objetivo:** Pasar de 32% a 55% de implementación real.

| Bloque | Qué hace Daniel | Qué hace Claude Code |
|--------|----------------|----------------------|
| 1 — FLOAT V2 producción | Evalúa fotos, edita, publica | Genera copy, evalúa con PREMIUM_VISUAL_SCORE |
| 2 — Alex Fase 2 | Configura Pipedrive + Zapier | Proporciona código JS y guía paso a paso |
| 3 — Meta Ads Zap | Conecta Meta → Pipedrive | Proporciona configuración exacta |
| 4 — Reportes | Llena CEO_DASHBOARD cada día a las 17:00 | Genera DAILY_BRIEF a las 07:00 |
| 5 — Automatizaciones | Configura alerta >2h en Pipedrive | — |

**Referencia completa:** `10_MEMORIA_EMPRESARIAL/PROXIMO_SPRINT.md`

---

## REGLAS DE OPERACIÓN

1. Todo contenido para clientes: **francés**. Todo interno: **español**.
2. Nunca visitar un lead sin ambos tomadores de decisión confirmados.
3. Score mínimo para publicar cualquier Hero Post: **90/100** (PREMIUM_VISUAL_SCORE).
4. Todo cambio importante: documentar en `10_MEMORIA_EMPRESARIAL/HISTORIAL_CAMBIOS.md`.
5. Commits a GitHub: al finalizar cada bloque de trabajo.

---

## LEADS URGENTES (estado 2026-06-23)

| Lead | Situación | Acción |
|------|-----------|--------|
| Paul Gagné | Propuesta $35,000 — 8 días sin respuesta | Llamar HOY — plantilla 4.2 en `06_CRM/plantillas_mensajes.md` |
| François Bergeron | Pavé-uni Laval — sin calificar | Calificar con `OPERACIONES_DIARIAS/LEAD_REVIEW_ENGINE.md` |

---

## CÓDIGO JS PARA ZAPIER (Alex Fase 2 — Zap 1)

Pegar directamente en "Code by Zapier" → JavaScript:

```javascript
const budget_map = {
  ">25000": 25,
  "15000-25000": 20,
  "8000-15000": 14,
  "3500-8000": 8
};
const urgency_map = {
  "30jours": 20,
  "1-3mois": 15,
  "3-6mois": 8
};
const project_map = {
  "piscine": 10,
  "cour_arriere": 10,
  "pave": 9,
  "cour_avant": 8,
  "balcon": 8,
  "escalier": 5,
  "cloture": 5
};

const f1 = budget_map[inputData.budget] || 2;
const f2 = urgency_map[inputData.urgency] || 3;
const f5 = project_map[inputData.project] || 3;
const raw = f1 + f2 + f5;
const score = Math.round((raw / 55) * 100);
const classif = score >= 75 ? "PRE-A" : score >= 55 ? "PRE-B" : "PRE-C";

return { prescore: score, preclassif: classif, raw_f1: f1, raw_f2: f2, raw_f5: f5 };
```

**Referencia completa:** `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_FASE2_IMPLEMENTATION_ROADMAP.md`

---

## GIT

| Campo | Dato |
|-------|------|
| Rama de trabajo | `claude/jardin-ideal-review-35t1mu` |
| Frecuencia de commit | Al finalizar cada bloque de trabajo |
| Último commit | `7043620` — TEST_OPERATIVO_FLOAT_V2 |
