# REPORTING SYSTEM MAP — JARDÍN IDEAL
**Versión:** 1.0 | **Fecha:** 2026-06-24
**Ubicación:** `08_REPORTES/REPORTING_SYSTEM_MAP.md`

---

## FLUJO MAESTRO DEL SISTEMA DE REPORTES

```
╔══════════════════════════════════════════════════════════════════╗
║              FLUJO DE DATOS — JARDÍN IDEAL 2026                  ║
╚══════════════════════════════════════════════════════════════════╝

FUENTES EXTERNAS
     │
     ├── Meta Ads Manager ──────────────────────────────┐
     │     (leads, CPL, alcance, CTR)                   │
     │                                                  ▼
     ├── Google Ads ──────────────────────────────► META_ADS/
     │     (search leads, CPC, keywords)           GOOGLE_ADS/
     │                                                  │
     ├── Landing Page ─────────────────────────────────►│
     │     (formulario contacto → futuro: Zapier)       │
     │                                                  │
     └── WhatsApp equipo campo ──────────────────► OPERACIONES/
           (proyectos en curso, incidencias)            │
                                                        │
                                                        ▼
                                                  ┌─────────────┐
                                                  │    CRM /    │
                                                  │  Pipedrive  │
                                                  │             │
                                                  │ Lead entra  │
                                                  │ Score ICS   │
                                                  │ Pipeline    │
                                                  │ Follow-up   │
                                                  └──────┬──────┘
                                                         │
                                                         ▼
                                               RESUMENES_DIARIOS/
                                               (integra todo — 17:00h)
                                                         │
                                                         ▼
                                                  DASHBOARDS/
                                               (CEO view — 2 min)
                                                         │
                                              ┌──────────┴───────────┐
                                              │                      │
                                              ▼                      ▼
                                     Decisión de presupuesto   START_DAY_ENGINE
                                     (Meta Ads, contratación)  (07:00h del día siguiente)
```

---

## DETALLE DEL FLUJO POR ETAPA

### ETAPA 1 — META ADS → CRM

