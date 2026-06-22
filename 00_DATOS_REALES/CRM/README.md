# CRM — Datos del Pipeline de Ventas

## 1. Qué datos deben ir aquí

Estado completo del pipeline de ventas al momento de generar el reporte.
Un archivo por día, con todos los leads organizados por etapa.

Incluye:
- Leads en cada etapa: Nuevo, Contactado, Calificado, Propuesta enviada, Cerrado ganado, Cerrado perdido
- Tiempo sin contacto por lead
- Alertas activas (sin contacto >24h, detenidos >7 días)
- Seguimientos que vencen hoy

## 2. Formato

**Archivo:** `leads_pipeline_YYYY-MM-DD.json`  
**Actualizar:** cada mañana antes de las 07:00 AM

```json
{
  "fecha_actualizacion": "2026-06-22T07:00:00",
  "pipeline": {
    "nuevo": [
      {
        "id": "L001",
        "nombre": "Jean Tremblay",
        "telefono": "514-555-0100",
        "email": "jean@email.com",
        "servicio": "pavé-uni",
        "zona": "Laval",
        "fuente": "Meta Ads",
        "hora_entrada": "2026-06-21T14:30:00",
        "horas_sin_contacto": 16.5,
        "notas": ""
      }
    ],
    "contactado": [
      {
        "id": "L002",
        "nombre": "Marie Côté",
        "telefono": "438-555-0200",
        "servicio": "cour arrière",
        "zona": "Montréal",
        "fuente": "Google Ads",
        "ultimo_contacto": "2026-06-21T10:00:00",
        "dias_sin_avance": 1,
        "proxima_accion": "llamada de calificación",
        "notas": "Interesada para julio"
      }
    ],
    "calificado": [],
    "propuesta_enviada": [
      {
        "id": "L003",
        "nombre": "Paul Gagné",
        "telefono": "514-555-0300",
        "servicio": "escaliers extérieurs",
        "monto_propuesta_cad": 8500,
        "fecha_envio": "2026-06-14",
        "dias_sin_respuesta": 8,
        "validez_hasta": "2026-06-28",
        "notas": ""
      }
    ],
    "cerrado_ganado": [],
    "cerrado_perdido": []
  },
  "alertas": {
    "sin_contacto_mas_24h": 1,
    "detenidos_mas_7_dias": 0,
    "propuestas_sin_respuesta_mas_7_dias": 1,
    "seguimientos_vencen_hoy": [
      {
        "nombre": "Marie Côté",
        "tipo": "llamada de calificación",
        "plazo": "antes del mediodía"
      }
    ]
  },
  "indicadores": {
    "total_leads_activos": 3,
    "valor_pipeline_cad": 8500,
    "tasa_contacto_menos_2h_pct": 80
  }
}
```

## 3. Ejemplo de archivo válido

Ver el bloque JSON de arriba. Un archivo válido tiene:
- ✅ `fecha_actualizacion` con formato ISO 8601
- ✅ Las 6 etapas del pipeline presentes (aunque estén vacías: `[]`)
- ✅ Cada lead con al menos `nombre`, `telefono`, `servicio`, `fuente`
- ✅ Sección `alertas` con los conteos numéricos
- ✅ Sección `indicadores` con los KPIs del día

Un archivo **inválido** o que genera alerta en el reporte:
- ❌ Archivo no existe → alerta: "CRM sin datos — verificar exportación"
- ❌ Archivo vacío o `{}` → alerta: "CRM vacío — pipeline no actualizado"
- ❌ `fecha_actualizacion` con más de 24h de antigüedad → alerta: "Datos CRM desactualizados"

## 4. Cómo será leído por el motor de reportes

El script `scripts/generar_reporte.py` busca el archivo más reciente con el patrón `leads_pipeline_*.json` en esta carpeta.

Lee:
- Conteo de leads por etapa → sección "Pipeline" del reporte
- `alertas.sin_contacto_mas_24h` → si >0, genera alerta roja en el reporte
- `alertas.detenidos_mas_7_dias` → si >0, genera alerta naranja
- `alertas.seguimientos_vencen_hoy` → lista en sección "Prioridades 09:00 AM"
- `indicadores.valor_pipeline_cad` → aparece en resumen ejecutivo

Si el archivo no existe, el motor escribe en el reporte:
```
⚠️ ALERTA — CRM: archivo no encontrado en 00_DATOS_REALES/CRM/
   Sección omitida. Actualizar antes de las 09:00 AM.
```

**Fuente recomendada:** Exportar desde Pipedrive → Vista Pipeline → Exportar CSV → convertir a JSON.  
**Alternativa manual:** Llenar este archivo directamente cada mañana.
