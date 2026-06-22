# GOOGLE ADS — Métricas de Campañas

## 1. Qué datos deben ir aquí

Rendimiento de todas las campañas activas en Google Ads del día anterior.
Incluye campañas de búsqueda y Performance Max.

Incluye:
- Gasto por campaña vs. presupuesto diario
- Leads / conversiones por campaña
- CPL (Costo por Lead) y CPC (Costo por Clic)
- CTR — objetivo >5% en búsqueda
- Quality Score promedio
- Estado de cada campaña

## 2. Formato

**Archivo:** `google_ads_YYYY-MM-DD.json` (fecha = día del que son los datos)  
**Actualizar:** cada mañana con datos de ayer desde Google Ads

```json
{
  "fecha_datos": "2026-06-21",
  "fecha_actualizacion": "2026-06-22T07:00:00",
  "campanas": [
    {
      "nombre": "Búsqueda: Pavé-uni Montreal",
      "tipo": "busqueda",
      "presupuesto_diario_cad": 65,
      "gasto_cad": 61.80,
      "impresiones": 920,
      "clics": 61,
      "ctr_pct": 6.63,
      "cpc_cad": 1.01,
      "conversiones": 2,
      "cpl_cad": 30.90,
      "quality_score_promedio": 7.4,
      "cpl_objetivo_cad": 75,
      "estado": "normal",
      "nota": ""
    },
    {
      "nombre": "Búsqueda: Aménagement paysager",
      "tipo": "busqueda",
      "presupuesto_diario_cad": 50,
      "gasto_cad": 48.20,
      "impresiones": 640,
      "clics": 28,
      "ctr_pct": 4.38,
      "cpc_cad": 1.72,
      "conversiones": 1,
      "cpl_cad": 48.20,
      "quality_score_promedio": 6.1,
      "cpl_objetivo_cad": 80,
      "estado": "atencion",
      "nota": "CTR por debajo de 5% — revisar keywords y match types"
    },
    {
      "nombre": "Performance Max — Gran Montreal",
      "tipo": "performance_max",
      "presupuesto_diario_cad": 33,
      "gasto_cad": 33.00,
      "impresiones": 4200,
      "clics": 105,
      "ctr_pct": 2.50,
      "cpc_cad": 0.31,
      "conversiones": 0,
      "cpl_cad": 0,
      "quality_score_promedio": null,
      "cpl_objetivo_cad": 85,
      "estado": "atencion",
      "nota": "0 conversiones hoy — normal en PMax, evaluar semana completa"
    }
  ],
  "totales": {
    "gasto_total_cad": 143.00,
    "presupuesto_total_cad": 148,
    "pct_presupuesto_ejecutado": 96.6,
    "leads_totales": 3,
    "cpl_promedio_cad": 47.67,
    "ctr_promedio_pct": 4.50,
    "cpc_promedio_cad": 1.35
  },
  "alertas": {
    "cpl_critico": [],
    "ctr_bajo_busqueda": ["Búsqueda: Aménagement paysager"],
    "quality_score_bajo": [],
    "sin_conversiones_con_presupuesto": []
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `fecha_datos` = ayer, `fecha_actualizacion` = hoy
- ✅ Todas las campañas activas (Performance Max incluido)
- ✅ `quality_score_promedio: null` es válido para Performance Max
- ✅ `totales` reflejan solo campañas activas

Umbrales que generan alertas en el reporte:
- `cpl_cad > 150` → alerta roja
- `ctr_pct < 3.0` en búsqueda → alerta naranja
- `quality_score_promedio < 5` → alerta naranja
- `conversiones == 0` con `gasto_cad > 30` en búsqueda → alerta amarilla

## 4. Cómo será leído por el motor de reportes

El script busca `google_ads_YYYY-MM-DD.json` con la fecha de ayer.

Lee:
- `campanas[]` → tabla "Google Ads" en sección de Marketing
- `totales.leads_totales` → se suma al total de leads del día
- `totales.cpl_promedio_cad` → comparado vs. objetivo <75 CAD
- `totales.ctr_promedio_pct` → comparado vs. objetivo >5%
- `alertas.*` → cualquier array no vacío genera alerta en el reporte

Si el archivo no existe:
```
⚠️ ALERTA — GOOGLE ADS: sin datos para 2026-06-21
   No se puede reportar rendimiento de campañas Google.
   Verificar Google Ads y actualizar manualmente.
```

**Fuente recomendada:**
- Google Ads → Campañas → rango "Ayer" → Exportar CSV → convertir a JSON
- **Futuro:** Make.com + Google Ads API puede poblar automáticamente cada noche
