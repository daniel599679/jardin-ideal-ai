# 08_REPORTES / DASHBOARDS
**Responsable:** Daniel (CEO)
**Frecuencia:** CEO Dashboard — actualización diaria 17:00h + resumen mensual

---

## QUÉ SE ALMACENA AQUÍ

Los paneles ejecutivos de alto nivel que consolidan todas las métricas en una vista de 2 minutos. Es lo que Daniel lee para tomar decisiones estratégicas. También incluye los reportes mensuales históricos.

### Archivos presentes

| Archivo | Tipo | Estado |
|---------|------|--------|
| `reporte_mensual.md` | Plantilla mensual | ✅ Plantilla oficial |
| `reporte_mensual_2026-06.md` | Reporte real junio 2026 | ✅ En progreso |

### Convención de nombres

```
CEO DASHBOARD DIARIO:   dashboard_CEO_YYYY-MM-DD.md
REPORTE MENSUAL:        reporte_mensual_YYYY-MM.md
DASHBOARD SEMANAL:      dashboard_semana_YYYY-WNN.md  (opcional)
```

---

## ESTRUCTURA DEL CEO DASHBOARD

El CEO Dashboard es una vista de lectura en 2 minutos. Máximo 1 página.

```
╔══════════════════════════════════════════════════════════╗
║           CEO DASHBOARD — JARDÍN IDEAL                   ║
║  Fecha: ___________  |  Objetivo 7M CAD 2026            ║
╚══════════════════════════════════════════════════════════╝

VENTAS
  Ingresos YTD:          $_______ CAD  (___% del objetivo anual)
  Proyectado cierre mes: $_______ CAD
  Propuestas abiertas:   $_______  CAD en pipeline
  Tasa de cierre:        ___%

LEADS
  Leads totales mes:     ___
  Costo por lead (CPL):  $___  CAD
  Leads calificados:     ___  (ICS ≥65)
  Conversión lead→deal:  ___%

OPERACIONES
  Proyectos activos:     ___
  Proyectos completados mes: ___
  Ingresos realizados:   $_______ CAD

MARKETING
  Inversión Meta Ads:    $___  CAD (este mes)
  ROAS (ingresos/gasto): ___×
  Mejor campaña:         _______________

ALERTA DEL DÍA:
  [ ] _______________________________________________
```

---

## FRECUENCIA DE ACTUALIZACIÓN

| Acción | Cuándo | Tiempo estimado |
|--------|--------|----------------|
| CEO Dashboard diario | 17:00h (junto al reporte diario) | 5 min |
| Reporte mensual | Primer lunes del mes | 60 min |
| Revisión trimestral | Primer lunes de Q2/Q3/Q4 | 2-3 horas |

---

## RESPONSABLE

- **Creación:** Daniel (CEO) — solo él tiene visión completa de todas las métricas
- **Lectura:** Daniel — primera lectura del día junto al DAILY_BRIEF
- **Archivado:** Mantener histórico mensual — son la base para decisiones de presupuesto

---

## OBJETIVO 2026 — REFERENCIA CONSTANTE

```
OBJETIVO ANUAL:  $7,000,000 CAD
Promedio mensual requerido: $583,333 CAD
Promedio semanal requerido: $134,615 CAD
Tasa de cierre requerida: ___% (calibrar con datos reales)
```

Cada Dashboard debe mostrar el % de avance hacia el objetivo de $7M CAD.

---

## CONEXIÓN CON OTROS SISTEMAS

- **Lee desde:** `RESUMENES_DIARIOS/` (input principal)
- **Lee desde:** `CRM/`, `META_ADS/`, `OPERACIONES/` (validación)
- **Referencia:** `10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/CEO_DASHBOARD_TEMPLATE.md`
- **Alimenta:** Decisiones estratégicas de Daniel (presupuestos, contrataciones, pausa de campañas)
