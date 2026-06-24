# 08_REPORTES / META_ADS
**Responsable:** Daniel (gestor de campañas)
**Frecuencia:** Revisión diaria 08:00h + reporte semanal lunes

---

## QUÉ SE ALMACENA AQUÍ

Todo lo relacionado con el rendimiento de campañas en Meta Ads (Facebook + Instagram).

### Archivos esperados

| Tipo | Nombre de archivo | Frecuencia |
|------|------------------|-----------|
| Snapshot diario de campañas | `meta_ads_YYYY-MM-DD.md` | Diario (si hay campañas activas) |
| Reporte semanal de rendimiento | `meta_ads_semana_YYYY-WNN.md` | Semanal (lunes) |
| Reporte por campaña específica | `meta_ads_campagna_[NOMBRE].md` | Por campaña |
| Registro de creativos A/B | `meta_ads_ab_test_[NOMBRE].md` | Por test |

### Campos mínimos en cada reporte Meta Ads

```
META ADS — YYYY-MM-DD

CAMPAÑAS ACTIVAS HOY: ___

POR CAMPAÑA:
  [Nombre campaña]
    Presupuesto/día:   $___  CAD
    Alcance:           ___   personas
    Clics:             ___
    CTR:               ___%
    CPL (costo/lead):  $___  CAD  ← MÉTRICA MÁS IMPORTANTE
    Leads generados:   ___
    ROAS (si ecommerce): ___

ALERTA CPL > $100 CAD → pausar campaña inmediatamente

CREATIVOS:
  Mejor rendimiento: [nombre imagen] → CTR: ___%
  Peor rendimiento:  [nombre imagen] → CTR: ___%
  Decisión: ___________________________________
```

---

## FRECUENCIA DE ACTUALIZACIÓN

| Acción | Cuándo |
|--------|--------|
| Revisión rápida CPL | Cada día hábil 08:00h — antes del brief diario |
| Snapshot completo | Cada día con campañas activas |
| Reporte semanal | Lunes AM — incluye comparativa semana anterior |
| Reporte por campaña | Al cerrar cada campaña (7-14 días) |
| A/B test result | Al determinar ganador (mínimo 3 días de datos) |

---

## RESPONSABLE

- **Plataforma:** Meta Ads Manager (acceso: daniel@groupe-ideal.com)
- **Revisión:** Daniel — revisión diaria de CPL y leads
- **Alertas automáticas:** Meta Ads Manager → email si CPL supera umbral
- **Futuro:** Zapier → Meta Ads Leads → Pipedrive (Automatización Zap #3)

---

## KPIs OBJETIVO (referencia)

| Métrica | Objetivo | Alerta si... |
|---------|----------|-------------|
| CPL (Cour Avant) | <$65 CAD | >$100 CAD → pausar |
| CPL (Piscines) | <$80 CAD | >$120 CAD → pausar |
| CTR | >1.5% | <0.8% → cambiar creativo |
| Frecuencia | <3.0 | >4.0 → renovar audiencia |
| Leads/semana | ≥5 | <2 → revisar targeting |

---

## CONEXIÓN CON OTROS SISTEMAS

- **Fuente:** Meta Ads Manager (exportar CSV o registrar manualmente)
- **Alimenta:** `CRM/` — los leads generados entran al pipeline
- **Alimenta:** `RESUMENES_DIARIOS/` — sección de campañas en reporte diario
- **Alimenta:** `DASHBOARDS/` — KPIs de marketing del CEO Dashboard
- **Creativas:** `05_MARKETING/CAMPAGNES_TEST/` — registro de qué imágenes se usaron

---

## REGISTRO DE CAMPAÑAS ACTIVAS

Actualizar este campo cuando haya cambios:

```
ÚLTIMA ACTUALIZACIÓN: 2026-06-24

CAMPAÑAS ACTIVAS:
  COUR_AVANT_TEST_01 — Hero Post → $15 CAD/día → activa desde ___
  COUR_AVANT_TEST_01 — Reel     → $20 CAD/día → activa desde ___
  COUR_AVANT_TEST_01 — Rmktg   → $25 CAD/día → activa desde ___

CAMPAÑAS EN PAUSA:
  (ninguna)

CAMPAÑAS CERRADAS (este mes):
  (ninguna)
```