**Qué pasa:**
1. Un lead ve el Hero Post / Reel de Jardín Ideal en Meta Ads
2. Hace clic → llega al formulario de la landing page
3. Llena el formulario (nombre, servicio, urgencia, presupuesto)
4. **Futuro (Zapier Zap #1):** formulario → PRE-SCORE calculado automáticamente → Deal creado en Pipedrive
5. **Actual (manual):** Daniel revisa el formulario → crea el deal manualmente en Pipedrive

**Archivos generados:**
- `META_ADS/meta_ads_YYYY-MM-DD.md` — registro del rendimiento diario
- `CRM/crm_pipeline_YYYY-MM-DD.md` — nuevo lead aparece en pipeline

**Tiempo máximo entre lead y primer contacto:**
- PRE-A (score ≥75): **≤2 horas**
- PRE-B (score 55-74): **≤4 horas**
- PRE-C (score <55): **≤24 horas**

---

### ETAPA 2 — CRM → OPERACIONES

**Qué pasa:**
1. Daniel llama al lead → calificación completa ICS (100 puntos, 8 factores)
2. Si ICS ≥65 (Lead A o B): se envía soumission / se agenda visita
3. Si la propuesta es aceptada: Deal pasa a "Ganado" en Pipedrive
4. Se agenda el proyecto en el calendario de operaciones
5. El equipo de campo ejecuta el trabajo

**Archivos generados:**
- `CRM/crm_pipeline_YYYY-MM-DD.md` — actualización de etapa del deal
- `OPERACIONES/operaciones_proyectos_YYYY-MM-DD.md` — proyecto añadido a agenda

---

### ETAPA 3 — OPERACIONES → DASHBOARDS

**Qué pasa:**
1. El equipo de campo completa el proyecto
2. Se toman fotografías → Francisco las selecciona → van a `05_MARKETING/00_BIBLIOTECA_VISUAL/`
3. Daniel actualiza Pipedrive: deal → "Completado"
4. El ingreso se registra en el reporte diario
5. El ingreso aparece en el CEO Dashboard

**Archivos generados:**
- `OPERACIONES/proyecto_[CLIENTE]_[FECHA].md` — resumen del proyecto completado
- `RESUMENES_DIARIOS/reporte_YYYY-MM-DD.md` — ingreso aparece en sección operaciones

---

### ETAPA 4 — RESUMENES DIARIOS → DASHBOARDS

**Qué pasa (17:00h todos los días hábiles):**
1. Daniel abre `RESUMENES_DIARIOS/reporte_diario.md` (plantilla)
2. Copia → renombra `reporte_YYYY-MM-DD.md`
3. Llena las secciones con datos de CRM + Meta Ads + Operaciones
4. Guarda el archivo → commit → push a GitHub
5. Actualiza el CEO Dashboard (`DASHBOARDS/dashboard_CEO_YYYY-MM-DD.md`)
6. Comparte por WhatsApp si hay novedades importantes

**Archivos generados:**
- `RESUMENES_DIARIOS/reporte_YYYY-MM-DD.md`
- `DASHBOARDS/dashboard_CEO_YYYY-MM-DD.md`

---

### ETAPA 5 — DASHBOARDS → START_DAY_ENGINE (inicio del ciclo)

**Qué pasa (07:00h del día siguiente):**
1. Daniel abre Claude Code (o Claude Desktop)
2. Activa el START_DAY_ENGINE
3. El engine lee automáticamente:
   - `DASHBOARDS/dashboard_CEO_[ayer].md` → ingresos, pipeline
   - `CRM/crm_pipeline_[ayer].md` → leads sin contactar, follow-ups urgentes
   - `OPERACIONES/operaciones_proyectos_[ayer].md` → proyectos activos
   - `META_ADS/meta_ads_[ayer].md` → campañas con alerta de CPL
4. Genera el DAILY_BRIEF con 8 secciones
5. Daniel actúa sobre las prioridades antes de las 09:00h

**El ciclo se reinicia.**

---

## MAPA DE RESPONSABILIDADES

| Sistema | Quién crea | Cuándo | Quién lee | Para qué |
|---------|-----------|--------|----------|---------|
| `META_ADS/` | Daniel (manual) / Zapier (futuro) | Diario 08:00h | Daniel + START_DAY_ENGINE | Optimizar campañas |
| `GOOGLE_ADS/` | Daniel (manual) | Semanal (lunes) | Daniel | Comparar CPL entre canales |
| `CRM/` | Daniel + Pipedrive | Diario al entrar/salir leads | Daniel + START_DAY_ENGINE | No perder leads |
| `OPERACIONES/` | Daniel + equipo campo | Diario (días con trabajo) | Daniel | Coordinar equipo |
| `RESUMENES_DIARIOS/` | Daniel | 17:00h diario | START_DAY_ENGINE 07:00h | Input del día siguiente |
| `DASHBOARDS/` | Daniel | 17:00h diario | Daniel (CEO) | Decisiones estratégicas |

---

## AUTOMATIZACIONES REQUERIDAS (roadmap)

| Automatización | Estado | Impacto |
|----------------|--------|---------|
| Formulario → PRE-SCORE → Pipedrive (Zapier Zap #1) | ⬜ Pendiente | Alto — elimina entrada manual de leads |
| Pipedrive → Alerta WhatsApp Daniel (Zapier Zap #2) | ⬜ Pendiente | Alto — evita perder leads PRE-A |
| Meta Ads Leads → Pipedrive (Zapier Zap #3) | ⬜ Pendiente | Alto — captura leads de anuncios con Lead Forms |
| Reporte diario generado automáticamente a 17:00h | ⬜ Pendiente | Medio — ahorra 10 min/día |

Ver detalles: `07_AUTOMATIZACIONES/` y `10_MEMORIA_EMPRESARIAL/ECOSISTEMA_BACKTEST_V1.md`

---

## ESTADO ACTUAL DEL SISTEMA (2026-06-24)

```
META_ADS/      → 🟡 Manual — Daniel registra manualmente desde Ads Manager
GOOGLE_ADS/    → 🟡 Manual — revisión semanal
CRM/           → 🟡 Manual — Pipedrive activo, Zapier pendiente
OPERACIONES/   → 🟡 Manual — WhatsApp equipo → Daniel actualiza
RESUMENES/     → 🟡 Manual — Daniel llena plantilla diariamente
DASHBOARDS/    → 🟡 Manual — CEO Dashboard diario

AUTOMATIZACIÓN GLOBAL: 0% implementado
→ Todos los flujos son manuales hasta que Zapier esté configurado
→ Sprint 2026-06-24/30: implementar los 3 Zaps críticos
```

---

## PRÓXIMO PASO PARA OPERACIONALIZAR

1. Configurar los 3 Zapier Zaps críticos (ver `10_MEMORIA_EMPRESARIAL/PROXIMO_SPRINT.md`)
2. Llenar el primer reporte diario real hoy (2026-06-24) usando la plantilla en `RESUMENES_DIARIOS/`
3. Crear el primer CEO Dashboard real de la semana

---

*REPORTING SYSTEM MAP v1.0 — Jardín Ideal — 2026-06-24*
