# LEADS — Nuevos Leads del Día

## 1. Qué datos deben ir aquí

Todos los leads nuevos que entraron en las últimas 24 horas, antes de ser procesados en el CRM.
Esta carpeta captura el volumen y la fuente de leads del día — es la entrada del embudo.

Incluye:
- Leads de Meta Ads (formulario instantáneo)
- Leads de Google Ads (formulario web)
- Leads por DM de Instagram o Facebook
- Leads por llamada directa o referido
- Cantidad total, fuente, hora de entrada, campos completos o incompletos

## 2. Formato

**Archivo:** `leads_nuevos_YYYY-MM-DD.json`  
**Actualizar:** cada mañana con los leads de las últimas 24h

```json
{
  "fecha": "2026-06-22",
  "periodo": "2026-06-21T18:00:00 a 2026-06-22T07:00:00",
  "leads": [
    {
      "id": "L2026-0622-001",
      "hora_entrada": "2026-06-21T19:45:00",
      "nombre": "François Bergeron",
      "telefono": "450-555-0101",
      "email": "",
      "servicio_interes": "pavé-uni",
      "zona": "Laval",
      "fuente": "Meta Ads",
      "canal": "formulario_instantaneo",
      "mensaje": "",
      "campos_completos": true,
      "primer_contacto_realizado": false,
      "horas_esperando": 11.25
    },
    {
      "id": "L2026-0622-002",
      "hora_entrada": "2026-06-22T06:30:00",
      "nombre": "Sophie Larivière",
      "telefono": "514-555-0202",
      "email": "sophie@email.com",
      "servicio_interes": "cour arrière",
      "zona": "Montréal-Nord",
      "fuente": "Google Ads",
      "canal": "formulario_web",
      "mensaje": "Je voudrais un estimé pour refaire ma cour arrière complète.",
      "campos_completos": true,
      "primer_contacto_realizado": false,
      "horas_esperando": 0.5
    },
    {
      "id": "L2026-0622-003",
      "hora_entrada": "2026-06-21T20:10:00",
      "nombre": "Compte Instagram inconnu",
      "telefono": "",
      "email": "",
      "servicio_interes": "desconocido",
      "zona": "",
      "fuente": "Instagram DM",
      "canal": "dm_instagram",
      "mensaje": "Bonjour, est-ce que vous faites des allées latérales?",
      "campos_completos": false,
      "campos_faltantes": ["telefono", "zona", "servicio_confirmado"],
      "primer_contacto_realizado": true,
      "horas_esperando": 10.8
    }
  ],
  "resumen": {
    "total_leads_hoy": 3,
    "por_fuente": {
      "meta_ads": 1,
      "google_ads": 1,
      "instagram_dm": 1,
      "facebook_dm": 0,
      "llamada_directa": 0,
      "referido": 0
    },
    "sin_primer_contacto": 2,
    "con_campos_incompletos": 1
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `fecha` del día actual
- ✅ Cada lead con `hora_entrada`, `nombre`, `fuente`, `horas_esperando`
- ✅ `campos_completos: false` acompañado de `campos_faltantes` listados
- ✅ `resumen.total_leads_hoy` igual al número de objetos en `leads`
- ✅ Array `leads: []` vacío es válido — significa que no llegaron leads nuevos

Umbral de alerta: cualquier lead con `horas_esperando > 24` y `primer_contacto_realizado: false` → alerta roja.

## 4. Cómo será leído por el motor de reportes

El script busca `leads_nuevos_YYYY-MM-DD.json` con la fecha del día.

Lee:
- `resumen.total_leads_hoy` → "Leads del día" en resumen ejecutivo
- `resumen.por_fuente` → tabla de leads por canal
- `resumen.sin_primer_contacto` → si >0, tarea crítica en Prioridades 09:00 AM
- Leads con `horas_esperando > 2` → listados como alertas CRM
- Leads con `campos_completos: false` → listados para completar en CRM

Si el archivo no existe:
```
⚠️ ALERTA — LEADS: archivo no encontrado para 2026-06-22
   No se puede reportar volumen de leads. Verificar captura.
```

**Fuente recomendada:**
- Meta Ads → Meta Business Suite → Formularios → Descargar leads del día
- Google Ads → Conversiones → Exportar
- DMs → Revisar manualmente y registrar aquí
- **Futuro:** Make.com puede poblar este archivo automáticamente al llegar cada lead
