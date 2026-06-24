# 08_REPORTES / CRM
**Responsable:** Daniel (vendedor principal)
**Frecuencia:** Actualización diaria antes de las 18:00h

---

## QUÉ SE ALMACENA AQUÍ

Todo lo relacionado con el estado del pipeline de ventas y la gestión de leads en Pipedrive.

### Archivos esperados

| Tipo | Nombre de archivo | Frecuencia |
|------|------------------|-----------|
| Snapshot diario del pipeline | `crm_pipeline_YYYY-MM-DD.md` | Diario |
| Reporte de leads por semana | `crm_leads_semana_YYYY-WNN.md` | Semanal (lunes) |
| Seguimiento de propuestas abiertas | `crm_propuestas_abiertas.md` | Actualizar al cambiar |
| Leads sin contactar >24h | `crm_alertas_YYYY-MM-DD.md` | Cuando aplique |

### Campos mínimos en cada reporte CRM

```
PIPELINE HOY — YYYY-MM-DD

LEADS NUEVOS HOY:        ___
LEADS CONTACTADOS:       ___
LEADS SIN CONTACTAR:     ___  ← si >0, alerta inmediata

POR ETAPA:
  Nuevo (sin contactar): ___
  Contactado:            ___
  Soumission enviada:    ___
  Negociación:           ___
  Ganado:                ___
  Perdido:               ___

DEALS CRÍTICOS (ICS ≥85):
  1. [Nombre] — $___K — Etapa: ___ — Último contacto: ___
  2. [Nombre] — $___K — Etapa: ___ — Último contacto: ___

FOLLOW-UPS URGENTES HOY:
  [ ] _______________________________________________
  [ ] _______________________________________________
```

---

## FRECUENCIA DE ACTUALIZACIÓN

| Acción | Cuándo |
|--------|--------|
| Nuevo lead entra | Inmediato — Pipedrive lo captura automáticamente (futuro: Zapier) |
| Snapshot del pipeline | Cada día hábil antes de 18:00h |
| Reporte semanal CRM | Lunes AM antes de la reunión 09:00h |
| Propuestas abiertas | Actualizar cada vez que cambie una etapa |

---

## RESPONSABLE

- **Captura de datos:** Pipedrive (automático) + Daniel (manual hasta Zapier activo)
- **Lectura diaria:** Daniel — primer input del START_DAY_ENGINE a las 07:00h
- **Alertas:** Daniel — lead sin contactar >2h (PRE-A) o >4h (PRE-B)

---

## CONEXIÓN CON OTROS SISTEMAS

- **Fuente:** Pipedrive CRM + formulario landing page (futuro: Zapier)
- **Consume:** `06_CRM/` (fichas de leads individuales)
- **Alimenta:** `RESUMENES_DIARIOS/` (el reporte diario incluye sección CRM)
- **Alimenta:** `DASHBOARDS/` (KPIs de ventas del CEO Dashboard)

---

## ALERTAS CRÍTICAS (registrar aquí si ocurren)

Crear archivo `crm_alerta_YYYY-MM-DD.md` cuando:
- Lead PRE-A sin contactar en >2 horas
- Propuesta enviada sin respuesta en >5 días
- Deal ganado — registrar para reporte de ingresos
- Deal perdido — registrar razón para análisis mensual
