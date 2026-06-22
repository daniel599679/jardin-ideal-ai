# META ADS — Métricas de Campañas

## 1. Qué datos deben ir aquí

Rendimiento de todas las campañas activas en Meta Ads (Facebook e Instagram) del día anterior.
Se actualiza cada mañana con los datos de ayer para que el reporte del día refleje el estado real.

Incluye:
- Gasto por campaña vs. presupuesto diario
- Leads generados por campaña
- CPL (Costo por Lead) por campaña
- CTR (Click Through Rate)
- Frecuencia del anuncio (alerta si >3.5)
- Estado de cada campaña: normal / atención / problema

## 2. Formato

**Archivo:** `meta_ads_YYYY-MM-DD.json` (fecha = día del que son los datos)  
**Actualizar:** cada mañana con datos de ayer desde Meta Ads Manager

```json
{
  "fecha_datos": "2026-06-21",
  "fecha_actualizacion": "2026-06-22T07:00:00",
  "campanas": [
    {
      "nombre": "Pavé-uni & Entrées — Montreal",
      "objetivo": "lead_generation",
      "presupuesto_diario_cad": 100,
      "gasto_cad": 97.40,
      "impresiones": 13200,
      "clics": 341,
      "ctr_pct": 2.58,
      "leads": 3,
      "cpl_cad": 32.47,
      "frecuencia_7_dias": 2.9,
      "cpl_objetivo_cad": 80,
      "estado": "normal",
      "nota": ""
    },
    {
      "nombre": "Cour Avant/Arrière — Laval",
      "objetivo": "lead_generation",
      "presupuesto_diario_cad": 65,
      "gasto_cad": 64.10,
      "impresiones": 8900,
      "clics": 178,
      "ctr_pct": 2.00,
      "leads": 1,
      "cpl_cad": 64.10,
      "frecuencia_7_dias": 3.6,
      "cpl_objetivo_cad": 70,
      "estado": "atencion",
      "nota": "Frecuencia superó 3.5 — rotar creatividades esta semana"
    },
    {
      "nombre": "Piscinas — Gran Montreal",
      "objetivo": "lead_generation",
      "presupuesto_diario_cad": 50,
      "gasto_cad": 0,
      "impresiones": 0,
      "clics": 0,
      "ctr_pct": 0,
      "leads": 0,
      "cpl_cad": 0,
      "frecuencia_7_dias": 0,
      "cpl_objetivo_cad": 120,
      "estado": "pausada",
      "nota": "Pausada manualmente el 2026-06-20"
    }
  ],
  "totales": {
    "gasto_total_cad": 161.50,
    "presupuesto_total_cad": 215,
    "pct_presupuesto_ejecutado": 75.1,
    "leads_totales": 4,
    "cpl_promedio_cad": 40.38,
    "ctr_promedio_pct": 2.32,
    "frecuencia_promedio": 3.25
  },
  "alertas": {
    "cpl_critico": [],
    "frecuencia_alta": ["Cour Avant/Arrière — Laval"],
    "ctr_bajo": [],
    "sin_leads_con_presupuesto_activo": [],
    "presupuesto_agotado_antes_15h": []
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `fecha_datos` = ayer, `fecha_actualizacion` = hoy
- ✅ Todas las campañas activas listadas (pausadas incluidas con `estado: "pausada"`)
- ✅ `totales` calculados correctamente (suma de campañas activas)
- ✅ Sección `alertas` con arrays (vacíos si no hay alertas)

Umbrales que generan alertas automáticas en el reporte:
- `cpl_cad > 150` → alerta roja
- `ctr_pct < 1.0` durante 3 días → alerta roja
- `frecuencia_7_dias > 3.5` → alerta naranja
- `leads == 0` con `gasto_cad > 0` y `estado != "pausada"` → alerta naranja
- `pct_presupuesto_ejecutado < 50` a las 17:00 → alerta amarilla

## 4. Cómo será leído por el motor de reportes

El script busca `meta_ads_YYYY-MM-DD.json` con la fecha de ayer.

Lee:
- `campanas[]` → tabla "Estado de Campañas" con semáforo de color
- `totales.leads_totales` → contribuye al total de leads del día
- `totales.cpl_promedio_cad` → comparado vs. objetivo <75 CAD (junio)
- `totales.ctr_promedio_pct` → comparado vs. objetivo >2.5%
- `alertas.*` → cualquier array no vacío genera sección de alerta en el reporte
- Campañas con `frecuencia_7_dias > 3.5` → tarea en prioridades: "Rotar creatividades"

Si el archivo no existe:
```
⚠️ ALERTA — META ADS: sin datos para 2026-06-21
   No se puede reportar rendimiento de campañas Meta.
   Verificar Meta Ads Manager y actualizar manualmente.
```

**Fuente recomendada:**
- Meta Ads Manager → Campañas → seleccionar rango "Ayer" → Exportar (columnas: nombre, gasto, impresiones, clics, CTR, leads, CPL, frecuencia)
- **Futuro:** Make.com + Meta Marketing API puede poblar este archivo automáticamente cada noche a las 06:30
